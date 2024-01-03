

from typing import Tuple
from tungeon.config.schema.base_skill_check import BaseSkillCheck
from tungeon.config.schema.item import Item
from tungeon.data.hero import Hero
from tungeon.logics import config_finder


def item_can_reroll_base_skill_check(item:Item, check_types:list[str], region_name:str) -> Tuple[bool, bool]:
    '''
    Returns:
    - can_reroll(bool)
    - gets_destroyed(bool)
    '''
    reroll_functions = [f for f in item.functions if f.condition_type == 'dice-reroll']
    if not reroll_functions:
        return False, False
    legit_rerolls = [f for f in reroll_functions if region_name in f.regions and any([check_type in f.reroll_types for check_type in check_types])]
    
    if not legit_rerolls:
        return False, False
    return True, all([f.destructive for f in legit_rerolls])


def get_functionable_items_for_check(hero:Hero, check_types:list[str], region_name:str) -> Tuple[list[Item], list[bool]]:
    active_items = [config_finder.get_item(item_name) for item_name in hero.active_items]
    functionable_items:list[Item] = []
    destruction = []
    for item in active_items:
        val, des = item_can_reroll_base_skill_check(item, check_types, region_name)
        if val:
            functionable_items += [item]
            destruction += [des]
    return functionable_items, destruction