from typing import Literal
from tungeon.config.schema.functionality import Functionality
from tungeon.config.schema.json_representation import JSONRepresentation

CONDITION_TYPE_ENEMY_MIN = 'enemy-min'

class Skill(JSONRepresentation):
    def __init__(self, json_data: dict) -> None:
        super().__init__(json_data)
    
    @property
    def name(self):
        return self.json_data['name']
    
    @property
    def display_name(self):
        return self.json_data['display-name']
    
    @property
    def functions(self) -> list[Functionality]:
        funcs = [Functionality(func) for func in self.json_data.get('functions')]
        for func in funcs:
            func.display_name = self.display_name
        return funcs
    
    @property
    def learning_cost_money(self) -> int | None:
        '''
        Price to pay for learning
        '''
        return self.json_data.get('learning-cost-money')
    
    @property
    def learning_cost_improvement_points(self) -> int | None:
        '''
        Amount of improvement points to use for learning
        '''
        return self.json_data.get('learning-cost-improvement-points')
    
    @property
    def learning_required_skills(self) -> list[str]:
        '''
        Names of skills required before being able to learn the skill
        '''
        return self.json_data.get('learning-required-skills')
    
    @property
    def learning_removes_skills(self) -> list[str]:
        '''
        Names of skills getting removed when learning the skill
        '''
        return self.json_data.get('learning-removes-skills')
        
    @property
    def other_skill_prevention(self) -> list[str]:
        '''
        Names of skills the hero is prevented to learn when having this skill
        '''
        return self.json_data.get('other-skill-prevention',[])