import random
from tkinter import filedialog
from tungeon.config.game_config import game_config
from tungeon.config.schema.functionality import Functionality
from tungeon.config.schema.item import Item
from tungeon.data.condition import condition
from tungeon.data.hero import Hero
from tungeon.logics import config_finder, item_effects
from tungeon.logics import ui_connection

def wait_enter(text:str):
    input(text)

def write_to_console(text:str):
    print(text)

def get_number_input(text:str, max_value:int|None=None) -> int:
    i = input(f'{text} ')
    try:
        i = int(i)
    except Exception:
        print(game_config().language_package.enter_number_error)
        return get_number_input(text, max_value)
    if max_value and i > max_value:
        print(game_config().language_package.enter_number_max_error.format(max=max_value))
        return get_number_input(text, max_value)
    if i < 0:
        print(game_config().language_package.enter_number_pos_error)
        return get_number_input(text, max_value)
    return i

def select_option(text:str|None, options:list[str]) -> str:
    '''
    Returns:
    - selected option(str)
    '''
    if not options:
        raise ValueError('Not enough options')
    if text:
        print(text)
    for idx, option in enumerate(options):
        print(f'[{idx}] {option}')
    selected_option = None
    while selected_option is None:
        try:
            user_input = int(input(f'{game_config().language_package.select}: '))
            if user_input < 0 or user_input >= len(options):
                raise ValueError(game_config().language_package.select_out_of_range)
            return options[user_input]
        except Exception:
            print(game_config().language_package.faulty_input)
    return select_option

def select_yes_no(text:str|None) -> bool:
    '''
    Returns:
    - flag(bool): True if Yes selected
    '''
    return select_option(text, [game_config().language_package.yes, game_config().language_package.no]) == game_config().language_package.yes

def file_dialog(text:str) -> str:
    return filedialog.askopenfilename(defaultextension='json', filetypes=[('json', '.json')], title=text, initialdir='./')

def folder_dialog(text:str) -> str:
    return filedialog.askdirectory(initialdir='./', title=text)

def new_file_dialog(text:str) -> str:
    return filedialog.asksaveasfilename(initialdir='./', filetypes=[('json', '.json')], title=text, defaultextension='json')

def roll_hero_dice(hero:Hero, check_types:list[str], region_name:str) -> int:
    dice_roll = random.randint(1,6)
    print(game_config().language_package.hero_dice_roll.format(hero_name=hero.name, dice_roll=dice_roll))

    # check for amulets
    functionable_items, destruction = item_effects.get_functionable_items_for_check(hero, check_types, region_name)
    if functionable_items:
        options = [game_config().language_package.no]
        def get_option(i:Item,d:bool):
            return f'''{i.display_name}{f' ({game_config().language_package.item_gets_destroyed})' if d else ''}'''
        for func, des in zip(functionable_items, destruction):
            options.append(get_option(func, des))
        item_selection = select_option(game_config().language_package.use_item_for_roll, options)
        if item_selection != game_config().language_package.no:
            for item, des in zip(functionable_items, destruction):
                if item_selection == get_option(item, des):
                    selected_item = item
                    destroy_item = des
                    break            
            dice_roll = random.randint(1,6)
            print(game_config().language_package.new_roll.format(dice_roll=dice_roll))
            if destroy_item:
                hero.active_items.remove(selected_item.name)
                print(game_config().language_package.lost_item.format(item_name=selected_item.display_name))
    return dice_roll

def roll_skillcheck(hero:Hero) -> bool:
    if condition.base_skill == 'strength':
        skill_name = game_config().language_package.strength
        skill_value = hero.current_strength
    if condition.base_skill == 'speed':
        skill_name = game_config().language_package.speed
        skill_value = hero.current_speed
    if condition.base_skill == 'agility':
        skill_name = game_config().language_package.agility
        skill_value = hero.current_agility
    if condition.base_skill == 'intelligence':
        skill_name = game_config().language_package.intelligence
        skill_value = hero.current_intelligence
    print(game_config().language_package.req_check.format(skill_name=skill_name, skill_value=skill_value))
    dice_roll = random.randint(1,6)
    print(game_config().language_package.hero_dice_roll.format(hero_name=hero.name, dice_roll=dice_roll))

    # check for amulets
    functionable_items, destruction = item_effects.get_functionable_items_for_check(hero, condition.check_types, condition.region_name)
    if functionable_items:
        options = [game_config().language_package.no]
        def get_option(i:Item,d:bool):
            return f'''{i.display_name}{f' ({game_config().language_package.item_gets_destroyed})' if d else ''}'''
        for func, des in zip(functionable_items, destruction):
            options.append(get_option(func, des))
        item_selection = select_option(game_config().language_package.use_item_for_roll,
                              options)
        if item_selection != game_config().language_package.no:
            for item, des in zip(functionable_items, destruction):
                if item_selection == get_option(item, des):
                    selected_item = item
                    destroy_item = des
                    break            
            dice_roll = random.randint(1,6)
            print(game_config().language_package.new_roll.format(dice_roll=dice_roll))
            if destroy_item:
                hero.active_items.remove(selected_item.name)
                print(game_config().language_package.lost_item.format(item_name=selected_item.display_name))
    
    return dice_roll < skill_value

def use_destroyable_item_dialog(hero:Hero, item:Item) -> bool:
    return select_yes_no(game_config().language_package.wanna_use_destr_item.format(item_name=item.display_name, hero_name=hero.name))

def functionality_used_dialog(func:Functionality):
    print(game_config().language_package.func_used.format(func_name=func.display_name))

def set_ui_callables():
    ui_connection.set_skillcheck_dialog(roll_skillcheck)
    ui_connection.set_use_destroyable_item_dialog(use_destroyable_item_dialog)
    ui_connection.set_functionality_used_dialog(functionality_used_dialog)