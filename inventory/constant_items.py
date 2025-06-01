# INVENTORY_BAG_WIDTH  = 8
# INVENTORY_BAG_HEIGHT = 10

ALL_ITEMS_TYPES = ['consumable']

ALL_ITEMS_SIZES = {
    '1_1': (1, 1),
    '1_2': (1, 2),
    '1_3': (1, 3),
    '2_1': (2, 1),
    '2_2': (2, 2),
    '2_3': (2, 3),
    '3_1': (3, 1),
    '3_2': (3, 2),
    '3_3': (3, 3)
}

# {'type': 'consumable', 'name': 'meat', 'image': 'Images/Items/Consumable/Meat.png', 'effects': {'heal': 5}, 'price': 10}
ITEMS_CONSUMABLE_STATS = {
    'meat' : {'name': 'meat',
              'type': 'consumable',

              'effects': {'heal': 5}, 
              'size': '1_1', 
              
              'stackable': True, 
              'number': 1, 
              'max_number': 10, 

              'price': 10,
              
              'image': 'Images/Items/Consumable/Meat.png'},
    'small life potion' : {'name': 'small life potion',
                           'type': 'consumable',

                           'effects': {'heal': 10}, 
                           'size': '1_2', 
                           
                           'stackable': False, 

                           'price': 80,
                           
                           'image': 'Images/Items/Consumable/SmallLifePotion.png'},
    'medium life potion' : {'name': 'medium life potion',
                           'type': 'consumable',

                           'effects': {'heal': 25}, 
                           'size': '1_2', 
                           
                           'stackable': False, 

                           'price': 200,
                           
                           'image': 'Images/Items/Consumable/MediumLifePotion.png'},
    'big life potion' : {'name': 'big life potion',
                           'type': 'consumable',

                           'effects': {'heal': 50}, 
                           'size': '1_2', 
                           
                           'stackable': False, 

                           'price': 400,
                           
                           'image': 'Images/Items/Consumable/BigLifePotion.png'},
}

