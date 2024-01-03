from tungeon.config.game_config import game_config
from tungeon.config.schema.item import Item

def get_item(item_name:str) -> Item:
    for item in game_config().items:
        if item.name == item_name:
            return item
    raise ValueError(f'Item {item_name} not found')