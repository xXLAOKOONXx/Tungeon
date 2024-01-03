
from tungeon.config.schema.json_representation import NamedJSONRepresentation
from tungeon.config.schema.region_event import RegionEvent

class Region(NamedJSONRepresentation):
    def __init__(self, json_data: dict) -> None:
        super().__init__(json_data)

    @property
    def available_regions(self) -> list[str]:
        '''
        regions available for travel (list of region-names)
        '''
        return self.json_data.get('available-regions',[])
    
    @property
    def free_camping(self) -> bool:
        return self.json_data.get('free-camping', False)
    
    @property
    def events(self) -> list[RegionEvent]:
        return [RegionEvent(element) for element in self.json_data.get('events', [])]
    
    @property
    def shop_items(self) -> list[str]:
        return self.json_data.get('shop-items', [])
    
    @property
    def trainable_skills(self) -> list[str]:
        return self.json_data.get('trainable-skills', [])
