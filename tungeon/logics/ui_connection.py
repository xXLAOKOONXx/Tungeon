from typing import Callable
from tungeon.config.schema.functionality import Functionality
from tungeon.config.schema.item import Item
from tungeon.data.hero import Hero

_skillcheck_dialog = None
_use_destroyable_item_dialog = None
_functionality_used_dialog = None


def set_skillcheck_dialog(func:Callable[[Hero], bool]):
    global _skillcheck_dialog
    _skillcheck_dialog = func

def get_skillcheck_dialog() -> Callable[[Hero], bool] | None:
    return _skillcheck_dialog

def set_use_destroyable_item_dialog(func:Callable[[Hero, Item], bool]):
    global _use_destroyable_item_dialog
    _use_destroyable_item_dialog = func

def get_use_destroyable_item_dialog() -> Callable[[Hero, Item], bool]:
    return _use_destroyable_item_dialog

def set_functionality_used_dialog(func:Callable[[Functionality], None]):
    global _functionality_used_dialog
    _functionality_used_dialog = func

def get_functionality_used_dialog() -> Callable[[Functionality], None]:
    return _functionality_used_dialog