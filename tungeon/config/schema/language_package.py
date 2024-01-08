from tungeon.config.schema.json_representation import JSONRepresentation


class LanguagePackage(JSONRepresentation):
    def __init__(self, json_data: dict) -> None:
        super().__init__(json_data)

    @property
    def yes(self) -> str:
        return self.json_data.get('yes', 'Yes')
    
    @property
    def no(self) -> str:
        return self.json_data.get('no', 'No')
    
    @property
    def faulty_input(self) -> str:
        return self.json_data.get('faulty-input', 'Faulty input')
    
    @property
    def select(self) -> str:
        return self.json_data.get('select', 'Select')
    
    @property
    def fight_melee_question(self) -> str:
        return self.json_data.get('fight-melee-question', 'Shouldd the hero fight melee?')
    
    @property
    def your_dice_throw(self) -> str:
        return self.json_data.get('your-dice-throw', 'Here is your dice throw:')
    
    @property
    def change_dice_question(self) -> str:
        return self.json_data.get('change-dice-question', 'Do you want to change a dice?')
    
    @property
    def change_dice_select(self) -> str:
        return self.json_data.get('change-dice-select', 'Which dice do you want to change?')
    
    @property
    def use_item(self) -> str:
        return self.json_data.get('use-item', 'Which item do you want to use?')
    
    @property
    def wanna_prep(self) -> str:
        return self.json_data.get('wanna-prep', 'Do you want to perform some preperation?')
    
    @property
    def no_skill(self) -> str:
        return self.json_data.get('no-skill', 'None')
    
    @property
    def which_skill(self) -> str:
        return self.json_data.get('which-skill', 'Which skill of {hero_name} do you want to use?')
     
    @property
    def no_item(self) -> str:
        return self.json_data.get('no-item', 'None')
    
    @property
    def which_item(self) -> str:
        return self.json_data.get('which-item', 'Which item of {hero_name} do you want to use?')
    
    @property
    def no_hero(self) -> str:
        return self.json_data.get('no-hero', 'None')
    
    @property
    def which_hero_learns(self) -> str:
        return self.json_data.get('which-hero-learns', 'Which hero can learn?')
    
    @property
    def which_heros_skill(self) -> str:
        return self.json_data.get('which-hero-learns', 'Which heros skill do you want to use?')
    
    @property
    def receive_points(self) -> str:
        return self.json_data.get('receive-points', 'You receive {points} improvement points.')

    @property
    def round_msg(self) -> str:
        return self.json_data.get('round-msg', 'We are in round {round}.')
    
    @property
    def fight_win(self) -> str:
        return self.json_data.get('fight-win', 'You won the fight.')
    @property
    def fight_tie(self) -> str:
        return self.json_data.get('fight-tie', 'You lost the fight.')
    @property
    def fight_loose(self) -> str:
        return self.json_data.get('fight-loose', 'The fight ended in a tie.')

    @property
    def receive_wounds(self) -> str:
        return self.json_data.get('receive-wounds', 'Your heroes received {wounds} wounds.')

    @property
    def enter_number_error(self) -> str:
        return self.json_data.get('enter-number-error', 'Please enter a number, try again.')
    
    @property
    def enter_number_max_error(self) -> str:
        return self.json_data.get('enter-number-max-error','Input too high, maximum value is {max}, try again.')

    @property
    def enter_number_pos_error(self) -> str:
        return self.json_data.get('enter-number-pos-error', 'Input needs to be positive, try again.')
    
    @property
    def select_out_of_range(self) -> str:
        return self.json_data.get('select-out-of-range', 'Input not in offered range.')

    @property
    def hero_dice_roll(self) -> str:
        return self.json_data.get('hero-dice-roll', '{hero_name} rolled a {dice_roll}.')
    
    @property
    def item_gets_destroyed(self) -> str:
        return self.json_data.get('item-gets-destroyed', 'gets destroyed on use')

    @property
    def use_item_for_roll(self) -> str:
        return self.json_data.get('use-item-for-roll', 'Do you want to use an item to reroll?')

    @property
    def new_roll(self) -> str:
        return self.json_data.get('new-roll', 'Your reroll is {dice_roll}.')

    @property
    def lost_item(self) -> str:
        return self.json_data.get('lost-item', 'You lost {item_name}.')

    @property
    def strength(self) -> str:
        return self.json_data.get('strength', 'strength')
    @property
    def speed(self) -> str:
        return self.json_data.get('speed', 'speed')
    @property
    def agility(self) -> str:
        return self.json_data.get('agility', 'agility')
    @property
    def intelligence(self) -> str:
        return self.json_data.get('intelligence', 'intelligence')
    
    @property
    def req_check(self) -> str:
        return self.json_data.get('req-check', 'You need a check for {skill_name} ({skill_value})')

    @property
    def wanna_use_destr_item(self) -> str:
        return self.json_data.get('wanna-use-destr-item', 'Do you want to use {item_name} of {hero_name}? (This destroys the item)')
    
    @property
    def func_used(self) -> str:
        return self.json_data.get('func-used', '{func_name} was used.')

    @property
    def skill_check_info(self) -> str:
        return self.json_data.get('skill-check-info', 'You have a {skill_name} of {skill_value} and the check has a modifier of {check_modifier}, so you need at least {req_value} or lower.')

    @property
    def skill_check_auto_no(self) -> str:
        return self.json_data.get('skill-check-auto-no', 'You know this is impossible, your try fails.')

    @property
    def skill_target_hero(self) -> str:
        return self.json_data.get('skill-target-hero', 'On which hero do you want to apply the skill?')

    @property
    def prep_question(self) -> str:
        return self.json_data.get('prep-question', 'What do you want to do?')

    @property
    def move_items(self) -> str:
        return self.json_data.get('move-items', 'Trade items')
    
    @property
    def nothing(self) -> str:
        return self.json_data.get('nothing', 'Nothing')
    
    @property
    def use_skills(self) -> str:
        return self.json_data.get('use-skills', 'Use skills')

    @property
    def sell(self) -> str:
        return self.json_data.get('sell', 'Sell')
    
    @property
    def buy(self) -> str:
        return self.json_data.get('buy', 'Buy')
    
    @property
    def keep_trading(self) -> str:
        return self.json_data.get('keep-trading', 'Do you want to keep trading?')

    @property
    def few_points_base_skill(self) -> str:
        return self.json_data.get('few-points-base-skill', 'You miss improvement points for {base_skill_name}, you have {points}, you need {base_skill_cost}.')

    @property
    def no_base_skill(self) -> str:
        return self.json_data.get('no-base-skill', 'None')

    @property
    def which_base_skill_learn(self) -> str:
        return self.json_data.get('which-base-skill-learn', 'Which base skill do you want to improve?')

    @property
    def money(self) -> str:
        return self.json_data.get('money', 'money')
    
    @property
    def improvement_points(self) -> str:
        return self.json_data.get('improvement-points', 'improvement points')

    @property
    def not_enough_res_for(self) -> str:
        return self.json_data.get('not-enough-res-for','You do not have enough ressources for the following skills:')
    

    @property
    def nothing_to_learn(self) -> str:
        return self.json_data.get('nothing-to-learn', 'It seems there is nothing for you to learn')

    @property
    def which_skill_learn(self) -> str:
        return self.json_data.get('which-skill-learn', 'Which skill do you want to learn?')
    
    @property
    def which_learning(self) -> str:
        return self.json_data.get('which-learning', 'What do you want to do?')
    
    @property
    def learning_teacher(self) -> str:
        return self.json_data.get('learning-teacher', 'Search for teachers')
    
    @property
    def learning_self(self) -> str:
        return self.json_data.get('learning-self', 'Teach yourself')
    
    @property
    def learned_skill(self) -> str:
        return self.json_data.get('learned-skill', '{hero_name} can now use "{skill_name}".')

    @property
    def who_camps(self) -> str:
        return self.json_data.get('who-camps', 'Who sets up the camp?')
    
    @property
    def camp_who_order(self) -> str:
        return self.json_data.get('camp-who-order', 'Whom do you want to give a task next?')
    
    @property
    def camp_trade(self) -> str:
        return self.json_data.get('camp-trade', 'Trade')
    
    @property
    def camp_heal(self) -> str:
        return self.json_data.get('camp-heal', 'Heal')
    
    @property
    def camp_learn(self) -> str:
        return self.json_data.get('camp-learn', 'Learn')

    @property
    def what_should_hero_do(self) -> str:
        return self.json_data.get('what-should-hero-do', 'What should {hero_name} use?')
    
    @property
    def you_are_in(self) -> str:
        return self.json_data.get('you-are-in', 'You are in {region_name}.')
    
    @property
    def adjacent_regions_prefix(self) -> str:
        return self.json_data.get('adjacent-regions-prefix', 'The adjacent regions are:')
    
    @property
    def no_adjacent_regions(self) -> str:
        return self.json_data.get('no-adjacent-regions', 'The region has no adjacent regions.')

    @property
    def region_option_question(self) -> str:
        return self.json_data.get('region-option-question', 'What do you want to do?')
    
    @property
    def region_option_search(self) -> str:
        return self.json_data.get('region-option-search', 'Search current region')
    
    @property
    def region_option_camp(self) -> str:
        return self.json_data.get('region-option-camp', 'Camp')
    
    @property
    def region_option_travel(self) -> str:
        return self.json_data.get('region-option-travel', 'Change region')
    
    @property
    def round_over(self) -> str:
        return self.json_data.get('round-over', 'Your round is over.')
    
    @property
    def hero_died(self) -> str:
        return self.json_data.get('hero-died', '{hero_name} died.')

    @property
    def skill_no_longer(self) -> str:
        return self.json_data.get('skill-no-longer', '{hero_name} no longer has {skill_name}.')

    @property
    def lost_money(self) -> str:
        return self.json_data.get('lost-money','')

    @property
    def lost_almost_melee(self) -> str:
        return self.json_data.get('lost-almost-melee','')

    @property
    def lost_almost_ranged(self) -> str:
        return self.json_data.get('lost-almost-ranged','')

    @property
    def lost_almost_shield(self) -> str:
        return self.json_data.get('lost-almost-shield','')

    @property
    def lost_almost_armor(self) -> str:
        return self.json_data.get('lost-almost-armor','')

    @property
    def lost_almost_active_item(self) -> str:
        return self.json_data.get('lost-almost-active-item','')

    @property
    def lost_empty_backpack(self) -> str:
        return self.json_data.get('lost-empty-backpack','')

    @property
    def lost_empty_backpack_item(self) -> str:
        return self.json_data.get('lost-empty-backpack-item','')
    
    
    @property
    def lost_melee(self) -> str:
        return self.json_data.get('lost-melee','')

    @property
    def lost_ranged(self) -> str:
        return self.json_data.get('lost-ranged','')

    @property
    def lost_shield(self) -> str:
        return self.json_data.get('lost-shield','')

    @property
    def lost_armor(self) -> str:
        return self.json_data.get('lost-armor','')

    @property
    def lost_active_item(self) -> str:
        return self.json_data.get('lost-active-item','')

    @property
    def lost_backpack_item(self) -> str:
        return self.json_data.get('lost-backpack-item','')

    @property
    def lost_backpack(self) -> str:
        return self.json_data.get('lost-backpack','')

    @property
    def who_gives_money(self) -> str:
        return self.json_data.get('who-gives-money','')

    @property
    def how_much_gives(self) -> str:
        return self.json_data.get('how-much-gives','')

    @property
    def hero_money(self) -> str:
        return self.json_data.get('hero-money','')

    @property
    def melee(self) -> str:
        return self.json_data.get('melee','')

    @property
    def ranged(self) -> str:
        return self.json_data.get('ranged','')

    @property
    def shield(self) -> str:
        return self.json_data.get('shield','')

    @property
    def armor(self) -> str:
        return self.json_data.get('armor','')

    @property
    def active_items(self) -> str:
        return self.json_data.get('active-items','')

    @property
    def backpack_items(self) -> str:
        return self.json_data.get('backpack-items','')

    @property
    def no_item_locations(self) -> str:
        return self.json_data.get('no-item-locations','')

    @property
    def item_source(self) -> str:
        return self.json_data.get('item-source','')

    @property
    def which_item_move(self) -> str:
        return self.json_data.get('which-item-move','')

    @property
    def throw_away(self) -> str:
        return self.json_data.get('throw-away','')

    @property
    def item_target(self) -> str:
        return self.json_data.get('item-target','')

    @property
    def hero_source(self) -> str:
        return self.json_data.get('hero-source','')

    @property
    def hero_target(self) -> str:
        return self.json_data.get('hero-target','')


    @property
    def more_move_from_to(self) -> str:
        return self.json_data.get('more-move-from-to','')

    @property
    def more_move_from_to(self) -> str:
        return self.json_data.get('more-move-from-to','')

    @property
    def more_move(self) -> str:
        return self.json_data.get('more-move','')
    
    @property
    def who_gets(self) -> str:
        return self.json_data.get('who-gets','')
    
    @property
    def money_transfer_count(self) -> str:
        return self.json_data.get('money-transfer-count','')
    
    @property
    def transfer_more_money(self) -> str:
        return self.json_data.get('transfer-more-money','')
    
    @property
    def money_target(self) -> str:
        return self.json_data.get('money-target','')

    @property
    def too_expensive(self) -> str:
        return self.json_data.get('too-expensive','')

    @property
    def which_buy(self) -> str:
        return self.json_data.get('which-buy','')

    @property
    def got_into_back(self) -> str:
        return self.json_data.get('got-into-back','')

    @property
    def nothing_to_sell(self) -> str:
        return self.json_data.get('nothing-to-sell','')
    
    @property
    def which_sell(self) -> str:
        return self.json_data.get('which-sell','')

    @property
    def backpack(self) -> str:
        return self.json_data.get('backpack','backpack')
    
    @property
    def active(self) -> str:
        return self.json_data.get('active','active')

    @property
    def hero_name_question(self) -> str:
        return self.json_data.get('hero-name-question','')

    @property
    def hero_race_question(self) -> str:
        return self.json_data.get('hero-race-question','')

    @property
    def hero_profession_question(self) -> str:
        return self.json_data.get('hero-profession-question','')

    @property
    def company_name_question(self) -> str:
        return self.json_data.get('company-name-question','')

    @property
    def define_four_heros(self) -> str:
        return self.json_data.get('define-four-heros','')

    @property
    def define_hero_number(self) -> str:
        return self.json_data.get('define-hero-number','')

    @property
    def company_start_at(self) -> str:
        return self.json_data.get('company-start-at','')

    @property
    def company_start_at(self) -> str:
        return self.json_data.get('company-start-at','')

    @property
    def company_save_question(self) -> str:
        return self.json_data.get('company-save-question','')

    @property
    def add_hero(self) -> str:
        return self.json_data.get('add-hero','')

    @property
    def select_company(self) -> str:
        return self.json_data.get('select-company','')

    @property
    def new_company(self) -> str:
        return self.json_data.get('new-company','')

    @property
    def existing_company(self) -> str:
        return self.json_data.get('existing-company','')

    @property
    def select_company_file(self) -> str:
        return self.json_data.get('select-company-file','')

    @property
    def you_selected(self) -> str:
        return self.json_data.get('you-selected','')

    @property
    def select_world_settings(self) -> str:
        return self.json_data.get('select-world-settings','')


    @property
    def which_hero_activity(self) -> str:
        return self.json_data.get('which-hero-activity','Which hero should take part in this activity?')


















