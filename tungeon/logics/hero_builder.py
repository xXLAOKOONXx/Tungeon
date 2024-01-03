

import random
from tungeon.config.schema.profession import Profession, StarterSkill
from tungeon.config.schema.race import Race
from tungeon.data.hero import Hero


def get_starting_skills(profession:Profession) -> list[str]:
    def get_starter_skill(starter_skill:StarterSkill) -> list[str]:
        if not starter_skill.is_roll:
            return [starter_skill.skill_name]
        return random.sample(starter_skill.roll_results, 1)[0]
    skills = []
    for starter_skill in profession.starter_skills:
        skills += get_starter_skill(starter_skill)
    return skills

def build_hero(name:str, race:Race, profession:Profession):
    skills = get_starting_skills(profession)
    return Hero(
               name=name,
               race=race.name,
               profession=profession.name,
               speed=race.speed_base,
               strength=race.strength_base,
               agility=race.agility_base,
               intelligence=race.intelligence_base,
               backpack_items=profession.starter_items,
               money=profession.starter_money,
               skills=skills,
               origin_regions=race.origin_regions
            )