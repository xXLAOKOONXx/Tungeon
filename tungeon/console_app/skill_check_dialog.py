

import random
from tungeon.config.schema.base_skill_check import BaseSkillCheck
from tungeon.config.schema.item import Item
from tungeon.data.hero import Hero
from tungeon.logics import config_finder, item_effects
from tungeon.console_app import helpers


def perform_base_skill_check(hero:Hero, check:BaseSkillCheck, region_name:str) -> int | None:
    '''
    Returns delta from target or None on miss
    '''
    skill_name = ''
    skill_value = 0
    if check.is_agility:
        skill_name = 'Agilität'
        skill_value = hero.agility
    if check.is_speed:
        skill_name = 'Schnelligkeit'
        skill_value = hero.speed
    if check.is_strength:
        skill_name = 'Stärke'
        skill_value = hero.strength
    if check.is_intelligence:
        skill_name = 'Intelligenz'
        skill_value = hero.intelligence
    
    print(f'Du hast eine {skill_name} von {skill_value} und der Test hat einen Modifikator von {check.check_modifier}, damit benötigst du wenigstens {skill_value + check.check_modifier} oder niedriger.')

    if skill_value + check.check_modifier < 1:
        print('Du weisst, dass das nicht geht, damit scheitert dein Versuch.')
        return None
    
    dice_roll = helpers.roll_hero_dice(hero, check.check_types, region_name)

    check_result = (skill_value + check.check_modifier) - dice_roll

    if check_result < 0:
        return None

    return check_result
