

from tungeon.config.schema.json_representation import JSONRepresentation, NamedJSONRepresentation

class StarterSkill(JSONRepresentation):
    def __init__(self, json_data: dict) -> None:
        super().__init__(json_data)

    @property
    def skill_name(self) -> str:
        '''
        in case this starter skill is not rolled here is just the plain name of it
        '''
        return self.json_data.get('skill-name')

    @property
    def is_roll(self) -> bool:
        return self.json_data.get('is-roll', False)

    @property
    def roll_results(self) -> list[list[str]]:
        '''
        list of results available for roll.
        a result consists of a list of skill names
        '''
        return self.json_data.get('roll-results', [])

class Profession(NamedJSONRepresentation):
    def __init__(self, json_data: dict) -> None:
        super().__init__(json_data)

    @property
    def available_skills(self) -> list[str]:
        return self.json_data.get('available-skills', [])

    @property
    def double_price_skills(self) -> list[str]:
        '''
        List of skill names costing the doubled price to learn
        '''
        return self.json_data.get('double-price-skills', [])
    
    @property
    def starter_items(self) -> list[str]:
        return self.json_data.get('starter-items')
    
    @property
    def starter_money(self) -> int:
        return self.json_data.get('starter-money', 0)
    
    @property
    def starter_skills(self) -> list[StarterSkill]:
        return [StarterSkill(d) for d in self.json_data.get('starter-skills', [])]