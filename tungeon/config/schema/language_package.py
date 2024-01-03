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
        return self.json_data.get('wanna-prep', 'Do yo uwant to perform some preperation?')
    
    