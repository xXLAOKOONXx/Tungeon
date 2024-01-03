import random
from tungeon.config.schema.region import Region
from tungeon.config.schema.skill import Skill
from tungeon.console_app import helpers
from tungeon.config.game_config import game_config
from tungeon.console_app import inventory_dialog, event_dialog
from tungeon.data.company import Company
from tungeon.data.condition import HeroCondition, condition
from tungeon.data.hero import Hero
from tungeon.logics import hero_actions, learningsystem, config_finder, functionality_system, hero_status

def perform_use_prep_skills(company:Company):
    selected_hero_name = helpers.select_option('Welcher Held soll eine Fähigkeit einsetzen?', [hero.name for hero in company.heroes])
    hero = company.get_hero(selected_hero_name)
    skills = [config_finder.get_skill(skill_name) for skill_name in hero.skills]
    prep_skills = [skill for skill in skills if any(functionality_system.check_conditions_met(func, hero) for func in skill.functions)]
    selected_skill_name = helpers.select_option('Welche Faehigkeit möchtest du einsetzen?', ['Keine'] + [s.display_name for s in prep_skills])
    if selected_skill_name == 'Keine':
        return
    selected_skill = [s for s in prep_skills if s.display_name == selected_skill_name][0]
    funcs = [f for f in selected_skill.functions if f.condition_type == 'round-preperation']
    for func in funcs:
        target_hero = hero
        if func.other_hero_allowed:
            target_hero = company.get_hero(helpers.select_option('Auf welchen Helden möchtest du die Fähigkeit anwenden?',[h.name for h in company.heroes]))
        hero_actions.apply_prepare_functionality(hero, target_hero, func)
        if hero.name not in condition.hero_condition.keys():
            condition.hero_condition[hero.name] = HeroCondition()
        condition.get_hero_condition(hero.name).used_skills.append(selected_skill.name)
        condition.get_hero_condition(hero.name).used_skill_groups += func.function_groups

def perform_preperation(company):
    condition.is_prep = True
    while helpers.select_yes_no(game_config.language_package.wanna_prep):
        selection = helpers.select_option('was wilse tun?', ['Items tauschen', 'nuex', 'Fähigkeiten einsetzen'])
        if selection == 'Items tauschen':
            inventory_dialog.move_company_items(company)
        if selection == 'Fähigkeiten einsetzen':
            perform_use_prep_skills(company)
    condition.is_prep = False

def perform_shopping(hero:Hero, region:Region):
    continue_shopping = True
    while continue_shopping:
        if helpers.select_yes_no('Verkaufen?'):
            inventory_dialog.sell_item(hero)
        if helpers.select_yes_no('Kaufen?'):
            inventory_dialog.buy_item(hero, region.shop_items)
        continue_shopping = helpers.select_yes_no('Weiter einkaufen?')

def perform_base_skill_learning(company:Company, hero:Hero):
    strength_cost = learningsystem.get_strength_cost(hero)
    speed_cost = learningsystem.get_speed_cost(hero)
    agility_cost = learningsystem.get_agility_cost(hero)
    intelligence_cost = learningsystem.get_intelligence_cost(hero)
    options = ['Keine']
    if strength_cost > company.improvement_points:
        print(f'Für Stärke fehlen die Steigerungspunkte, du hast {company.improvement_points}, du brauchst {strength_cost}')
    if strength_cost is not None:
        if strength_cost > company.improvement_points:
            print(f'Für Stärke fehlen die Steigerungspunkte, du hast {company.improvement_points}, du brauchst {strength_cost}')
        else:
            options.append(f'Stärke ({strength_cost})')
    if speed_cost is not None:
        if speed_cost > company.improvement_points:
            print(f'Für Schnelligkeit fehlen die Steigerungspunkte, du hast {company.improvement_points}, du brauchst {speed_cost}')
        else:
            options.append(f'Geschwindigkeit ({speed_cost})')
    if agility_cost is not None:
        if agility_cost > company.improvement_points:
            print(f'Für Agilität fehlen die Steigerungspunkte, du hast {company.improvement_points}, du brauchst {agility_cost}')
        else:
            options.append(f'Agilität ({agility_cost})')
    if intelligence_cost is not None:
        if intelligence_cost > company.improvement_points:
            print(f'Für Intelligenz fehlen die Steigerungspunkte, du hast {company.improvement_points}, du brauchst {intelligence_cost}')
        else:
            options.append(f'Intelligenz ({intelligence_cost})')
    selected_option = helpers.select_option('Welche Eigenschaft möchtest du stärken?', options)
    if selected_option == 'Keine':
        return
    if 'Stärke' in selected_option:
        hero.strength += 1
        company.use_improvement_points(strength_cost)
    if 'Schnelligkeit' in selected_option:
        hero.speed += 1
        company.use_improvement_points(speed_cost)
    if 'Agilität' in selected_option:
        hero.agility += 1
        company.use_improvement_points(agility_cost)
    if 'Intelligenz' in selected_option:
        hero.intelligence += 1
        company.use_improvement_points(intelligence_cost)

