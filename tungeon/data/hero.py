

from typing import Self
from tungeon.config.schema.poison import Poison
from tungeon.data.round_effects import RoundEffect

from tungeon.logics import config_finder


class Hero:
    '''
    Hero of a player
    '''
    def __init__(self,
                 name:str='Odin',
                 race:str='Mensch',
                 profession:str='Kampfer',
                 speed:int=2,
                 strength:int=2,
                 agility:int=2,
                 intelligence:int=2,
                 skills:list[str]=[],
                 armor:str|None=None,
                 melee_weapon:str|None=None,
                 ranged_weapon:str|None=None,
                 shield:str|None=None,
                 active_items:list[str]=[],
                 backpack_items:list[str]=[],
                 origin_regions:list[str]=[],
                 wounds:int=0,
                 money:int=0,
                 active_item_slots:int=6,
                 round_effects:list[RoundEffect] = [],
                 poisons:list[Poison]=[]
                 ) -> None:
        self.name = name
        self.race = race
        self.profession = profession
        self.speed = speed
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.skills = skills
        self.armor = armor
        self.melee_weapon = melee_weapon
        self.ranged_weapon = ranged_weapon
        self.shield = shield
        self.active_items = active_items
        self.backpack_items = backpack_items
        self.origin_regions = origin_regions
        self.wounds = wounds
        self.money = money
        self.active_item_slots = active_item_slots
        self.round_effects = round_effects
        self.poisons = poisons


    def __dict__(self):
        return {
            'name':self.name,
            'race':self.race,
            'profession':self.profession,
            'speed':self.speed,
            'strength':self.strength,
            'agility':self.agility,
            'intelligence':self.intelligence,
            'skills':self.skills,
            'armor':self.armor,
            'melee_weapon':self.melee_weapon,
            'ranged_weapon':self.ranged_weapon,
            'shield':self.shield,
            'active_items':self.active_items,
            'backpack_items':self.backpack_items,
            'origin-regions':self.origin_regions,
            'wounds':self.wounds,
            'money':self.money,
            'active-item-slots':self.active_item_slots,
            'round-effects':[re.__dict__() for re in self.round_effects],
            'poisons':[p.__dict__() for p in self.poisons]
        }
    
    @classmethod
    def from_json(cls, json_data:dict) -> Self:
        return cls(
            name=json_data.get('name'),
            race=json_data.get('race'),
            profession=json_data.get('profession'),
            speed=json_data.get('speed'),
            strength=json_data.get('strength'),
            agility=json_data.get('agility'),
            intelligence=json_data.get('intelligence'),
            skills=json_data.get('skills'),
            armor=json_data.get('armor'),
            melee_weapon=json_data.get('melee_weapon'),
            ranged_weapon=json_data.get('ranged_weapon'),
            shield=json_data.get('shield'),
            active_items=json_data.get('active_items'),
            backpack_items=json_data.get('backpack_items'),
            origin_regions=json_data.get('origin-regions'),
            wounds=json_data.get('wounds'),
            money=json_data.get('money'),
            active_item_slots=json_data.get('active-item-slots'),
            round_effects=[RoundEffect.from_dict(re) for re in json_data.get('round-effects')],
            posions=[Poison.from_dict(d) for d in json_data.get('poisons')]
        )
    
    def inventory_str(self) -> str:
        new_line = '\n'
        lines = []
        if self.melee_weapon:
            lines.append(f'Nahkampfwaffe: {self.melee_weapon}')
        if self.ranged_weapon:
            lines.append(f'Fernkampfwaffe: {self.ranged_weapon}')
        if self.shield:
            lines.append(f'Schild: {self.shield}')
        if self.armor:
            lines.append(f'Ruestung: {self.armor}')
        if self.active_items:
            lines.append(f'''Aktive Gegenstände:{[f'{config_finder.get_item(item).display_name}' for item in self.active_items]}''')
        if self.backpack_items:
            lines.append(self.backpack_str())
        return '\n'.join(lines)
    
    def backpack_str(self) -> str:
        return f'''Gegenstände im Rucksack: {', '.join([f'{config_finder.get_item(item).display_name}' for item in self.backpack_items])}'''
    
    def skills_str(self) -> str:
        return '\n'.join([
            f'Schnelligkeit: {self.speed}',
            f'Stärke: {self.strength}',
            f'Agilität: {self.agility}',
            f'Weisheit: {self.intelligence}',
            f'Fähigkeiten:',
            '\n'.join([config_finder.get_skill(skill).display_name for skill in self.skills])
        ])
    
    def __str__(self) -> str:
        return '\n'.join([
            f'{self.name}:',
            f'{self.race}, {self.profession}',
            f'Geld: {self.money}',
            self.inventory_str(),
            self.skills_str(),
            f'Wunden: {self.wounds}',
            f'Maximale aktive Gegenstände: {self.active_item_slots}'
        ])
    
    @property
    def current_strength(self) -> int:
        return self.strength + sum([round_effect.bonus_strength for round_effect in self.round_effects])
    
    @property
    def current_agility(self) -> int:
        return self.agility + sum([round_effect.bonus_agility for round_effect in self.round_effects])
    
    @property
    def current_speed(self) -> int:
        return self.speed + sum([round_effect.bonus_speed for round_effect in self.round_effects])
    
    @property
    def current_intelligence(self) -> int:
        return self.intelligence + sum([round_effect.bonus_intelligence for round_effect in self.round_effects])

    def modify_money(self, money_change):
        new_money = self.money + money_change
        if new_money < 0:
            raise ValueError('Hero has not enough money')
        self.money = int(new_money)
