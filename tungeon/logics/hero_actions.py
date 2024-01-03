from tungeon.config.schema.functionality import Functionality
from tungeon.data.hero import Hero
from tungeon.data.condition	import condition
from tungeon.data.round_effects import RoundEffect
from tungeon.logics.ui_connection import get_skillcheck_dialog
from tungeon.logics.hero_status import is_effected_by_wound


def add_base_check_condition(functionality:Functionality):
    if functionality.base_skill_check.is_strength:
        condition.base_skill = 'strength'
    if functionality.base_skill_check.is_speed:
        condition.base_skill = 'speed'
    if functionality.base_skill_check.is_agility:
        condition.base_skill = 'agility'
    if functionality.base_skill_check.is_intelligence:
        condition.base_skill = 'intelligence'
    condition.check_types = functionality.base_skill_check.check_types
    condition.check_modifier = functionality.base_skill_check.check_modifier

def remove_base_check_condition():
    condition.base_skill = None
    condition.check_types = []
    condition.check_modifier = 0

def do_check(hero:Hero, functionality:Functionality) -> bool:    
    if is_effected_by_wound(hero):
        return False
    if functionality.base_skill_check:
        add_base_check_condition(functionality)
        skill_check_result = get_skillcheck_dialog()(hero)
        remove_base_check_condition()
        return skill_check_result
    return True
    

def apply_prepare_functionality(hero:Hero, target_hero:Hero, functionality:Functionality):
    if functionality.base_skill_check:
        add_base_check_condition(functionality)
        skill_check_result = get_skillcheck_dialog()(hero)
        remove_base_check_condition()
        if not skill_check_result:
            return

    round_effect = RoundEffect(
        round_count=0 + (functionality.additional_rounds or 0),
        bonus_strength=functionality.strength_bonus,
        bonus_agility=functionality.agility_bonus,
        bonus_speed=functionality.speed_bonus,
        bonus_intelligence=functionality.intelligence_bonus,
        bonus_melee_damage=functionality.fight_flat_bonus if functionality.fight_type=='melee' or functionality.fight_type is None else 0,
        bonus_ranged_damage=functionality.fight_flat_bonus if functionality.fight_type=='ranged' or functionality.fight_type is None else 0
    )
    target_hero.round_effects.append(round_effect)