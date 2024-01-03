from typing import Literal
from tungeon.config.schema.item import Item
from tungeon.config.schema.region_event import RegionEventStep
from tungeon.console_app import helpers
from tungeon.data.company import Company
from tungeon.data.hero import Hero
from tungeon.logics import config_finder
from tungeon.config.game_config import game_config
import random


LOCATIONS = Literal['melee','ranged','shield','armor','active','backpack']

def perform_steal(company:Company, step:RegionEventStep) -> int | None:
    if step.text:
        print(step.text)
    positions = [i for i in step.hero_positions if step.can_miss or i < len(company.heroes)] if step.hero_positions else list(range(0, len(company.heroes)))
    if not positions:
        return step.no
    position = random.sample(positions, 1)[0]
    available_steal_types = []
    if not step.steal_types:
        return step.no
    hero = company.heroes[position]
    for steal_type in step.steal_types:
        if steal_type == 'money':
            available_steal_types.append(steal_type)
        if steal_type == 'melee':
            if hero.melee_weapon or step.can_miss:
                available_steal_types.append(steal_type)
        if steal_type == 'ranged':
            if hero.ranged_weapon or step.can_miss:
                available_steal_types.append(steal_type)
        if steal_type == 'armor':
            if hero.armor or step.can_miss:
                available_steal_types.append(steal_type)
        if steal_type == 'shield':
            if hero.shield or step.can_miss:
                available_steal_types.append(steal_type)
        if steal_type == 'active':
            if hero.active_items or step.can_miss:
                available_steal_types.append(steal_type)
        if steal_type == 'backpack':
            if hero.backpack_items or step.can_miss:
                available_steal_types.append(steal_type)

    steal_type = random.sample(available_steal_types, 1)[0]
    if steal_type == 'money':
        print(f'All das Gold ({hero.money}) von {hero.name} wurde gestohlen.')
        hero.money = 0
    if steal_type == 'melee':
        if hero.melee_weapon is None:
            print(f'{hero.name} hätte fast seine Nahkampfwaffe verloren, aber er hat gar keine.')
            return step.no
        print(f'{hero.name} hat seine Waffe {config_finder.get_item(hero.melee_weapon).display_name} verloren.')
        hero.melee_weapon = None
    if steal_type == 'ranged':
        if hero.ranged_weapon is None:
            print(f'{hero.name} hätte fast seine Fernkampfwaffe verloren, aber er hat gar keine.')
            return step.no
        print(f'{hero.name} hat seine Waffe {config_finder.get_item(hero.ranged_weapon).display_name} verloren.')
        hero.melee_weapon = None
    if steal_type == 'shield':
        if hero.shield is None:
            print(f'{hero.name} hätte fast seinen Schild verloren, aber er hat gar keine.')
            return step.no
        print(f'{hero.name} hat seinen Schild {config_finder.get_item(hero.shield).display_name} verloren.')
        hero.melee_weapon = None
    if steal_type == 'armor':
        if hero.armor is None:
            print(f'{hero.name} hätte fast seine Rüstung verloren, aber er hat gar keine.')
            return step.no
        print(f'{hero.name} hat seine Rüstung {config_finder.get_item(hero.armor).display_name} verloren.')
        hero.melee_weapon = None
    if steal_type == 'active':
        active_draw = random.randint(0, len(hero.active_items) if not step.can_miss else hero.active_item_slots)
        if active_draw >= len(hero.active_items):
            print(f'{hero.name} hätte fast einen aktiven Gegenstand verloren, aber der Dieb griff daneben.')
            return step.no
        dropped_item_name = hero.active_items.pop(active_draw)
        print(f'{hero.name} hat {config_finder.get_item(dropped_item_name)} aus seinen aktiven Gegenständen verloren.')
    if steal_type == 'backpack':
        if not hero.backpack_items:
            print(f'{hero.name} hat seinen Rucksack verloren, aber er war leer.')
            return step.no
        if step.backpack_parts:
            active_draw = random.randint(0, len(hero.backpack_items))
            if active_draw >= len(hero.backpack_items):
                print(f'{hero.name} hätte fast einen aktiven Gegenstand verloren, aber der Dieb griff daneben.')
                return step.no
            dropped_item_name = hero.backpack_items.pop(active_draw)
            print(f'{hero.name} hat {config_finder.get_item(dropped_item_name)} aus seinen Rucksack verloren.')
        else:
            print(f'{hero.name} hat seinen gesamten Rucksack verloren.')
            print(hero.backpack_str)
            hero.backpack_items = []
    return step.yes



