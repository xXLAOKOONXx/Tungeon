
from tungeon.config.schema.base_skill_check import BaseSkillCheck
from tungeon.config.schema.json_representation import JSONRepresentation


class Functionality(JSONRepresentation):
    def __init__(self, json_data: dict) -> None:
        super().__init__(json_data)

    _display_name = ''
    @property
    def display_name(self) -> str:
        return self._display_name
    
    @display_name.setter
    def display_name(self, value:str):
        self._display_name = value
    
    @property
    def fight_flat_bonus(self) -> int | None:
        '''
        Bonus damage in fights
        '''
        return self.json_data.get('fight-flat-bonus')
    
    @property
    def condition_type(self) -> str | None:
        '''
        conition type as keyword
        '''
        return self.json_data.get('condition-type')
    
    @property
    def condition_threshhold(self) -> int | None:
        '''
        threshhold required to trigger functionality
        '''
        return self.json_data.get('condition-threshhold')
    
    @property
    def fight_type(self) -> str | None:
        '''
        fight type as keyword
        '''
        return self.json_data.get('fight-type')
    
    @property
    def base_skill_check(self) -> BaseSkillCheck | None:
        '''
        base check if needed to use function
        '''
        check = self.json_data.get('base-skill-check')
        return BaseSkillCheck(check) if check else None
    
    @property
    def reroll_types(self) -> list[str]:
        return self.json_data.get('reroll-types',[])
    
    @property
    def regions(self) -> list[str]:
        return self.json_data.get('regions',[])
    
    @property
    def destructive(self) -> bool:
        return self.json_data.get('destructive', False)
    
    @property
    def wound_resistance(self) -> int | None:
        return self.json_data.get('wound-resistance')
    
    @property
    def resistance_passing(self) -> int |None:
        return self.json_data.get('resistance-passing')
    
    @property
    def resistance_surpassing(self) -> bool:
        return self.json_data.get('resistance-surpassing')
    
    @property
    def function_groups(self) -> list[str]:
        '''
        
        '''
        return self.json_data.get('function-groups',[])
    
    @property
    def strength_bonus(self) -> int | None:
        '''
        
        '''
        return self.json_data.get('strength-bonus')
    
    @property
    def speed_bonus(self) -> int | None:
        '''
        
        '''
        return self.json_data.get('speed-bonus')
    
    @property
    def agility_bonus(self) -> int | None:
        '''
        
        '''
        return self.json_data.get('agility-bonus')
    
    @property
    def intelligence_bonus(self) -> int | None:
        '''
        
        '''
        return self.json_data.get('intelligence-bonus')
    
    @property
    def additional_rounds(self) -> int | None:
        '''
        
        '''
        return self.json_data.get('aditional-rounds')
    
    @property
    def other_hero_allowed(self) -> bool:
        return self.json_data.get('other-hero-allowed', False)
    
    @property
    def is_prevent_trap(self) -> bool:
        return self.json_data.get('is-prevent-trap', False)
    
    @property
    def fight_rounds(self) -> list[int]:
        return self.json_data.get('fight-rounds', [])
    
    @property
    def fight_voluntary_required(self) -> bool:
        return self.json_data.get('fight-voluntary-required', False)
    
    @property
    def fight_enemy_min(self) -> int | None:
        return self.json_data.get('fight-enemy-min')
    
    @property
    def death_wound_resistance(self) -> int | None:
        return self.json_data.get('death-wound-resistance')
    
    @property
    def fight_enemy_types(self) -> list[str] | None:
        return self.json_data.get('fight-enemy-types')
    
    @property
    def poison_type_preventions(self) -> list[str] | None:
        return self.json_data.get('poison-type-prevention')
    
    @property
    def healing_poison_types(self) -> list[str] | None:
        return self.json_data.get('healing-poison-types')
    
    @property
    def poison_count_cleaning(self) -> int | None:
        return self.json_data.get('poison-count-cleaning')
    
    @property
    def heals_poison(self) -> bool:
        return self.json_data.get('heals-poison', False)
