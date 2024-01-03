

import random
from tungeon.config.schema.base_skill_check import BaseSkillCheck
from tungeon.config.schema.item import Item
from tungeon.data.hero import Hero
from tungeon.logics import config_finder, item_effects
from tungeon.console_app import helpers
from tungeon.config.game_config import game_config


def perform_base_skill_check(hero:Hero, check:BaseSkillCheck, region_name:str) -> int | None:
    '''
    Returns delta from target or None on miss
    '''
    skill_name = ''
    skill_value = 0
    if check.is_agility:
        skill_name = game_config.language_package.agility
        skill_value = hero.agility
    if check.is_speed:
        skill_name = game_config.language_package.speed
        skill_value = hero.speed
    if check.is_strength:
        skill_name = game_config.language_package.strength
        skill_value = hero.strength
    if check.is_intelligence:
        skill_name = game_config.language_package.intelligence
        skill_value = hero.intelligence
    
    print(game_config.language_package.skill_check_info.format(
        skill_name=skill_name,
        skill_value=skill_value,
        check_modifier=check.check_modifier,
        req_value=skill_value + check.check_modifier
    ))

    if skill_value + check.check_modifier < 1:
        print(game_config.language_package.skill_check_auto_no)
        return None
    
    dice_roll = helpers.roll_hero_dice(hero, check.check_types, region_name)

    check_result = (skill_value + check.check_modifier) - dice_roll

    if check_result < 0:
        return None

    return check_result
