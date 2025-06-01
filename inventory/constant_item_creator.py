from .constant_items import ITEMS_CONSUMABLE_STATS
import copy

def CustomTitle(item_name):
    return ' '.join(word.capitalize() if not word.startswith("'") else word for word in item_name.split())

def FindItem(itemName):
    if itemName in ITEMS_CONSUMABLE_STATS:
        foundItem = copy.deepcopy(ITEMS_CONSUMABLE_STATS[itemName])
        return foundItem

def create_constant_item(item_name):
    new_item = FindItem(item_name)
    new_item['name'] = CustomTitle(item_name)

    return new_item