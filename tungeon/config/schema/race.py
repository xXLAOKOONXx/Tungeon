

class Race:
    '''
    Base Information for a race
    '''

    def __init__(self, json_data:dict) -> None:
        self.json_data = json_data

    @property
    def name(self) -> int:
        return self.json_data['name']

    @property
    def isplay_name(self) -> int:
        return self.json_data['display-name']

    @property
    def speed_base(self) -> int:
        return self.json_data['speed-base']

    @property
    def strength_base(self) -> int:
        return self.json_data['strength-base']

    @property
    def agility_base(self) -> int:
        return self.json_data['agility-base']

    @property
    def intelligence_base(self) -> int:
        return self.json_data['intelligence-base']

    @property
    def speed_upgrades(self) -> dict[int,int]:
        '''
        keys: value to upgrade to
        value: cost of upgrade
        '''
        return {int(key):self.json_data['speed-upgrades'][key] for key in self.json_data['speed-upgrades'].keys()}

    @property
    def strength_upgrades(self) -> dict[int,int]:
        '''
        keys: value to upgrade to
        value: cost of upgrade
        '''
        return {int(key):self.json_data['strength-upgrades'][key] for key in self.json_data['strength-upgrades'].keys()}

    @property
    def agility_upgrades(self) -> dict[int,int]:
        '''
        keys: value to upgrade to
        value: cost of upgrade
        '''
        return {int(key):self.json_data['agility-upgrades'][key] for key in self.json_data['agility-upgrades'].keys()}

    @property
    def intelligence_upgrades(self) -> dict[int,int]:
        '''
        keys: value to upgrade to
        value: cost of upgrade
        '''
        return {int(key):self.json_data['intelligence-upgrades'][key] for key in self.json_data['intelligence-upgrades'].keys()}
    
    @property
    def origin_regions(self) -> list[str]:
        '''
        Regions the race comes from
        '''
        return self.json_data['origin-regions']
    
    @property
    def additional_regionslots(self) -> int:
        '''
        Amount of additional slots available for regions
        '''
        return self.json_data['additional-regionslots']

