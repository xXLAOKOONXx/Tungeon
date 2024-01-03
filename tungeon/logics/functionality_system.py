from tungeon.config.schema.functionality import Functionality
from tungeon.data.company import Company
from tungeon.data.hero import Hero
from tungeon.data.round_effects import RoundEffect
from tungeon.logics import config_finder
from tungeon.data.condition	import condition, HeroCondition
from tungeon.logics.ui_connection import get_skillcheck_dialog

def check_conditions_met(functionality:Functionality, hero:Hero) -> bool:
    if condition.get_hero_condition(hero.name) and any(fg in condition.get_hero_condition(hero.name).used_skill_groups for fg in functionality.function_groups):
        return False
    if not functionality.condition_type:
        return True
    if functionality.regions and condition.region_name not in functionality.regions:
        return False
    if functionality.condition_type == 'round-preperation':
        return condition.is_prep and condition.get_hero_condition(hero.name)
    if functionality.condition_type == 'fight':
        hero_condition = condition.get_hero_condition(hero.name)
        ft = ((functionality.fight_type is None) or 
            (functionality.fight_type == 'melee' and hero_condition.is_melee) or 
            (functionality.fight_type == 'ranged' and not hero_condition.is_melee))
        vf = (not functionality.fight_voluntary_required or not condition.is_forced)
        e_min = (not functionality.fight_enemy_min or condition.enemy_count)
        fr = (not functionality.fight_rounds or condition.fight_round in functionality.fight_rounds)
        et = (not functionality.fight_enemy_types or (condition.enemy_types and any([t in functionality.fight_enemy_types for t in condition.enemy_types])))
        return ft and vf and e_min and fr and et
    if functionality.condition_type == 'dice-reroll':
        if any([rt in condition.check_types for rt in functionality.reroll_types]):
            return True
    
def get_functionalities(hero:Hero) -> list[Functionality]:
    functions:list[Functionality] = []
    for skill_name in hero.skills:
        skill = config_finder.get_skill(skill_name)
        functions += skill.functions
    for item_name in hero.active_items:
        item = config_finder.get_item(item_name)
        functions += item.functions
    return functions
    