from dataclasses import dataclass, field


@dataclass
class RoundEffect:
    round_count:int = 0
    bonus_strength:int = 0
    bonus_agility:int = 0
    bonus_speed:int = 0
    bonus_intelligence:int = 0
    bonus_melee_damage:int = 0
    bonus_ranged_damage:int = 0
    poison_type_preventions:list[str] = field(default_factory=list)

    def __dict__(self):
        return {
            'round-count':self.round_count,
            'bonus-strength':self.bonus_strength,
            'bonus-agility':self.bonus_agility,
            'bonus-speed':self.bonus_speed,
            'bonus-intelligence':self.bonus_intelligence,
            'bonus-melee-damage':self.bonus_melee_damage,
            'bonus-ranged-damage':self.bonus_ranged_damage,
            'poison-type-preventions':self.poison_type_preventions
        }
    
    @classmethod
    def from_dict(cls, json_data:dict):
        return cls(
            round_count=json_data.get('round-count'),
            bonus_strength=json_data.get('bonus-strength'),
            bonus_agility=json_data.get('bonus-agility'),
            bonus_speed=json_data.get('bonus-speed'),
            bonus_intelligence=json_data.get('bonus-intelligence'),
            bonus_melee_damage=json_data.get('bonus-melee-damage'),
            bonus_ranged_damage=json_data.get('bonus-ranged-damage'),
            poison_type_preventions=json_data.get('poison-type-preventions')
        )