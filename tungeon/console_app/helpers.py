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
    i = input(text)
    try:
        i = int(i)
    except Exception:
        print('Gib eine Zahl an, versuche es noch einmal.')
        return get_number_input(text, max_value)
    if max_value and i > max_value:
        print(f'Eingabe zu hoch, maximaler Wert ist {max_value}, versuche es noch einmal.')
        return get_number_input(text, max_value)
    if i < 0:
        print('Gib einen positiven Wert an, versuche es noch einmal.')
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
            user_input = int(input(f'{game_config.language_package.select}: '))
            if user_input < 0 or user_input >= len(options):
                raise ValueError('User input not in offered range')
            return options[user_input]
        except Exception:
            print(game_config.language_package.faulty_input)
    return select_option

def select_yes_no(text:str|None) -> bool:
    '''
    Returns:
    - flag(bool): True if Yes selected
    '''
    return select_option(text, [game_config.language_package.yes, game_config.language_package.no]) == game_config.language_package.yes

def file_dialog(text:str) -> str:
    return filedialog.askopenfilename(defaultextension='json', filetypes=[('json', '.json')], title=text, initialdir='./')

def folder_dialog(text:str) -> str:
    return filedialog.askdirectory(initialdir='./')

def new_file_dialog(text:str) -> str:
    return filedialog.asksaveasfilename(initialdir='./', filetypes=[('json', '.json')], title=text, defaultextension='json')

def roll_hero_dice(hero:Hero, check_types:list[str], region_name:str) -> int:
    dice_roll = random.randint(1,6)
    print(f'Der Wurf von {hero.name} ist eine {dice_roll}')

    # check for amulets
    functionable_items, destruction = item_effects.get_functionable_items_for_check(hero, check_types, region_name)
    if functionable_items:
        options = ['Nein']
        def get_option(i:Item,d:bool):
            return f'''{i.display_name}{' (zerstört sich bei Benutzung)' if d else ''}'''
        for func, des in zip(functionable_items, destruction):
            options.append(get_option(func, des))
        item_selection = select_option('Möchtest du deinen Gegenstand einsetzen, um den Würfel neu zu würfeln?',
                              options)
        if item_selection != 'Nein':
            for item, des in zip(functionable_items, destruction):
                if item_selection == get_option(item, des):
                    selected_item = item
                    destroy_item = des
                    break            
            dice_roll = random.randint(1,6)
            print(f'Der neue Wurf ist eine {dice_roll}')
            if destroy_item:
                hero.active_items.remove(selected_item.name)
                print(f'Du hast {selected_item.display_name} verloren.')
    return dice_roll

def roll_skillcheck(hero:Hero) -> bool:
    if condition.base_skill == 'strength':
        skill_name = 'Stärke'
        skill_value = hero.current_strength
    if condition.base_skill == 'speed':
        skill_name = 'Schnelligkeit'
        skill_value = hero.current_speed
    if condition.base_skill == 'agility':
        skill_name = 'Agilität'
        skill_value = hero.current_agility
    if condition.base_skill == 'intelligence':
        skill_name = 'Intelligenz'
        skill_value = hero.current_intelligence
    print(f'Du brauchst einen check für {skill_name} ({skill_value})')
    dice_roll = random.randint(1,6)
    print(f'Der Wurf von {hero.name} ist eine {dice_roll}')

    # check for amulets
    functionable_items, destruction = item_effects.get_functionable_items_for_check(hero, condition.check_types, condition.region_name)
    if functionable_items:
        options = ['Nein']
        def get_option(i:Item,d:bool):
            return f'''{i.display_name}{' (zerstört sich bei Benutzung)' if d else ''}'''
        for func, des in zip(functionable_items, destruction):
            options.append(get_option(func, des))
        item_selection = select_option('Möchtest du deinen Gegenstand einsetzen, um den Würfel neu zu würfeln?',
                              options)
        if item_selection != 'Nein':
            for item, des in zip(functionable_items, destruction):
                if item_selection == get_option(item, des):
                    selected_item = item
                    destroy_item = des
                    break            
            dice_roll = random.randint(1,6)
            print(f'Der neue Wurf ist eine {dice_roll}')
            if destroy_item:
                hero.active_items.remove(selected_item.name)
                print(f'Du hast {selected_item.display_name} verloren.')
    
    return dice_roll < skill_value

def use_destroyable_item_dialog(hero:Hero, item:Item) -> bool:
    return select_yes_no(f'Möchtest du {item.display_name} von {hero.name} einsetzen? (Die Benutzung zerstört den Gegenstand)')

def functionality_used_dialog(func:Functionality):
    print(f'{func.display_name} wurde angewendet.')

def set_ui_callables():
    ui_connection.set_skillcheck_dialog(roll_skillcheck)
    ui_connection.set_use_destroyable_item_dialog(use_destroyable_item_dialog)
    ui_connection.set_functionality_used_dialog(functionality_used_dialog)