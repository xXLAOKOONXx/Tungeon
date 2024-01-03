from dataclasses import dataclass
import random
from tungeon.config.schema.json_representation import JSONRepresentation
from tungeon.config.schema.region_event import RegionEvent, RegionEventStep
from tungeon.config.schema.skill import Skill
from tungeon.data.company import Company
from tungeon.console_app import fighting_dialog, inventory_dialog, helpers, learning_dialog
from tungeon.logics import rewardsystem, functionality_system, config_finder, hero_actions
from tungeon.data.condition import condition
from tungeon.config.game_config import game_config

@dataclass
class RegionJump():
    target_region:str


def perform_trap(company:Company, step:RegionEventStep) -> int | None:
    if step.text:
        print(step.text)
    for hero in company.heroes:
        trap_skills:list[Skill] =  [config_finder.get_skill(s) for s in hero.skills if any([f.is_prevent_trap and functionality_system.check_conditions_met(f,hero) for f in config_finder.get_skill(s).functions])]
        used_skills = []
        while [s for s in trap_skills if s.name not in used_skills]:
            selected_skill_display_name = helpers.select_option(game_config.language_package.which_skill.format(hero_name=hero.name), [game_config.language_package.no_skill] + [s.display_name for s in trap_skills if s.name not in used_skills])
            if selected_skill_display_name == game_config.language_package.no_skill:
                break
            selected_skill = [s for s in trap_skills if s.display_name == selected_skill_display_name][0]
            condition.get_hero_condition(hero.name).used_skill_groups += selected_skill.function_groups
            for f in selected_skill.functions:
                if f.is_prevent_trap:
                    if hero_actions.do_check(hero, f):
                        return step.no
        trap_items = [config_finder.get_item(i) for i in hero.active_items + [hero.melee_weapon] + [hero.shield] + [hero.armor] + [hero.ranged_weapon] if i]
        trap_items = [t for t in trap_items if any([f.is_prevent_trap and functionality_system.check_conditions_met(f,hero) for f in t.functions])]
        used_items = []
        while [t for t in trap_items if t.name not in used_items]:
            selected_items_display_name = helpers.select_option(game_config.language_package.which_item.format(hero_name=hero.name), [game_config.language_package.no_item] + [t.display_name for t in trap_items])
            if selected_skill_display_name == game_config.language_package.no_item:
                break
            selected_item = [t for t in trap_items if t.display_name == selected_items_display_name][0]
            for f in selected_item.functions:
                if f.is_prevent_trap:
                    if hero_actions.do_check(hero, f):
                        return step.no
    return step.yes

def perform_random(step:RegionEventStep) -> int | None:
    if step.text:
        print(step.text)
    all_vals = []
    for v in step.random_groups:
        all_vals += v.random_values
    r_val = random.sample(all_vals,1)[1]
    for v in step.random_groups:
        if r_val in v.random_values:
            return v.step

def perform_learn_skill(company:Company, step:RegionEventStep) -> int | None:
    learned = False
    hero_options = [game_config.language_package.no_hero] + [h.name for h in company.heroes if h.profession in step.required_professions]
    selected_hero_name = helpers.select_option(game_config.language_package.which_hero_learns, hero_options)
    if selected_hero_name == game_config.language_package.no_hero:
        return step.no
    hero = company.get_hero(selected_hero_name)
    learned = learning_dialog.perform_teacher_learning(company, hero, step.learn_skills)
    return step.yes if learned else step.no


def perform_reward(company:Company, step:RegionEventStep) -> int | None:
    if step.text:
        print(step.text)
    total_money = step.reward_gold or 0
    total_items = step.reward_items
    if step.reward_improvement_points:
        print(game_config.language_package.receive_points.format(points=step.reward_improvement_points))
        company.add_improvement_points(step.reward_improvement_points)
    if step.reward_draws:
        total_draw_money = 0
        total_draw_items = []
        for draw in step.reward_draws:
            draw_money, draw_items = rewardsystem.draw_reward(draw)
            total_draw_money += draw_money
            total_draw_items += draw_items
        total_money += total_draw_money
        total_items += total_draw_items
    if total_money:
        inventory_dialog.add_money(company, total_money)
    if total_items:
        for item in total_items:
            inventory_dialog.add_item(company, item)
    return step.next_step

def perform_step(company:Company, step:RegionEventStep, region_name:str) -> int | None | RegionJump:
    if step.is_fight:
        return fighting_dialog.perform_fight(company, step, region_name)
    if step.is_reward:
        return perform_reward(company, step)
    if step.decision:
        decision = helpers.select_yes_no(step.text)
        return step.yes or step.next_step if decision else step.no or step.next_step
    if step.is_region_jump:
        if step.region_jump_origin:
            return RegionJump(company.exit_region)
        return RegionJump(step.region_jump_target)
    if step.profession_check:
        if any(h.profession in step.required_professions for h in company.heroes):
            return step.yes
        return step.no
    if step.is_random:
        return perform_random(step)
    if step.is_trap:
        return perform_trap(company, step)
    if step.is_steal:
        return inventory_dialog.perform_steal(company, step)
    if step.text:
        print(step.text)
    if step.money_loss:
        able_to_pay = inventory_dialog.pay_money(company, step.money_loss)
        if not able_to_pay and step.unable_to_pay:
            return step.unable_to_pay
    return step.next_step


def perform_event(company:Company, region_event:RegionEvent, region_name:str):
    step = 0
    while isinstance(step, int):
        pot_region_event_step = [s for s in region_event.steps if s.id == step]
        if not pot_region_event_step:
            return
        step = perform_step(company, pot_region_event_step[0], region_name)
    if isinstance(step, RegionJump):
        company.current_region = step.target_region