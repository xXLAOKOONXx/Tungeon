from tungeon.config.schema.json_representation import JSONRepresentation


class BaseSkillCheck(JSONRepresentation):
    def __init__(self, json_data: dict) -> None:
        super().__init__(json_data)

    @property
    def is_agility(self) -> bool:
        return self.json_data.get('is-agility', False)

    @property
    def is_strength(self) -> bool:
        return self.json_data.get('is-strength', False)

    @property
    def is_speed(self) -> bool:
        return self.json_data.get('is-speed', False)

    @property
    def is_intelligence(self) -> bool:
        return self.json_data.get('is-intelligence', False)
    
    @property
    def check_modifier(self) -> int:
        return self.json_data.get('check-modifier', 0)
    
    @property
    def check_types(self) -> list[str]:
        return self.json_data.get('check-types',[])