def perform_teacher_learning(company:Company, hero:Hero, learnable_skill_names:list[str]):
    hero_profession = config_finder.get_profession(hero.profession)
    avilable_learning_skills = learnable_skill_names
    available_skills = learningsystem.get_learnable_skills(hero, avilable_learning_skills)
    def has_enough(skill:Skill, max_money, max_points, is_doubled=False):
        factor = 1
        if is_doubled:
            factor = 2
        return skill.learning_cost_money * factor <= max_money and skill.learning_cost_improvement_points * factor <= max_points
    too_expensive_skills = [skill for skill in available_skills if not has_enough(skill, hero.money, company.improvement_points, skill.name in hero_profession.double_price_skills)]
    actual_available_skills = [skill for skill in available_skills if has_enough(skill, hero.money, company.improvement_points, skill.name in hero_profession.double_price_skills)]
    
    def shop_entry(skill:Skill, is_double:bool):
        factor = 1 if not is_double else 2
        return f'{skill.display_name} ({skill.learning_cost_improvement_points * factor} Steigerungspunkte, {skill.learning_cost_money * factor} Geld)'
    
    if too_expensive_skills:
        print('Leider reichen Geld und Steigerungspunkte nicht für folgende Fähigkeiten:')
        for skill in too_expensive_skills:
            print(shop_entry(skill, skill.name in hero_profession.double_price_skills))
    if not available_skills:
        print('Hier scheint es nichts zu lernen zu geben.')
        return
    selected_skill = helpers.select_option('Welche Faehigkeit soll es werden?', ['Keine'] + [shop_entry(skill, skill.name in hero_profession.double_price_skills) for skill in actual_available_skills])
    if selected_skill == 'Keine':
        
        return
    selected_skill = [skill for skill in actual_available_skills if shop_entry(skill, skill.name in hero_profession.double_price_skills) == selected_skill][0]
    factor = 1
    if selected_skill.name in hero_profession.double_price_skills:
        factor = 2
    hero.modify_money(-1 * factor * selected_skill.learning_cost_money)
    company.use_improvement_points(factor * selected_skill.learning_cost_improvement_points)
    hero.skills.append(selected_skill.name)
    for skill_name in selected_skill.learning_removes_skills:
        hero.skills.remove(skill_name)
    print(f'{hero.name} kann jetzt "{selected_skill.display_name}"')

def perform_learning(company:Company, hero:Hero, region:Region):
    learning_type = helpers.select_option('Was wollt ihr tun?', ['Lehrmeister suchen', 'Selbst weiterbilden'])
    if learning_type == 'Lehrmeister suchen':
        perform_teacher_learning(company, hero, learnable_skill_names=region.trainable_skills)
    if learning_type == 'Selbst weiterbilden':
        perform_base_skill_learning(company, hero)


def perform_camping(company:Company):
    region = config_finder.get_region(company.current_region)
    busy_heroes:list[str] = []
    if not region.free_camping:
        busy_heroes += helpers.select_option('Wer schlägts lager uf?', [hero.name for hero in company.heroes if hero_actions.is_effected_by_wound(hero) and region.name in hero.origin_regions])
    while len(busy_heroes) != len(company.heroes):
        next_hero_name = helpers.select_option('Wen möchtest du als nächstes zuteilen?',
                                          [hero.name for hero in company.heroes if hero.name not in busy_heroes])
        busy_heroes.append(next_hero_name)
        action_options = ['Nichts', 'Handeln', 'Heilen', 'Lernen']
        action = helpers.select_option(f'Was soll {next_hero_name} machen?', action_options)
        if action == 'Nichts':
            continue
        if action == 'Handeln':
            perform_shopping(company.get_hero(next_hero_name), region)
        if action == 'Heilen':
            company.get_hero(next_hero_name).wounds -= 1
        if action == 'Lernen':
            perform_learning(company, company.get_hero(next_hero_name), region)

def search_current_region(company:Company):
    region = [region for region in game_config.regions if region.name == company.current_region][0]
    event_roll = random.randint(1,100)
    region_event = [e for e in region.events if event_roll in e.values][0]
    event_dialog.perform_event(company, region_event, region.name)

def perform_region_activity(company:Company):
    region = config_finder.get_region(company.current_region)
    print(f'''Du bist in {region.display_name} und hast als angrenzende Gebiete: {', '.join([config_finder.get_region(r).display_name for r in region.available_regions])}''')
    
    options = ['aktuelles gebiet durchsuchen']
    if region.free_camping or any(region.name in hero.origin_regions and hero_actions.hero_is_able_to_act(hero) for hero in company.heroes):
        options.append('lagern')
    if region.available_regions:
        options.append('gebiet wechseln')
    selection = helpers.select_option('Wat wilse mache?',options)
    if selection == 'lagern':
        perform_camping(company)
    elif selection == 'gebiet wechseln':
        region_selection = helpers.select_option('',region.available_regions)
        company.current_region = region_selection
        search_current_region(company)
    elif selection == 'aktuelles gebiet durchsuchen':
        search_current_region(company)
    condition.hero_condition = {}
    helpers.wait_enter('Deine Runde ist vorbei.')
    dieing_heroes = [hero.name for hero in company.heroes if hero_status.should_die(hero)]
    for hero_name in dieing_heroes:
        idx = [i for i, h in enumerate(company.heroes) if h.name == hero_name][0]
        print(f'{hero_name} ist leider an seinen Verletzungen erlegen.')
        company.heroes.pop(idx)