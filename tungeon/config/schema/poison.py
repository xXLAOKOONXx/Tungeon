
from dataclasses import dataclass
from typing import Self

@dataclass
class Poison:
  duration:int|None=None
  prevents_healing:bool=False
  rounds_until_death:int|None=None
  rounds_until_wound:int|None=None
  malus_on_throws:int|None=None
  throw_types:list[str]|None=None
  poison_types:list[str]|None=None

  def __dict__(self):
    return {
      'duration':self.duration,
      'prevents-healing':self.prevents_healing,
      'rounds-until-death':self.rounds_until_death,
      'rounds-until-wound':self.rounds_until_wound,
      'malus-on-throw':self.malus_on_throws,
      'throw-types':self.throw_types,
      'poison-types':self.poison_types
    }
  
  @classmethod
  def from_dict(cls, d:dict) -> Self:
    return cls(
      duration=d.get('duration'),
      prevents_healing=d.get('prevents-healing'),
      rounds_until_death=d.get('rounds-until-death'),
      rounds_until_wound=d.get('rounds-until-wounds'),
      malus_on_throws=d.get('malus-on-throw'),
      throww_types=d.get('throw-types'),
      poison_types=d.get('poison-types')      
      )