def pay_money(company:Company, amount_to_pay:int) -> bool:
    '''
    Returns:
    - amount is payed: False if company has too few money
    '''
    if sum([hero.money for hero in company.heroes]) < amount_to_pay:
        for hero in company.heroes:
            hero.money = 0
        return False
    amount_payed = 0
    while amount_payed < amount_to_pay:
        hero_name_paying = helpers.select_option('Wer gibt Geld?', [hero.name for hero in company.heroes])
        hero_paying = company.get_hero(hero_name_paying)
        print(f'{hero_paying.name} hat {hero_paying.money} Geld.')
        pay_amount = helpers.get_number_input(f'Wie viel will {hero_paying.name} geben?', hero_paying.money)
        hero_paying.modify_money(-1 * pay_amount)
        amount_payed += pay_amount
    return True

def show_money(hero:Hero):
    print(f'{hero.name}:')
    print(f'Geld: {hero.money}')

def show_inventory(hero:Hero):
    print(f'{hero.name}:')
    print(hero.inventory_str())

def move_item(source_hero:Hero, target_hero:Hero):
    show_inventory(source_hero)
    locations = []
    if source_hero.melee_weapon:
        locations.append('Nahkampfwaffe')
    if source_hero.ranged_weapon:
        locations.append('Fernkampfwaffe')
    if source_hero.shield:
        locations.append('Schild')
    if source_hero.armor:
        locations.append('Ruestung')
    if source_hero.active_items:
        locations.append('Aktive Gegenstände')
    if source_hero.backpack_items:
        locations.append('Gegenstände im Rucksack')
    if not locations:
        print('Keine verfügbaren Gegenstände.')
        return
    
    source_location = helpers.select_option('Von wo möchtest du einen Gegenstand nehmen?', locations)
    if source_location == 'Aktive Gegenstände':
        item_name = helpers.select_option('Welchen Gegenstandd möchtest du bewegen?', source_hero.active_items)
    if source_location == 'Gegenstände im Rucksack':
        item_name = helpers.select_option('Welchen Gegenstandd möchtest du bewegen?', source_hero.backpack_items)


    if source_location == 'Nahkampfwaffe':
        item_name = source_hero.melee_weapon
        source_hero.melee_weapon = None
    if source_location == 'Fernkampfwaffe':
        item_name = source_hero.ranged_weapon
        source_hero.ranged_weapon = None
    if source_location == 'Schild':
        item_name = source_hero.shield
        source_hero.shield = None
    if source_location == 'Ruestung':
        item_name = source_hero.armor
        source_hero.armor = None
    if source_location == 'Aktive Gegenstände':
        source_hero.active_items.remove(item_name)
    if source_location == 'Gegenstände im Rucksack':
        source_hero.backpack_items.remove(item_name)

    item = config_finder.get_item(item_name)




    target_locations = ['Wegwerfen', 'Gegenstände im Rucksack']
    if not target_hero.melee_weapon and item.is_weapon and item.is_melee:
        target_locations.append('Nahkampfwaffe')
    if not target_hero.ranged_weapon and item.is_weapon and item.is_ranged:
        target_locations.append('Fernkampfwaffe')
    if not target_hero.shield and item.is_shield:
        target_locations.append('Schild')
    if not target_hero.armor and item.is_armor:
        target_locations.append('Ruestung')
    if len(target_hero.active_items) < target_hero.active_item_slots and not item.is_armor and not item.is_weapon and not item.is_shield:
        target_locations.append('Aktive Gegenstände')

    target_location = helpers.select_option('Wohin möchtest du den Gegenstand bewegen?', target_locations)
    
    if target_location == 'Wegwerfen':
        return
    if target_location == 'Nahkampfwaffe':
        target_hero.melee_weapon = item_name
    if target_location == 'Fernkampfwaffe':
        target_hero.ranged_weapon = item_name
    if target_location == 'Schild':
        target_hero.shield = item_name
    if target_location == 'Ruestung':
        target_hero.armor = item_name
    if target_location == 'Aktive Gegenstände':
        target_hero.put_item_into_active_items(item_name)
    if target_location == 'Gegenstände im Rucksack':
        target_hero.backpack_items.append(item_name)


