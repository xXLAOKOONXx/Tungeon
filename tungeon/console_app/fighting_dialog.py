import random
from tungeon.config.schema.region_event import RegionEventStep
from tungeon.data.company import Company
from tungeon.logics import fightingsystem, item_effects
from tungeon.console_app import helpers

from tungeon.data.hero import Hero
from tungeon.config.game_config import game_config
from tungeon.data.condition import HeroCondition, condition

def determine_hero_is_melee(hero:Hero) -> bool:
    '''
    Returns:
    - is_melee(bool)
    '''
    can_ranged = fightingsystem.is_allowed_fighting(hero, is_melee=False)
    if not can_ranged:
        return True
    print(str(hero))
    return helpers.select_yes_no(text=f'{hero.name}: {game_config.language_package.fight_melee_question}')
    

def determine_is_melee(heroes:list[Hero]):
    for hero in heroes:
        if hero.name not in condition.hero_condition.keys():
            condition.hero_condition[hero.name] = HeroCondition()
        condition.get_hero_condition(hero.name).is_melee = determine_hero_is_melee(hero)

def fight_round(company:Company, fight:RegionEventStep, region_name:str) -> fightingsystem.FightRoundResult:
    enemy_strength = fightingsystem.draw_enemy_strength(fight)
    fighting_heroes = [hero for hero in company.heroes if fightingsystem.is_allowed_fighting(hero, condition.get_hero_condition(hero.name).is_melee)]
    hero_base = fightingsystem.calculate_heroes_base_damage(fighting_heroes)
    
    roll_strength = 0
    for hero in fighting_heroes:
        is_melee = condition.get_hero_condition(hero.name).is_melee
        hero_roll = helpers.roll_hero_dice(hero, ['fight', 'melee' if is_melee else 'ranged'], region_name)
        roll_strength += hero_roll

    hero_strength = hero_base + roll_strength
    fight_result = fightingsystem.calculate_fight_round(hero_strength, fightingsystem.calculate_hero_resistance(company.heroes[0]), enemy_strength, fight.fight_enemy_resistance)
    return fight_result

def perform_fight(company:Company, fight:RegionEventStep, region_name:str) -> int | None:
    '''
    Returns:
    - continuation-id(int), None if there is no continuation-number
    '''
    def reset_condition():
        condition.is_fight = False
        condition.is_forced = False
        condition.enemy_count = None
        condition.fight_round = None
    condition.is_fight = True
    condition.is_forced = fight.is_forced
    condition.enemy_count = fight.fight_enemy_count
    if fight.fight_melee:
        for hero in company.heroes:
            condition.get_hero_condition(hero.name).is_melee = True
    elif fight.fight_ranged:
        for hero in company.heroes:
            condition.get_hero_condition(hero.name).is_melee = False
    else:
        determine_is_melee(company.heroes)
    for i in range(0,3):
        condition.fight_round = i + 1
        print(game_config.language_package.round_msg.format(round=i+1))
        fight_result = fight_round(company, fight, region_name)
        if not fight_result.is_tie:
            break
    if fight_result.is_tie:
        print(game_config.language_package.fight_tie)
        reset_condition()
        return fight.fight_tie or fight.next_step
    if fight_result.is_win:
        print(game_config.language_package.fight_win)
        reset_condition()
        return fight.fight_win or fight.next_step
    if fight_result.is_loose:
        print(game_config.language_package.fight_loose)
        applied_wounds = fightingsystem.apply_damage_on_players(company.heroes, strength_delta=fight_result.strength_delta)
        print(game_config.language_package.receive_wounds.format(wounds=applied_wounds))
        reset_condition()
        return fight.fight_loose or fight.next_step
    

