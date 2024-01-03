

from tungeon.config.schema.skill import Skill
from tungeon.data.hero import Hero
from tungeon.logics import config_finder



def get_learnable_skills(hero:Hero, available_skill_names:list[str]) -> list[Skill]:
    available_skills = [config_finder.get_skill(skill_name) for skill_name in available_skill_names]
    hero_skills = [config_finder.get_skill(skill_name) for skill_name in hero.skills]
    hero_profession = config_finder.get_profession(hero.profession)
    profession_skills = hero_profession.available_skills + hero_profession.double_price_skills
    # eliminate by profession
    available_skills = [skill for skill in available_skills if skill.name in profession_skills]
    # eliminate by skill-prevention
    prevented_skills:list[str] = []
    for skill in hero_skills:
        prevented_skills += skill.other_skill_prevention
    available_skills = [skill for skill in available_skills if skill.name not in prevented_skills]
    # eliminate by required skills
    available_skills = [skill for skill in available_skills if all([req_skill in hero.skills for req_skill in skill.learning_required_skills])]
    return available_skills

def get_strength_cost(hero) -> int | None:
    '''
    returns upgrade costs for strength
    '''
    target_strength = hero.strength + 1
    race = config_finder.get_race(hero.race)
    if target_strength not in race.strength_upgrades.keys():
        return None
    return race.strength_upgrades[target_strength]

def get_speed_cost(hero) -> int | None:
    '''
    returns upgrade costs for speed
    '''
    target_speed = hero.speed + 1
    race = config_finder.get_race(hero.race)
    if target_speed not in race.speed_upgrades.keys():
        return None
    return race.speed_upgrades[target_speed]

def get_agility_cost(hero) -> int | None:
    '''
    returns upgrade costs for agility
    '''
    target_agility = hero.agility + 1
    race = config_finder.get_race(hero.race)
    if target_agility not in race.agility_upgrades.keys():
        return None
    return race.agility_upgrades[target_agility]

def get_intelligence_cost(hero) -> int | None:
    '''
    returns upgrade costs for strength
    '''
    target_intelligence = hero.intelligence + 1
    race = config_finder.get_race(hero.race)
    if target_intelligence not in race.intelligence_upgrades.keys():
        return None
    return race.intelligence_upgrades[target_intelligence]

