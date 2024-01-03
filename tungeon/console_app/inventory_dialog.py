from typing import Literal
from tungeon.config.schema.item import Item
from tungeon.config.schema.region_event import RegionEventStep
from tungeon.console_app import helpers
from tungeon.data.company import Company
from tungeon.data.hero import Hero
from tungeon.logics import config_finder
from tungeon.config.game_config import game_config
import random


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
        print(game_config.language_package.lost_money.format(money=hero.money, hero_name=hero.name))
        hero.money = 0
    if steal_type == 'melee':
        if hero.melee_weapon is None:
            game_config.language_package.lost_almost_melee.format(hero_name=hero.name)
            return step.no
        print(game_config.language_package.lost_melee.format(hero_name=hero.name, item_name=config_finder.get_item(hero.melee_weapon).display_name))
        hero.melee_weapon = None
    if steal_type == 'ranged':
        if hero.ranged_weapon is None:
            game_config.language_package.lost_almost_ranged.format(hero_name=hero.name)
            return step.no
        print(game_config.language_package.lost_ranged.format(hero_name=hero.name, item_name=config_finder.get_item(hero.ranged_weapon).display_name))
        hero.ranged_weapon = None
    if steal_type == 'shield':
        if hero.shield is None:
            game_config.language_package.lost_almost_shield.format(hero_name=hero.name)
            return step.no
        print(game_config.language_package.lost_shield.format(hero_name=hero.name, item_name=config_finder.get_item(hero.shield).display_name))
        hero.shield = None
    if steal_type == 'armor':
        if hero.armor is None:
            game_config.language_package.lost_almost_armor.format(hero_name=hero.name)
            return step.no
        print(game_config.language_package.lost_armor.format(hero_name=hero.name, item_name=config_finder.get_item(hero.armor).display_name))
        hero.armor = None
    if steal_type == 'active':
        active_draw = random.randint(0, len(hero.active_items) if not step.can_miss else hero.active_item_slots)
        if active_draw >= len(hero.active_items):
            game_config.language_package.lost_almost_active_item.format(hero_name=hero.name)
            return step.no
        dropped_item_name = hero.active_items.pop(active_draw)
        print(game_config.language_package.lost_active_item.format(hero_name=hero.name, item_name=config_finder.get_item(dropped_item_name).display_name))
    if steal_type == 'backpack':
        if not hero.backpack_items:
            game_config.language_package.lost_empty_backpack.format(hero_name=hero.name)
            return step.no
        if step.backpack_parts:
            active_draw = random.randint(0, len(hero.backpack_items))
            if active_draw >= len(hero.backpack_items):
                print(game_config.language_package.lost_backpack_item.format(hero_name=hero.name, item_name=config_finder.get_item(hero.armor).display_name))
                return step.no
            dropped_item_name = hero.backpack_items.pop(active_draw)
            print(game_config.language_package.lost_backpack_item.format(hero_name=hero.name, item_name=config_finder.get_item(dropped_item_name)))
        else:
            print(game_config.language_package.lost_backpack.format(hero_name=hero.name))
            print(hero.backpack_str())
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
        hero_name_paying = helpers.select_option(game_config.language_package.who_gives_money, [hero.name for hero in company.heroes])
        hero_paying = company.get_hero(hero_name_paying)
        print(game_config.language_package.hero_money.format(hero_name=hero_paying.name, money=hero_paying.money))
        pay_amount = helpers.get_number_input(game_config.language_package.how_much_gives.format(hero_name=hero_paying.name), hero_paying.money)
        hero_paying.modify_money(-1 * pay_amount)
        amount_payed += pay_amount
    return True

def show_money(hero:Hero):
    print(f'{hero.name}:')
    print(f'{game_config.language_package.money}: {hero.money}')

def show_inventory(hero:Hero):
    print(f'{hero.name}:')
    print(hero.inventory_str())

def move_item(source_hero:Hero, target_hero:Hero):
    show_inventory(source_hero)
    locations = []
    if source_hero.melee_weapon:
        locations.append(game_config.language_package.melee)
    if source_hero.ranged_weapon:
        locations.append(game_config.language_package.ranged)
    if source_hero.shield:
        locations.append(game_config.language_package.shield)
    if source_hero.armor:
        locations.append(game_config.language_package.armor)
    if source_hero.active_items:
        locations.append(game_config.language_package.active_items)
    if source_hero.backpack_items:
        locations.append(game_config.language_package.backpack_items)
    if not locations:
        print(game_config.language_package.no_item_locations)
        return
    
    source_location = helpers.select_option(game_config.language_package.item_source, locations)
    if source_location == game_config.language_package.active_items:
        item_name = helpers.select_option(game_config.language_package.which_item_move, source_hero.active_items)
    if source_location == game_config.language_package.backpack_items:
        item_name = helpers.select_option(game_config.language_package.which_item_move, source_hero.backpack_items)


    if source_location == game_config.language_package.melee:
        item_name = source_hero.melee_weapon
        source_hero.melee_weapon = None
    if source_location == game_config.language_package.ranged:
        item_name = source_hero.ranged_weapon
        source_hero.ranged_weapon = None
    if source_location == game_config.language_package.shield:
        item_name = source_hero.shield
        source_hero.shield = None
    if source_location == game_config.language_package.armor:
        item_name = source_hero.armor
        source_hero.armor = None
    if source_location == game_config.language_package.active_items:
        source_hero.active_items.remove(item_name)
    if source_location == game_config.language_package.backpack_items:
        source_hero.backpack_items.remove(item_name)

    item = config_finder.get_item(item_name)




    target_locations = [game_config.language_package.throw_away, game_config.language_package.backpack_items]
    if not target_hero.melee_weapon and item.is_weapon and item.is_melee:
        target_locations.append(game_config.language_package.melee)
    if not target_hero.ranged_weapon and item.is_weapon and item.is_ranged:
        target_locations.append(game_config.language_package.ranged)
    if not target_hero.shield and item.is_shield:
        target_locations.append(game_config.language_package.shield)
    if not target_hero.armor and item.is_armor:
        target_locations.append(game_config.language_package.armor)
    if len(target_hero.active_items) < target_hero.active_item_slots and not item.is_armor and not item.is_weapon and not item.is_shield:
        target_locations.append(game_config.language_package.active_items)

    target_location = helpers.select_option(game_config.language_package.item_target, target_locations)
    
    if target_location == game_config.language_package.throw_away:
        return
    if target_location == game_config.language_package.melee:
        target_hero.melee_weapon = item_name
    if target_location == game_config.language_package.ranged:
        target_hero.ranged_weapon = item_name
    if target_location == game_config.language_package.shield:
        target_hero.shield = item_name
    if target_location == game_config.language_package.armor:
        target_hero.armor = item_name
    if target_location == game_config.language_package.active_items:
        target_hero.put_item_into_active_items(item_name)
    if target_location == game_config.language_package.backpack_items:
        target_hero.backpack_items.append(item_name)


