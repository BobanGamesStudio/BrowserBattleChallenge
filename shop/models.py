from inventory.constant_item_creator import create_constant_item

import math

def sell_player_item(player_inventory, player_currencies, item_id):
    item = player_inventory.get_item_by_id(item_id)

    stackable = False
    if 'stackable' in item:
        if item['stackable'] == True:
            stackable = True

    if stackable:
        item_price = item['price'] * item['number']
    else:
        item_price = item['price']

    gold_received = math.ceil(item_price / 2)
    
    player_inventory.delete_item_from_inventory(item_id)

    player_currencies.add_gold(gold_received)
 
    return gold_received

def get_products_data():
    SmallLifePotion = create_constant_item('small life potion')
    MediumLifePotion = create_constant_item('medium life potion')
    BigLifePotion = create_constant_item('big life potion')

    products = [SmallLifePotion, MediumLifePotion, BigLifePotion]

    return products

def buy_item(player_inventory, player_currencies, item_name):
    items_for_sell = get_products_data()

    for item_for_sale in items_for_sell:
        if item_for_sale['name'] == item_name:
            if player_currencies.get_gold() >= item_for_sale['price']:
                item_added = player_inventory.add_new_item_to_inventory(item_for_sale)

                if item_added:
                    player_currencies.subtract_gold(item_for_sale['price'])

                    return item_for_sale['price']
    return False
