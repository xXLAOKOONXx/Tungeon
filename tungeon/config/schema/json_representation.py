

class JSONRepresentation:
    '''
    Representation of a JSON object
    '''

    def __init__(self, json_data:dict) -> None:
        self.json_data = json_data

class NamedJSONRepresentation(JSONRepresentation):
    '''
    Representation of a JSON object that comes with a name and display-name attribute    
    '''
    def __init__(self, json_data: dict) -> None:
        super().__init__(json_data)

    @property
    def name(self) -> str | None:
        '''
        name of element
        used in other places to reference this object
        '''
        return self.json_data.get('name')

    @property
    def display_name(self) -> str | None:
        '''
        name to be displayed to users
        '''
        return self.json_data.get('display-name')