from tungeon.config.schema.base_skill_check import BaseSkillCheck
from tungeon.config.schema.json_representation import JSONRepresentation, NamedJSONRepresentation
from tungeon.config.schema.reward_draws import RewardDraw

class RegionEvent(NamedJSONRepresentation):
    def __init__(self, json_data: dict) -> None:
        super().__init__(json_data)

    @property
    def values(self) -> list[int]:
        return self.json_data.get('values')
    
    @property
    def steps(self):
        return [RegionEventStep(element) for element in self.json_data.get('steps', [])]
    
class LearnSkill(JSONRepresentation):
    def __init__(self, json_data: dict) -> None:
        super().__init__(json_data)

    @property
    def skill_name(self) -> str:
        return self.json_data.get('skill-name','')
    
    @property
    def money(self) -> int:
        return self.json_data.get('money',0)
    
    @property
    def points(self) -> int:
        return self.json_data.get('points',0)
    
class RandomGroup(JSONRepresentation):
    def __init__(self, json_data: dict) -> None:
        super().__init__(json_data)

    @property
    def random_values(self) -> list[int]:
        return self.json_data.get('random-values', [])
    
    @property
    def step(self) -> int | None:
        return self.json_data.get('step')
    
class Trade(JSONRepresentation):
    def __init__(self, json_data: dict) -> None:
        super().__init__(json_data)

    @property
    def item_name(self) -> str:
        return self.json_data.get('item-name','')
    
    @property
    def money(self) -> int:
        return self.json_data.get('money', 0)

class RegionEventStep(NamedJSONRepresentation):
    def __init__(self, json_data: dict) -> None:
        super().__init__(json_data)

    @property
    def id(self) -> str:
        '''
        id of the step
        '''
        return self.json_data.get('id')
    
    @property
    def text(self) -> str | None:
        '''
        text to tell the player
        '''
        return self.json_data.get('text')
    
    @property
    def decision(self) -> bool:
        '''
        Flag whether the step contains a decision or not
        '''
        return self.json_data.get('decision', False)
    
    @property
    def decision_yes(self) -> int | None:
        '''
        step id to go to if decision is yes
        '''
        return self.json_data.get('decision-yes')
    
    @property
    def decision_no(self) -> int | None:
        '''
        step id to go to if decision is no
        '''
        return self.json_data.get('decision-no')
    
    @property
    def money_loss(self) -> int | None:
        return self.json_data.get('money-loss')
    
    @property
    def unable_to_pay(self) -> int | None:
        return self.json_data.get('unable-to-pay')

    @property
    def is_fight(self) -> bool:
        return self.json_data.get('is-fight', False)
    
    @property
    def fight_enemy_count(self) -> int | None:
        return self.json_data.get('fight-enemy-count')
    
    @property
    def fight_enemy_dice(self) -> int | None:
        '''
        Number dice to roll for the enemy
        '''
        return self.json_data.get('fight-enemy-dice')
    
    @property
    def fight_enemy_base_damage(self) -> int | None:
        return self.json_data.get('fight-enemy-base-damage')
    
    @property
    def fight_enemy_resistance(self) -> int | None:
        return self.json_data.get('fight-enemy-resistance')
    
    @property
    def fight_thief_count(self) -> int | None:
        return self.json_data.get('fight-thief-count')
    
    @property
    def fight_win(self) -> int | None:
        return self.json_data.get('fight-win')
    
    @property
    def fight_loose(self) -> int | None:
        return self.json_data.get('fight-loose')
    
    @property
    def fight_tie(self) -> int | None:
        return self.json_data.get('fight-tie')
    
    @property
    def is_reward(self) -> bool:
        return self.json_data.get('is-reward', False)
    
    @property
    def reward_gold(self) -> int | None:
        return self.json_data.get('reward-gold')
    
    @property
    def reward_draws(self) -> list[RewardDraw]:
        return [RewardDraw(draw) for draw in self.json_data.get('reward-draws',[])]
    
    @property
    def reward_improvement_points(self) -> int | None:
        return self.json_data.get('reward-improvement-points')
    
    @property
    def reward_items(self) -> list[str]:
        return self.json_data.get('reward-items')
    
    @property
    def next_step(self) -> int:
        return self.json_data.get('next-step')
    
    @property
    def is_region_jump(self) -> bool:
        return self.json_data.get('region-jump', False)
    
    @property
    def region_jump_target(self) -> str |None:
        return self.json_data.get('region-jump-target')
    
    @property
    def region_jump_origin(self) -> bool:
        return self.json_data.get('region-jump-origin', False)
    
    @property
    def learn_skills(self) -> LearnSkill:
        return [LearnSkill(ls) for ls in self.json_data.get('learn-skills',[])]
    
    @property
    def learn_yes(self) -> int | None:
        return self.json_data.get('learn-yes')
    
    @property
    def learn_no(self) -> int | None:
        return self.json_data.get('learn-no')
    
    @property
    def yes(self) -> int | None:
        return self.json_data.get('yes', self.next_step)
    
    @property
    def no(self) -> int | None:
        return self.json_data.get('no', self.next_step)
        
    
    @property
    def required_professions(self) -> list[str]:
        return self.json_data.get('required-professions',[])
    
    @property
    def profession_check(self) -> bool:
        return self.json_data.get('profession-check', False)
    
    @property
    def is_random(self) -> bool:
        return self.json_data.get('is-random', False)
    
    @property
    def random_groups(self) -> list[RandomGroup]:
        return [RandomGroup(rg) for rg in self.json_data.get('random-groups', [])]
    
    @property
    def is_trap(self) -> bool:
        return self.json_data.get('is-trap', False)
    
    @property
    def is_steal(self) -> bool:
        return self.json_data.get('is-steal', False)
    
    @property
    def steal_types(self) -> list[str]:
        return self.json_data.get('steal-types', [])
    
    @property
    def hero_positions(self) -> list[int]:
        return self.json_data.get('hero-positions', [])
    
    @property
    def can_miss(self) -> bool:
        return self.json_data.get('can-miss', False)
    
    @property
    def backpack_parts(self) -> bool:
        return self.json_data.get('backpack-parts', False)
    
    @property
    def is_forced(self) -> bool:
        return self.json_data.get('is-forced', False)
    
    @property
    def fight_melee(self) -> bool:
        return self.json_data.get('fight-melee', False)
        
    @property
    def fight_ranged(self) -> bool:
        return self.json_data.get('fight-ranged', False)
    
    @property
    def fight_enemy_types(self) -> list[str]:
        return self.json_data.get('fight-enemy-types',[])
    
    @property
    def is_skill_check(self) -> bool:
        return self.json_data.get('is-skill-check', False)
    
    @property
    def required_races(self) -> list[str]:
        return self.json_data.get('required-races', [])
    
    @property
    def base_skill_check(self) -> BaseSkillCheck | None:
        return self.json_data.get('base-skill-check')
    
    @property
    def is_single_hero(self) -> bool:
        return self.json_data.get('is-single-hero', False)
    
    @property
    def random_hero(self) -> list[int]:
        return self.json_data.get('random-hero', [])
    
    @property
    def is_trade(self) -> bool:
        return self.json_data.get('is-trade', False)
    
    @property
    def trades(self) -> list[Trade]:
        return [Trade(t) for t in self.json_data.get('trades', [])]
    
    @property
    def allow_money_move(self) -> bool:
        return self.json_data.get('allow-money-move', False)
    
    @property
    def allow_multiple_buy(self) -> bool:
        return self.json_data.get('allow-money-move', False)