from tungeon.config.schema.json_representation import JSONRepresentation, NamedJSONRepresentation
from tungeon.config.schema.reward_draws import RewardDraw
    
class Reward(JSONRepresentation):
    def __init__(self, json_data: dict) -> None:
        super().__init__(json_data)

    @property
    def values(self) -> list[int]:
        '''Values that trigger the reward'''
        return self.json_data.get('values', [])
    
    @property
    def money(self) -> int | None:
        return self.json_data.get('money')
    
    @property
    def items(self) -> list[str]:
        return self.json_data.get('items', [])
    
    @property
    def rewardset_draws(self) -> list[RewardDraw]:
        return [RewardDraw(element) for element in self.json_data.get('rewardset-draws', [])]


class RewardSet(NamedJSONRepresentation):
    def __init__(self, json_data: dict) -> None:
        super().__init__(json_data)

    @property
    def description(self) -> str | None:
        return self.json_data.get('description')

    @property
    def rewards(self) -> list[Reward]:
        return [Reward(element) for element in self.json_data.get('rewards', [])]