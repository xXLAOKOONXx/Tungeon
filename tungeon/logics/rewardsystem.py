import random
from typing import Tuple
from tungeon.config.game_config import game_config
from tungeon.config.schema.reward_draws import RewardDraw


def draw_reward(settings:RewardDraw) -> Tuple[int, list[str]]:
    '''
    Returns:
    - money(int): Money value
    - items(list[str]): List of item names
    '''
    
    filtered_rewardsets = [set for set in game_config.reward_sets if set.name == settings.rewardset_name]
    if len(filtered_rewardsets) != 1:
        raise ValueError(f'Unable to uniquely identify {settings.rewardset_name} in game configuration')
    rewardset = filtered_rewardsets[0]
    draw_score = settings.draw_base
    for dice_sides, dice_rolls in zip([6, 10, 100], [settings.draw_d6_count, settings.draw_d10_count, settings.draw_d100_count]):
        for _ in range(0, dice_rolls or 0):
            draw_score += random.randint(1, dice_sides)
    reward = [reward for reward in rewardset.rewards if draw_score in reward.values][0]
    money = reward.money
    items = reward.items
    for additional_draw in reward.rewardset_draws:
        additional_money, additional_items = draw_reward(additional_draw)
        money += additional_money
        items += additional_items
    return money, items