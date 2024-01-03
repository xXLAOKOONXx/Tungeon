from tungeon.config.schema.functionality import Functionality
from tungeon.config.schema.json_representation import NamedJSONRepresentation


class Item(NamedJSONRepresentation):
    '''representation of an item that is defined in config files'''
    def __init__(self, json_data: dict) -> None:
        super().__init__(json_data)

    @property
    def is_weapon(self) -> bool:
        '''
        Flag whether item is a weapon or not, defaults to False
        '''
        return self.json_data.get('is-weapon', False)

    @property
    def is_melee(self) -> bool:
        '''
        Flag whether item is used in melee or not, defaults to False
        Main usage is for weapons
        '''
        return self.json_data.get('is-melee', False)

    @property
    def is_ranged(self) -> bool:
        '''
        Flag whether item is used in ranged or not, defaults to False
        Main usage is for weapons        
        '''
        return self.json_data.get('is-ranged', False)

    @property
    def is_shield(self) -> bool:
        '''
        Flag whether the item is a shield or not, defaults to False
        '''
        return self.json_data.get('is-shield', False)

    @property
    def is_armor(self) -> bool:
        '''
        Flag whether the item is an armor or not, defaults to False
        '''
        return self.json_data.get('is-armor', False)

    @property
    def money_value(self) -> int | None:
        '''
        prize for the item to pay under normal conditions
        can be None, eg on unique items that you would not be able to sell or buy
        '''
        return self.json_data.get('money-value')

    @property
    def damage(self) -> int | None:
        '''
        damage the item provides, only relevant for weapons
        '''
        return self.json_data.get('damage')

    @property
    def resistance(self) -> int | None:
        '''
        resistance an item provides, mostly relevant for shield and armor
        '''
        return self.json_data.get('resistance')

    @property
    def required_hands(self) -> int | None:
        '''
        hands required to use an item
        relevant for weapons only,
        determines whether user has a free hand for a shield
        '''
        return self.json_data.get('required-hands')
    
    @property
    def functions(self) -> list[Functionality]:
        funcs = [Functionality(func) for func in self.json_data.get('functions')]
        for func in funcs:
            func.display_name = self.display_name
        return funcs