def move_company_items(company:Company):
    move = True
    while move:
        for hero in company.heroes:
            show_inventory(hero)
        source_hero_name = helpers.select_option(game_config.language_package.hero_source, [hero.name for hero in company.heroes])
        target_hero_name = helpers.select_option(game_config.language_package.hero_target, [hero.name for hero in company.heroes])
        source_hero = [hero for hero in company.heroes if hero.name==source_hero_name][0]
        target_hero = [hero for hero in company.heroes if hero.name==target_hero_name][0]
        hero_swapping = True
        while hero_swapping:
            move_item(source_hero, target_hero)
            hero_swapping = helpers.select_yes_no(game_config.language_package.more_move_from_to.format(source_hero_name=source_hero_name, target_hero_name=target_hero_name))
        move = helpers.select_yes_no(game_config.language_package.more_move) 

def add_item(company:Company, item_name:str):
    item = config_finder.get_item(item_name)
    hero_name = helpers.select_option(game_config.language_package.who_gets.format(item_name=item.display_name), [hero.name for hero in company.heroes])
    hero = [hero for hero in company.heroes if hero.name==hero_name][0]
    hero.backpack_items.append(item_name)

def move_company_money(company:Company):
    move = True
    while move:
        for hero in company.heroes:
            show_money(hero)
        source_hero_name = helpers.select_option(game_config.language_package.hero_source, [hero.name for hero in company.heroes])
        target_hero_name = helpers.select_option(game_config.language_package.hero_target, [hero.name for hero in company.heroes])
        source_hero = [hero for hero in company.heroes if hero.name==source_hero_name][0]
        target_hero = [hero for hero in company.heroes if hero.name==target_hero_name][0]
        
        money = helpers.get_number_input(game_config.language_package.money_transfer_count, source_hero.money)
        source_hero.money -= money
        target_hero.money += money
        move = helpers.select_yes_no(game_config.language_package.transfer_more_money) 

def add_money(company:Company, money_value:int):
    hero_name = helpers.select_option(game_config.language_package.money_target.format(money=money_value), [hero.name for hero in company.heroes])
    hero = [hero for hero in company.heroes if hero.name==hero_name][0]
    hero.money += money_value

def buy_item(hero:Hero, available_item_names:list[str]):
    available_items = [item for item in game_config.items if item.name in available_item_names]
    def get_shop_entry(item:Item) -> str:
        return f'{item.name} ({item.money_value})'
    too_expensive_items = [item for item in available_items if item.money_value > hero.money]
    actual_available_items = [item for item in available_items if item.money_value <= hero.money]
    print(game_config.language_package.too_expensive)
    for item in too_expensive_items:
        print(get_shop_entry(item))
    shop_entry_to_buy = helpers.select_option(game_config.language_package.which_buy, [
        get_shop_entry(item) for item in actual_available_items
    ] + [game_config.language_package.no_item])
    if shop_entry_to_buy == game_config.language_package.no_item:
        return
    item_to_buy = [item for item in actual_available_items if get_shop_entry(item) == shop_entry_to_buy][0]
    hero.modify_money(-1 * item_to_buy.money_value)
    hero.backpack_items.append(item_to_buy.name)
    print(game_config.language_package.got_into_back.format(hero_name=hero.name, item_name=item_to_buy.display_name))

def sell_item(hero:Hero):
    items = [game_config.language_package.no_item]
    active_postfix = f' ({game_config.language_package.backpack})'
    backpack_postfix = f' ({game_config.language_package.backpack})'
    if hero.active_items:
        items += [f'{item}{active_postfix}' for item in hero.active_items]
    if hero.backpack_items:
        items += [f'{item}{backpack_postfix}' for item in hero.backpack_items]
    if not items:
        print(game_config.language_package.nothing_to_sell)
        return
    selected_item = helpers.select_option(game_config.language_package.which_sell, items)
    if selected_item == game_config.language_package.no_item:
        return
    if backpack_postfix in selected_item:
        item = config_finder.get_item(selected_item.strip(backpack_postfix))
        hero.backpack_items.remove(item.name)
        hero.money += item.money_value / 2
    if active_postfix in selected_item:
        item = config_finder.get_item(selected_item.strip(active_postfix))
        hero.active_items.remove(item.name)
        hero.money += item.money_value / 2
