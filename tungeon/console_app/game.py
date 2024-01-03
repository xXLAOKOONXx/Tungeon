from typing import Tuple
from tungeon.console_app.round_dialog import perform_preperation, perform_region_activity
from tungeon.data.company import Company
from tungeon.console_app import helpers
from tungeon.data.hero import Hero
from tungeon.logics import storage_logics, config_finder, hero_builder
from tungeon.config.game_config import game_config, set_game_config

HERO_COUNT = 4

def create_hero() -> Hero:
    hero_name = input(game_config.language_package.hero_name_question)
    hero_race_name = helpers.select_option(game_config.language_package.hero_race_question, [race.name for race in game_config.races])
    hero_race = config_finder.get_race(hero_race_name)
    hero_profession_name = helpers.select_option(game_config.language_package.hero_profession_question, [profession.name for profession in game_config.professions])
    hero_profession = config_finder.get_profession(hero_profession_name)

    return hero_builder.build_hero(hero_name, hero_race, hero_profession)

def create_company() -> Tuple[Company, str]:
    company_name = input(game_config.language_package.company_name_question)
    print(game_config.language_package.define_four_heros)
    heroes = []
    for i in range (1, 5):
        print(game_config.language_package.define_hero_number.format(number=i))
        hero = create_hero()
        print(hero)
        heroes.append(hero)

    starter_region = game_config.regions[0]
    print(game_config.language_package.company_start_at(region_name=starter_region.display_name))

    c = Company(
        name=company_name,
        heroes=heroes,
        current_region=starter_region.name
        )

    save_location = helpers.new_file_dialog(game_config.language_package.company_save_question)
    storage_logics.save(c, save_location)
    return c, save_location

def play_rounds(company:Company, save_path:str):
    while True:
        print(str(company))
        if len(company.heroes) < HERO_COUNT:
            if helpers.select_yes_no(game_config.language_package.add_hero):
                hero = create_hero()
                company.heroes.append(hero)
        perform_preperation(company)
        perform_region_activity(company)
        storage_logics.save(company, save_path)

def get_game_config():
    game_config_path = helpers.folder_dialog(game_config.language_package.select_world_settings)
    set_game_config(game_config_path)

def get_company() -> Tuple[Company, str]:
    company_type = helpers.select_option(game_config.language_package.select_company, [game_config.language_package.new_company, game_config.language_package.existing_company])
    if company_type == game_config.language_package.new_company:
        return create_company()
    if company_type == game_config.language_package.existing_company:
        company_filepath = helpers.file_dialog(game_config.language_package.select_company_file)
        company = storage_logics.load(company_filepath)
        print(f'{game_config.language_package.you_selected} {company.name} ({company_filepath})')
        return company, company_filepath
    
def start_game():
    get_game_config()
    company, save_location = get_company()
    play_rounds(company, save_location)

if __name__ == '__main__':
    helpers.set_ui_callables()
    start_game()