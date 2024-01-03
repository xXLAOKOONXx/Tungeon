from tungeon.config.game_config import game_config
from tungeon.config.schema.item import Item
from tungeon.config.schema.profession import Profession
from tungeon.config.schema.race import Race
from tungeon.config.schema.region import Region
from tungeon.config.schema.skill import Skill


def get_skill(skill_name:str) -> Skill:
    for skill in game_config().skills:
        if skill.name == skill_name:
            return skill
    raise ValueError(f'Skill {skill_name} not found')

def get_profession(profession_name:str) -> Profession:
    for profession in game_config().professions:
        if profession.name == profession_name:
            return profession
    raise ValueError(f'Profession {profession_name} not found')

def get_race(race_name:str) -> Race:
    for race in game_config().races:
        if race.name == race_name:
            return race
    raise ValueError(f'Race {race_name} not found')


def get_region(region_name:str) -> Region:
    for region in game_config().regions:
        if region.name == region_name:
            return region
    raise ValueError(f'Region {region_name} not found')


def get_item(item_name:str) -> Item:
    for item in game_config().items:
        if item.name == item_name:
            return item
    raise ValueError(f'Item {item_name} not found')
