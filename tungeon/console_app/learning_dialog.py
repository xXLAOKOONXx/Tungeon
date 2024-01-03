
from tungeon.config.schema.skill import Skill
from tungeon.data.company import Company
from tungeon.data.hero import Hero
from tungeon.logics import hero_actions, learningsystem, config_finder, functionality_system
from tungeon.console_app import helpers
from tungeon.config.schema.region_event import LearnSkill

def _has_enough(skill:LearnSkill, max_money, max_points, is_doubled=False):
    factor = 1
    if is_doubled:
        factor = 2
    return skill.money * factor <= max_money and skill.points * factor <= max_points
def _shop_entry(skill:LearnSkill, is_double:bool):
    factor = 1 if not is_double else 2
    return f'{config_finder.get_skill(skill.skill_name).display_name} ({skill.points * factor} Steigerungspunkte, {skill.money * factor} Geld)'
 

def perform_teacher_learning(company:Company, hero:Hero, learnable_skills:list[LearnSkill]) -> bool:
    '''
    Returns
    - skill learned
    '''
    lbs = learningsystem.get_learnable_skills(hero, [s.skill_name for s in learnable_skills])
    learnable_skills = [ls for ls in learnable_skills if any([s.name == ls.skill_name for s in lbs])]
    hero_profession = config_finder.get_profession(hero.profession)
    too_expensive_skills = [skill for skill in learnable_skills if not _has_enough(skill, hero.money, company.improvement_points, skill.skill_name in hero_profession.double_price_skills)]
    actual_available_skills = [skill for skill in learnable_skills if _has_enough(skill, hero.money, company.improvement_points, skill.skill_name in hero_profession.double_price_skills)]
    
   
    if too_expensive_skills:
        print('Leider reichen Geld und Steigerungspunkte nicht für folgende Fähigkeiten:')
        for skill in too_expensive_skills:
            print(_shop_entry(skill, skill.skill_name in hero_profession.double_price_skills))
    if not actual_available_skills:
        print('Hier scheint es nichts zu lernen zu geben.')
        return False
    selected_skill = helpers.select_option('Welche Faehigkeit soll es werden?', ['Keine'] + [_shop_entry(skill, skill.skill_name in hero_profession.double_price_skills) for skill in actual_available_skills])
    if selected_skill == 'Keine':
        return False
    selected_skill = [skill for skill in actual_available_skills if _shop_entry(skill, skill.name in hero_profession.double_price_skills) == selected_skill][0]
    factor = 1
    if selected_skill.skill_name in hero_profession.double_price_skills:
        factor = 2
    hero.modify_money(-1 * factor * selected_skill.money)
    company.use_improvement_points(factor * selected_skill.points)
    hero.skills.append(selected_skill.skill_name)
    for skill_name in config_finder.get_skill(selected_skill.skill_name).learning_removes_skills:
        hero.skills.remove(skill_name)
        print(f'{hero.name} kann nicht länger {config_finder.get_skill(skill_name).display_name}')
    print(f'{hero.name} kann jetzt "{config_finder.get_skill(selected_skill.skill_name).display_name}"')
    return True
