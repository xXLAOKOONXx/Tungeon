import json
from os import path
from tungeon.config.schema.item import Item
from tungeon.config.schema.language_package import LanguagePackage
from tungeon.config.schema.profession import Profession
from tungeon.config.schema.race import Race
from tungeon.config.schema.region import Region
from tungeon.config.schema.reward_set import RewardSet
from tungeon.config.schema.skill import Skill

class GameConfiguration:
    '''
    This class represents the game settings.
    You can imagine this the explaination of the world.
    This is the python implementation.
    Rule of thumb: replace '_' with '-' and you receive the attribute name in json.
    '''
    PROFESSIONS_FILENAME = 'professions.json'
    '''filename for professions configuration'''
    RACES_FILENAME = 'races.json'
    '''filename for professions configuration'''
    REGIONS_FILENAME = 'regions.json'
    '''filename for regions configuration'''
    SKILLS_FILENAME = 'skills.json'
    '''filename for skills configuration'''
    ITEMS_FILENAME = 'items.json'
    '''filename for items configuration'''
    REWARDSETS_FILENAME = 'rewardsets.json'
    '''filename for rewardsets configuration'''
    LANGUAGEPACKAGE_FILENAME = 'language_package.json'
    '''filename for language package'''

    def __init__(self, configuration_folder) -> None:
        self.configuration_folder = configuration_folder
        pass
    
    @property
    def professions(self) -> list[Profession]:
        '''
        list of all professions available in this world.
        professions defines starting money, item, skills as well as future potential to learn skills
        '''
        if not hasattr(self, '_professions'):
            filepath = path.join(self.configuration_folder, self.PROFESSIONS_FILENAME)
            with open(filepath) as f:
                j = json.load(f)
            if not isinstance(j, list):
                raise ValueError(f'Configurationfile for professions is faulty, should be list containing professions, please check {filepath}')
            self._professions = [Profession(element) for element in j]
        return self._professions
    
    @property
    def races(self) -> list[Race]:
        '''
        list of all races in this world.
        races define some basic properties of a hero.
        '''
        if not hasattr(self, '_races'):
            filepath = path.join(self.configuration_folder, self.RACES_FILENAME)
            with open(filepath) as f:
                j = json.load(f)
            if not isinstance(j, list):
                raise ValueError(f'Configurationfile for races is faulty, should be list containing Races, please check {filepath}')
            self._races = [Race(element) for element in j]
        return self._races
    
    @property
    def regions(self) -> list[Region]:
        '''
        list of all regions available in this world.
        This is a quite complex file.
        '''
        if not hasattr(self, '_regions'):
            filepath = path.join(self.configuration_folder, self.REGIONS_FILENAME)
            with open(filepath) as f:
                j = json.load(f)
            if not isinstance(j, list):
                raise ValueError(f'Configurationfile for regions is faulty, should be list containing region, please check {filepath}')
            self._regions = [Region(element) for element in j]
        return self._regions
    
    @property
    def skills(self) -> list[Skill]:
        '''
        All skills available in this world
        '''
        if not hasattr(self, '_skills'):
            filepath = path.join(self.configuration_folder, self.SKILLS_FILENAME)
            with open(filepath) as f:
                j = json.load(f)
            if not isinstance(j, list):
                raise ValueError(f'Configurationfile for skills is faulty, should be list containing skills, please check {filepath}')
            self._skills = [Skill(element) for element in j]
        return self._skills
    
    @property
    def items(self) -> list[Item]:
        '''
        list of all items available in this world.
        if an item is not listed here it does not exist.
        '''
        if not hasattr(self, '_items'):
            filepath = path.join(self.configuration_folder, self.ITEMS_FILENAME)
            with open(filepath) as f:
                j = json.load(f)
            if not isinstance(j, list):
                raise ValueError(f'Configurationfile for items is faulty, should be list containing items, please check {filepath}')
            self._items = [Item(element) for element in j]
        return self._items
    
    @property
    def reward_sets(self) -> list[RewardSet]:
        '''
        list of reward sets.
        a rewardset enables chance-based rewards
        '''
        if not hasattr(self, '_reward_sets'):
            filepath = path.join(self.configuration_folder, self.REWARDSETS_FILENAME)
            with open(filepath) as f:
                j = json.load(f)
            if not isinstance(j, list):
                raise ValueError(f'Configurationfile for rewardsets is faulty, should be list containing rewardsets, please check {filepath}')
            self._reward_sets = [RewardSet(element) for element in j]
        return self._reward_sets
    
    @property
    def language_package(self) -> LanguagePackage:
        '''
        Language Package to enable use of different language via configuration versus hard-codding,
        currently underdeveloped -> many texts are hard coded german
        '''
        if not hasattr(self, '_language_package'):
            filepath = path.join(self.configuration_folder, self.LANGUAGEPACKAGE_FILENAME)
            with open(filepath) as f:
                j = json.load(f)
            if not isinstance(j, dict):
                raise ValueError(f'Configurationfile for language_package is faulty, should be json object, please check {filepath}')
            self._language_package = LanguagePackage(j)
        return self._language_package

def set_game_config(configuration_folder):
    global game_config
    game_config = GameConfiguration(configuration_folder)