def move_company_items(company:Company):
    move = True
    while move:
        for hero in company.heroes:
            show_inventory(hero)
        source_hero_name = helpers.select_option('Von welchem Helden möchtest du einen Gegenstand nehmen?', [hero.name for hero in company.heroes])
        target_hero_name = helpers.select_option('Welchem Helden möchtest du einen Gegenstand geben?', [hero.name for hero in company.heroes])
        source_hero = [hero for hero in company.heroes if hero.name==source_hero_name][0]
        target_hero = [hero for hero in company.heroes if hero.name==target_hero_name][0]
        hero_swapping = True
        while hero_swapping:
            move_item(source_hero, target_hero)
            hero_swapping = helpers.select_yes_no(f'Möchtest du weiter Gegenstände von {source_hero_name} zu {target_hero_name} bewegen?')
        move = helpers.select_yes_no('Möchtest du weitere Gegenstände bewegen?') 

def add_item(company:Company, item_name:str):
    item = config_finder.get_item(item_name)
    hero_name = helpers.select_option(f'Welcher Held soll "{item.display_name}" bekommen?', [hero.name for hero in company.heroes])
    hero = [hero for hero in company.heroes if hero.name==hero_name][0]
    hero.backpack_items.append(item_name)

def move_company_money(company:Company):
    move = True
    while move:
        for hero in company.heroes:
            show_money(hero)
        source_hero_name = helpers.select_option('Von welchem Helden möchtest du einen Gegenstand nehmen?', [hero.name for hero in company.heroes])
        target_hero_name = helpers.select_option('Welchem Helden möchtest du einen Gegenstand geben?', [hero.name for hero in company.heroes])
        source_hero = [hero for hero in company.heroes if hero.name==source_hero_name][0]
        target_hero = [hero for hero in company.heroes if hero.name==target_hero_name][0]
        
        money = helpers.get_number_input('Wie viel Geld soll den Besitzer wechseln?', source_hero.money)
        source_hero.money -= money
        target_hero.money += money
        move = helpers.select_yes_no('Möchtest du weiteres Geld bewegen?') 

def add_money(company:Company, money_value:int):
    hero_name = helpers.select_option(f'Welcher Held soll die {money_value} Geld bekommen?', [hero.name for hero in company.heroes])
    hero = [hero for hero in company.heroes if hero.name==hero_name][0]
    hero.money += money_value

def buy_item(hero:Hero, available_item_names:list[str]):
    available_items = [item for item in game_config.items if item.name in available_item_names]
    def get_shop_entry(item:Item) -> str:
        return f'{item.name} ({item.money_value})'
    too_expensive_items = [item for item in available_items if item.money_value > hero.money]
    actual_available_items = [item for item in available_items if item.money_value <= hero.money]
    print('Folgende Gegenstände sind leider zu teuer für dich:')
    for item in too_expensive_items:
        print(get_shop_entry(item))
    shop_entry_to_buy = helpers.select_option('Welchen Gegenstand möchtest du kaufen?', [
        get_shop_entry(item) for item in actual_available_items
    ] + ['Nichts'])
    if shop_entry_to_buy == 'Nichts':
        return
    item_to_buy = [item for item in actual_available_items if get_shop_entry(item) == shop_entry_to_buy][0]
    hero.modify_money(-1 * item_to_buy.money_value)
    hero.backpack_items.append(item_to_buy.name)
    print(f'{hero.name} hat jetzt {item_to_buy.name} im Rucksack')

def sell_item(hero:Hero):
    items = []
    active_postfix = ' (active)'
    backpack_postfix = ' (Rucksack)'
    if hero.active_items:
        items += [f'{item}{active_postfix}' for item in hero.active_items]
    if hero.backpack_items:
        items += [f'{item}{backpack_postfix}' for item in hero.backpack_items]
    if not items:
        print('Es gibt nichts zu verkaufen. Nur Gegenstände in Rucksack und aktiven Gegenständen können verkauft werden.')
        return
    selected_item = helpers.select_option('Welchen Gegenstand möchtest du verkaufen?', items)
    if backpack_postfix in selected_item:
        item = config_finder.get_item(selected_item.strip(backpack_postfix))
        hero.backpack_items.remove(item.name)
        hero.money += item.money_value / 2
    if active_postfix in selected_item:
        item = config_finder.get_item(selected_item.strip(active_postfix))
        hero.active_items.remove(item.name)
        hero.money += item.money_value / 2
