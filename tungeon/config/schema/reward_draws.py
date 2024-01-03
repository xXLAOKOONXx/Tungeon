

from tungeon.config.schema.json_representation import NamedJSONRepresentation


class RewardDraw(NamedJSONRepresentation):
    '''
    Draw for a reward including all needed information
    '''
    def __init__(self, json_data: dict) -> None:
        super().__init__(json_data)

    @property
    def rewardset_name(self) -> str | None:
        '''
        Name of the rewardset to use
        '''
        return self.json_data.get('rewardset-name')
    
    @property
    def draw_d6_count(self) -> int | None:
        '''
        Amount of 6-sided dices to draw
        '''
        return self.json_data.get('draw-d6-count')
    
    @property
    def draw_d10_count(self) -> int | None:
        '''
        Amount of 10-sided dices to draw
        '''
        return self.json_data.get('draw-d10-count')
    
    @property
    def draw_d100_count(self) -> int | None:
        '''
        Amount of 100-sided dices to draw
        '''
        return self.json_data.get('draw-d100-count')
    
    @property
    def draw_base(self) -> int | None:
        '''
        Base value for the draw
        '''
        return self.json_data.get('draw-base')