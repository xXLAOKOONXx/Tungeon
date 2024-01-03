from tungeon.config.schema.functionality import Functionality
from tungeon.data.hero import Hero
from tungeon.logics import functionality_system

def is_effected_by_wound(hero:Hero):
    if not hero.wounds:
        return False
    funcs = functionality_system.get_functionalities(hero)
    wound_threshhold = 0
    for func in funcs:
        if func.wound_resistance and functionality_system.check_conditions_met(func, hero):
            if func.base_skill_check:
                if not functionality_system.do_check(hero, func):
                    continue
            wound_threshhold += func.wound_resistance
    return hero.wounds <= wound_threshhold
            

def should_die(hero:Hero):
    if not hero.wounds:
        return False
    funcs = functionality_system.get_functionalities(hero)
    wound_threshhold = 2
    for func in funcs:
        if func.death_wound_resistance and functionality_system.check_conditions_met(func, hero):
            if func.base_skill_check:
                if not functionality_system.do_check(hero, func):
                    continue
            wound_threshhold += func.death_wound_resistance
    return hero.wounds >= wound_threshhold
    