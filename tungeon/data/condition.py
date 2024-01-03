import copy
from dataclasses import dataclass, field
from typing import Literal
from tungeon.data.hero import Hero

LITERAL_BASE_SKILLS = Literal['strength', 'agility', 'speed', 'intelligence']

@dataclass
class HeroCondition:
    '''
    class to hold hero specific conditions
    '''
    is_melee:bool = False
    used_skills:list[str] = field(default_factory=list)
    used_skill_groups:list[str] = field(default_factory=list)

@dataclass
class Condition:
    '''
    class to hold data for current conditions
    '''
    is_prep:bool=False
    is_fight:bool=False
    is_forced:bool=False
    fight_round:int|None=None
    enemy_count:int|None=None
    enemy_types:list[str]|None=None
    region_name:str=''
    check_types:list[str]=field(default_factory=list)
    base_skill:LITERAL_BASE_SKILLS|None=None
    check_modifier:int=0
    hero_condition:dict[str, HeroCondition]=field(default_factory=dict)

    def get_hero_condition(self, hero_name) -> HeroCondition:
        if hero_name not in self.hero_condition:
            self.hero_condition[hero_name] = HeroCondition()
        return self.hero_condition[hero_name]

condition = Condition()


def add_region_condition_infos(base_condition:Condition, region_name:str) -> Condition:
    '''returns copy with additional values'''
    copied_condition = copy.copy(base_condition)
    copied_condition.region_name = region_name
    return copied_condition

def set_fight_conditions(base_condition:Condition, enemy_count:int) -> Condition:
    copied_condition = copy.copy(base_condition)
    copied_condition.is_fight = True
    copied_condition.enemy_count = enemy_count
    return copied_condition

def get_hero_condition(base_condition:Condition, hero:Hero, is_melee:bool|None=None):
    copied_condition = copy.copy(base_condition)
    if is_melee is not None:
        copied_condition.is_melee = is_melee
    return copied_condition

def set_dice_roll_condition(base_condition:Condition, check_types:list[str] = [], base_skill:LITERAL_BASE_SKILLS|None=None) -> Condition:
    copied_condition = copy.copy(base_condition)
    copied_condition.check_types = check_types
    copied_condition.base_skill = base_skill
    return copied_condition

