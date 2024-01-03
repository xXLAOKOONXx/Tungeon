
from tungeon.data.company import Company
from tungeon.data.condition import condition
from dataclasses import dataclass
import random
from tungeon.config.schema.region_event import RegionEventStep
from tungeon.data.hero import Hero
from tungeon.config.game_config import game_config
from tungeon.logics.config_finder import get_item
from tungeon.logics import hero_status, functionality_system, ui_connection

def is_allowed_fighting(hero:Hero, is_melee:bool):
    if hero_status.is_effected_by_wound(hero):
        return False
    if not is_melee and not hero.ranged_weapon:
        return False
    return True

def calculate_hero_base_damage(hero:Hero):
    base_damage = 0
    if condition.get_hero_condition(hero.name).is_melee:
        if not hero.melee_weapon:
            base_damage -= 1
            melee_hands = 0
        else:
            item = get_item(hero.melee_weapon)
            base_damage += item.damage
            melee_hands = item.required_hands
        if hero.shield:
            shield = get_item(hero.shield)
            if shield.required_hands + melee_hands <= 2:
                base_damage += shield.damage or 0
        if hero.armor:
            armor = get_item(hero.armor)
            base_damage += armor.damage or 0
    else:
        if not hero.ranged_weapon:
            base_damage -= 1
        else:
            item = get_item(hero.ranged_weapon)
            base_damage += item.damage

    if condition.get_hero_condition(hero.name).is_melee:
        base_damage += hero.current_strength
    else:
        base_damage += hero.current_agility

    funcs = functionality_system.get_functionalities(hero)
    for func in funcs:
        if func.fight_flat_bonus:
            if functionality_system.check_conditions_met(func, hero):
                ui_connection.get_functionality_used_dialog()(func)
                base_damage += func.fight_flat_bonus
    return base_damage

def calculate_heroes_base_damage(heroes:list[Hero]):
    return sum([calculate_hero_base_damage(hero) for hero in heroes])

def calculate_prefered_is_melee(hero:Hero):
    return calculate_hero_base_damage(hero, is_melee=True) > calculate_hero_base_damage(hero, is_melee=False)

def calculate_hero_resistance(hero:Hero):
    resistance = 0
    if ((hero.shield and get_item(hero.shield).resistance) and
        ((condition.get_hero_condition(hero.name).is_melee and get_item(hero.melee_weapon).required_hands < 2) or
         ((not condition.get_hero_condition(hero.name).is_melee) and get_item(hero.ranged_weapon).required_hands < 2))):
        resistance += get_item(hero.shield).resistance
    if hero.armor and get_item(hero.armor).resistance:
        resistance += get_item(hero.armor).resistance
    return resistance


def is_win(player_strength, player_resistance, enemy_strength, enemy_resistance):
    return player_strength > (enemy_strength + enemy_resistance)
def is_loose(player_strength, player_resistance, enemy_strength, enemy_resistance):
    return enemy_strength > (player_strength + player_resistance)
def is_tie(player_strength, player_resistance, enemy_strength, enemy_resistance):
    return not is_loose(player_strength, player_resistance, enemy_strength, enemy_resistance) and not is_win(player_strength, player_resistance, enemy_strength, enemy_resistance)

@dataclass
class FightRoundResult:
    is_win:bool
    is_loose:bool
    strength_delta:int
    @property
    def is_tie(self) -> bool:
        return not self.is_win and not self.is_loose

def calculate_fight_round(player_strength, player_resistance, enemy_strength, enemy_resistance):
    return FightRoundResult(is_win=is_win(player_strength, player_resistance, enemy_strength, enemy_resistance),
                            is_loose=is_loose(player_strength, player_resistance, enemy_strength, enemy_resistance),
                            strength_delta=enemy_strength-player_strength)

def apply_damage_on_players(heroes, strength_delta) -> int:
    '''
    Returns:
    - applied_wounds(int): amount of wounds that got applied
    '''
    applied_wounds = 0
    applied_damage = strength_delta
    while applied_damage > 0:
        for hero in heroes:
            applied_damage -= calculate_hero_resistance(hero)
            if applied_damage < 0:
                break
            hero.wounds += 1
            applied_wounds += 1
            applied_damage -= 1
    return applied_wounds

def draw_enemy_strength(fight:RegionEventStep) -> int:
    base = fight.fight_enemy_base_damage
    for _ in range(0,fight.fight_enemy_dice):
        base += random.randint(1,6)
    return base

def calculate_enemy_resistance(company:Company, base_resistance:int) -> int:
    resistance = base_resistance
    passing_surpassing = 0
    passing_non_surpassing = 0
    for hero in company.heroes:
        funcs = functionality_system.get_functionalities(hero)
        for func in funcs:
            if func.resistance_passing:
                if functionality_system.check_conditions_met(func, hero):
                    ui_connection.get_functionality_used_dialog()(func)
                    if func.resistance_surpassing:
                        passing_surpassing += func.resistance_passing
                    else:
                        passing_non_surpassing += func.resistance_passing
    if passing_surpassing > resistance:
        return resistance - passing_surpassing
    if passing_surpassing + passing_non_surpassing > resistance:
        return 0
    return resistance - passing_non_surpassing - passing_surpassing
