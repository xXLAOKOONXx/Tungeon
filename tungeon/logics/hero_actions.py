import random
from tungeon.config.schema.base_skill_check import BaseSkillCheck
from tungeon.config.schema.functionality import Functionality
from tungeon.config.schema.region_event import RegionEventStep
from tungeon.data.hero import Hero
from tungeon.data.condition	import condition
from tungeon.data.round_effects import RoundEffect
from tungeon.logics.ui_connection import get_skillcheck_dialog
from tungeon.logics.hero_status import is_effected_by_wound


def add_base_check_condition(base_skill_check:BaseSkillCheck):
    if base_skill_check.is_strength:
        condition.base_skill = 'strength'
    if base_skill_check.is_speed:
        condition.base_skill = 'speed'
    if base_skill_check.is_agility:
        condition.base_skill = 'agility'
    if base_skill_check.is_intelligence:
        condition.base_skill = 'intelligence'
    condition.check_types = base_skill_check.check_types
    condition.check_modifier = base_skill_check.check_modifier

def remove_base_check_condition():
    condition.base_skill = None
    condition.check_types = []
    condition.check_modifier = 0

def do_check(hero:Hero, functionality:Functionality) -> bool:    
    if is_effected_by_wound(hero):
        return False
    if functionality.base_skill_check:
        add_base_check_condition(functionality.base_skill_check)
        skill_check_result = get_skillcheck_dialog()(hero)
        remove_base_check_condition()
        return skill_check_result
    return True

def do_step_check(hero:Hero, step:RegionEventStep) -> bool:    
    if is_effected_by_wound(hero):
        return False
    if step.base_skill_check:
        add_base_check_condition(step.base_skill_check)
        skill_check_result = get_skillcheck_dialog()(hero)
        remove_base_check_condition()
        return skill_check_result
    return True


def pop_random_poison(target_hero:Hero, poison_types:list[str]|None) -> bool:
    poison_idx = [idx for idx, p in enumerate(target_hero.poisons) if not poison_types or any(any([pt in hpt for hpt in poison_types]) for pt in p.poison_types)]
    if not poison_idx:
        return False
    pop_idx = random.sample(poison_idx, 1)[0]
    target_hero.poisons.pop(pop_idx)
    return True
    

def apply_prepare_functionality(hero:Hero, target_hero:Hero, functionality:Functionality):
    if functionality.base_skill_check:
        add_base_check_condition(functionality.base_skill_check)
        skill_check_result = get_skillcheck_dialog()(hero)
        remove_base_check_condition()
        if not skill_check_result:
            return
    
    if functionality.heals_poison:
        for _ in range(0,functionality.poison_count_cleaning or len(target_hero.poisons)):
            pop_random_poison(target_hero, functionality.healing_poison_types)

    round_effect = RoundEffect(
        round_count=0 + (functionality.additional_rounds or 0),
        bonus_strength=functionality.strength_bonus,
        bonus_agility=functionality.agility_bonus,
        bonus_speed=functionality.speed_bonus,
        bonus_intelligence=functionality.intelligence_bonus,
        bonus_melee_damage=functionality.fight_flat_bonus if functionality.fight_type=='melee' or functionality.fight_type is None else 0,
        bonus_ranged_damage=functionality.fight_flat_bonus if functionality.fight_type=='ranged' or functionality.fight_type is None else 0,
        poison_type_preventions=functionality.poison_type_preventions or []
    )
    target_hero.round_effects.append(round_effect)