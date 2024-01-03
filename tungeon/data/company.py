from typing import Self
from tungeon.data.hero import Hero
import json
json.dumps
class Company:
    '''
    Company of a player
    '''
    def __init__(self, name:str, heroes:list[Hero]=[Hero('Odin'), Hero('Thor'), Hero('Tyr'), Hero('Freya')], improvement_points:int=0, current_region=None, exit_region=None, current_event=None) -> None:
        self.name = name
        self.heroes = heroes
        self.improvement_points = improvement_points
        self.current_region = current_region
        self.current_event = current_event
        self.exit_region = exit_region

    def add_improvement_points(self, count:int):
        self.improvement_points += count

    def get_hero(self, hero_name:str) -> Hero:
        return [hero for hero in self.heroes if hero.name == hero_name][0]
    
    def use_improvement_points(self, amount:int):
        self.improvement_points -= amount

    def __dict__(self):
        return {
            'name':self.name,
            'heroes':[hero.__dict__() for hero in self.heroes],
            'improvement-points':self.improvement_points,
            'current-region':self.current_region,
            'current-event':self.current_event,
            'exit-region':self.exit_region
        }
    
    def __str__(self):
        return '\n'.join([
            self.name,
            ''.join(['-' for c in self.name]),
            f'Steigerungspunkte: {self.improvement_points}',
            '\n'.join([str(hero) for hero in self.heroes])
        ])
    
    @classmethod
    def from_json(cls, json_dict:dict) -> Self:
        return cls(
            name=json_dict.get('name'),
            heroes=[Hero.from_json(hero_dict) for hero_dict in json_dict.get('heroes')],
            improvement_points=json_dict.get('improvement-points'),
            current_region=json_dict.get('current-region'),
            current_event=json_dict.get('current-event'),
            exit_region=json_dict.get('exit-region')
        )
    
    def enter_next_round(self):
        for hero in self.heroes:
            for round_effect in hero.round_effects:
                round_effect.round_count -= 1
            hero.round_effects = [round_effect for round_effect in hero.round_effects if round_effect < 0]