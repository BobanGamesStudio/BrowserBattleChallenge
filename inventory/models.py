from hero_stats.models import HeroStats
from django.db import models
from django.contrib.auth.models import User
from .inventory_types import ALL_ITEMS_SIZES_EQUIPMENT, INVENTORY_BAG_WIDTH, INVENTORY_BAG_HEIGHT, ALL_ITEMS_TYPES
from .constant_items import ALL_ITEMS_SIZES
# from hero_stats.models import HeroStats
import copy

def default_accumulated_stats():
    return {
        "max_health": 0,

        'min_physical_dmg': 0,
        'max_physical_dmg': 0,

        "armor": 0,
        "speed": 0,

        "strength": 0,
        "agility": 0,
        "intelligence": 0,

        "armor_percent": 0,
        "damage_percent": 0,
        "health_percent": 0,
    }

def default_inventory_slot_value():
    return -1  # You can set the default number here

class PlayerInventory(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.JSONField(default=dict)
    inventory_grid = models.JSONField(default=list)
    next_item_id = models.PositiveIntegerField(default=1)

    weapon_left  = models.JSONField(default=default_inventory_slot_value)
    weapon_right = models.JSONField(default=default_inventory_slot_value)
    body_armor   = models.JSONField(default=default_inventory_slot_value)
    gloves       = models.JSONField(default=default_inventory_slot_value)
    boots        = models.JSONField(default=default_inventory_slot_value)
    helmet       = models.JSONField(default=default_inventory_slot_value)
    belt         = models.JSONField(default=default_inventory_slot_value)
    amulet       = models.JSONField(default=default_inventory_slot_value)
    ring_left    = models.JSONField(default=default_inventory_slot_value)
    ring_right   = models.JSONField(default=default_inventory_slot_value)

    slot_fields_names = [
        'weapon_left',
        'weapon_right',
        'body_armor',
        'gloves',
        'boots',
        'helmet',
        'belt',
        'amulet',
        'ring_left',
        'ring_right',
    ]

    accumulated_stats = models.JSONField(default=default_accumulated_stats)

    class Meta:
        db_table = 'inventory'

    def __str__(self):
        return self.user.username + ' inventory.'

    def get_and_increment_next_item_id(self):
        """
        Get the current value of next_item_id and increment it by one.
        """
        current_id = self.next_item_id
        self.next_item_id += 1
        self.save()
        
        return int(current_id)

    def initialize_inventory_grid(self):
        """Initialize the inventory grid as an 8x10 grid of None values."""
        
        self.inventory_grid = [[None for _ in range(8)] for _ in range(10)]
        self.save()

    def get_accumulated_stats(self):
        return copy.deepcopy(self.accumulated_stats)

    def update_hero_inventory_stats(self):
        from hero_stats.models import HeroStats

        accumulated_stats = default_accumulated_stats () 

        for slot_field in self.slot_fields_names:
            slot_item_id = getattr(self, slot_field)
            if slot_item_id != -1:
                sloted_item = self.items[str(slot_item_id)]

                if "base_stats" in sloted_item:
                    for base_stat_name, base_stat_data in sloted_item["base_stats"].items():
                        if base_stat_data["stat_type"] == "double_value":
                            if base_stat_name == "physical_damage":
                                accumulated_stats['min_physical_dmg'] += base_stat_data["low_value"]
                                accumulated_stats['max_physical_dmg'] += base_stat_data["high_value"]
                        elif base_stat_data["stat_type"] == "single_value_int":
                            if base_stat_name == "armor":
                                accumulated_stats['armor'] += base_stat_data["value"]
                            elif base_stat_name == "strength":
                                accumulated_stats['strength'] += base_stat_data["value"]
                            elif base_stat_name == "agility":
                                accumulated_stats['agility'] += base_stat_data["value"]
                            elif base_stat_name == "intelligence":
                                accumulated_stats['intelligence'] += base_stat_data["value"]
                            elif base_stat_name == "all_attributes":
                                accumulated_stats['strength'] += base_stat_data["value"]
                                accumulated_stats['agility'] += base_stat_data["value"]
                                accumulated_stats['intelligence'] += base_stat_data["value"]

                        elif base_stat_data["stat_type"] == "single_value_float":
                            if base_stat_name == "speed":
                                accumulated_stats['speed'] += base_stat_data["value"]
                            
                            elif base_stat_name == "armor_percent":
                                accumulated_stats['armor_percent'] += base_stat_data["value"]
                            elif base_stat_name == "physical_damage_percent":
                                accumulated_stats['damage_percent'] += base_stat_data["value"]
                            elif base_stat_name == "health_percent":
                                accumulated_stats['health_percent'] += base_stat_data["value"]

        self.accumulated_stats = accumulated_stats
        self.save()

        hero_stats = HeroStats.objects.get(user=self.user)
        hero_stats.update_current_stats()

    def if_item_exists(self, item_id):
        if str(item_id) in self.items:
            return True
        else:
            print("Item does not exist")
            return False

    def get_item_by_id(self, item_id):
        return self.items[str(item_id)]

    def get_items_by_name(self, item_name):
        found_items = []
        for itemId, itemInfo in self.items.items():
            if itemInfo['name'] == item_name:
                found_items.append(self.items[itemId])
        if len(found_items) > 0:
            return found_items
        else:
            return False

    def get_item_type(self, item_id):
        if self.if_item_exists(item_id):
            return self.get_item_by_id(item_id)['type']


    def get_item_size_by_item(self, item):
        return ALL_ITEMS_SIZES.get(item['size'])
    
    def get_item_size_by_id(self, item_id):
        if self.if_item_exists(item_id):
            item = self.get_item_by_id(item_id)

            return self.get_item_size_by_item(item)
        
        return False
    

    def is_item_stackable(self, item):
        if 'stackable' in item:
            if item['stackable'] == True:
                return True
            
        return False

    def is_space_available(self, item_size):
        """
        Check if there is available space for an item of the given type in the inventory.
        """
        # Check if the item type is valid and get its size
        inventory_grid = self.inventory_grid

        # Check if there is space for the new item
        for row in range(10):
            for col in range(8):
                if inventory_grid[row][col] is None:
                    # Check if the entire item size can fit starting from this position
                    for i in range(item_size[0]):
                        for j in range(item_size[1]):
                            if (
                                col + i >= 8
                                or row + j >= 10
                                or inventory_grid[row + j][col + i] is not None
                            ):
                                break
                        else:
                            continue
                        break
                    else:
                        return (col, row)  # Return the position where the item can fit

        return False
    
    def find_item_position_on_grid(self, item_id):
        """
        Find the current position of an item on the inventory grid.

        Args:
            item_id (int): The ID of the item to locate on the grid.

        Returns:
            tuple: A tuple containing the (column, row) coordinates of the item's position on the grid,
                or False if the item is not found on the grid.
        """
        if self.if_item_exists(item_id):
            # Initialize current_position as None
            current_position = None

            # Iterate through the rows and columns of the inventory grid
            for row in range(INVENTORY_BAG_HEIGHT):
                for col in range(INVENTORY_BAG_WIDTH):
                    # Check if the current cell contains the item_id
                    if self.inventory_grid[row][col] == int(item_id):
                        # Set current_position to the (col, row) coordinates
                        current_position = (col, row)
                        break
                # If current_position is set, break out of the outer loop
                if current_position:
                    break

            # Check if the item was found on the grid
            if current_position:
                return current_position
            else:
                return False  # Item not found on the grid

    def find_the_item_occupied_slot(self, item_id):
        if self.if_item_exists(item_id):
            # Iterate through the slot fields and check if any of them contain the item_id
            for slot_field in self.slot_fields_names:
                slot_item_id = getattr(self, slot_field)
                if slot_item_id == int(item_id):
                    return slot_field

            # If item_id is not found in any slot, return None
            return False

    def place_item_on_inventory_grid(self, item_id):
        """
        Place the item on the player's inventory grid.
        """
        if self.if_item_exists(item_id):
            item_size          = self.get_item_size_by_id(item_id)
            available_position = self.is_space_available(item_size)

            if available_position != False:
                column = available_position[0]
                row    = available_position[1]

                # Place the item in the grid
                for i in range(item_size[0]):
                    for j in range(item_size[1]):
                        self.inventory_grid[row + j][column + i] = int(item_id)

                self.save()

                return True
            return False
    
    def remove_item_from_inventory_grid(self, item_id):
        if self.if_item_exists(item_id):
            # Find the current position of the item
            current_position = self.find_item_position_on_grid(item_id)
            item_size        = self.get_item_size_by_id(item_id)
            
            # Clear the current position of the item in the grid
            for i in range(item_size[0]):
                for j in range(item_size[1]):
                    self.inventory_grid[current_position[1] + j][current_position[0] + i] = None
            
            self.save()

    def add_new_item_to_inventory(self, item):
        """
        Add given item to the player's inventory if there is available space.
        """
        # self.inventory_grid[0][0] = 145
        if self.is_item_stackable(item):
            foundStacks = self.get_items_by_name(item['name'])
            maxStackSize = item['max_number']

            if foundStacks != False:
                for stack in foundStacks:
                    if stack['number'] < maxStackSize:
                        howManyCanBeAdded = min(item['number'], maxStackSize - stack['number'])

                        item['number'] -= howManyCanBeAdded
                        stack['number'] += howManyCanBeAdded

                        if item['number'] == 0:
                            self.save()
                            return True

        item_size = self.get_item_size_by_item(item)

        available_position = self.is_space_available(item_size)
        if available_position != False:
            item_id             = self.get_and_increment_next_item_id()
            self.items[str(item_id)] = item
            
            self.place_item_on_inventory_grid(item_id)

            self.save()

            return True
        else:
            return False

    def move_item(self, item_id, new_position):
        """
        Move an item to a new position in the player's inventory grid.
        """
        if self.if_item_exists(item_id):
            item_position = self.find_item_position_on_grid(item_id)
            if item_position != False:
                self.remove_item_from_inventory_grid(item_id)
            else:
                self.remove_item_from_slot(item_id)
                
            item_size = self.get_item_size_by_id(item_id)

            # Calculate the positions where the item will be placed
            new_col = new_position['col']
            new_row = new_position['row']
            positions_to_check = []
            for i in range(item_size[0]):
                for j in range(item_size[1]):
                    positions_to_check.append((new_col + i, new_row + j))
                    
            for col, row in positions_to_check:
                if (
                    col < 0
                    or col >= INVENTORY_BAG_WIDTH
                    or row < 0
                    or row >= INVENTORY_BAG_HEIGHT
                    or (
                        self.inventory_grid[row][col] is not None
                        and self.inventory_grid[row][col] != item_id
                    )
                ):
                    raise ValueError("Invalid or occupied position")

            # Place the item in the new position
            for i in range(item_size[0]):
                for j in range(item_size[1]):
                    self.inventory_grid[new_row + j][new_col + i] = int(item_id)

            self.save()
 
    def check_if_slot_free(self, item_type, ring_side):
        if item_type != 'ring':
            equipped_item_id = getattr(self, item_type)
            if equipped_item_id != -1:
                return False, item_type, equipped_item_id
            else:
                return True, item_type, None
        else:
            if self.ring_left == -1:
                return True, 'ring_left', None
            elif self.ring_right == -1:
                return True, 'ring_right', None
            elif ring_side == 'left':
                return False, 'ring_left', self.ring_left
            elif ring_side == 'right':
                return False, 'ring_right', self.ring_right

    def put_item_in_slot(self, item_id, item_type, drop_side):
        # if self.if_item_exists(item_id):
        is_slot_free, checked_slot, checked_item_id = self.check_if_slot_free(item_type, drop_side)

        if not is_slot_free:
            if item_id == checked_item_id:
                return False

        setattr(self, checked_slot, item_id)
        self.remove_item_from_inventory_grid(item_id)

        if not is_slot_free:
            self.place_item_on_inventory_grid(checked_item_id)

        self.save()
        self.update_hero_inventory_stats()
        
        return True

    def remove_item_from_slot(self, item_id):
        # if self.if_item_exists(item_id):
        item_slot = self.find_the_item_occupied_slot(item_id)
        setattr(self, item_slot, -1)
        self.update_hero_inventory_stats()


    def use_item(self, item_id, drop_side):
        if self.if_item_exists(item_id):
            item = self.items[str(item_id)]
            item_type = item['type']

            if item_type in ALL_ITEMS_TYPES: # Wear item
                self.put_item_in_slot(item_id, item_type, drop_side)
                return 'gear'
            elif item_type == 'consumable':
                self.consume_item(item_id)
                return 'consumable'
            else:
                print(f"Wrong item type: {item_type}")

    def consume_item(self, item_id):
        item = self.get_item_by_id(item_id)
        for effect_name, effect_data in item['effects'].items():
            if effect_name == 'heal':
                user_id = getattr(self, 'user').id
                hero_stats_model = HeroStats.objects.get(user_id=user_id)
                hero_stats_model.increment_stats({'current_health': effect_data})
        
        if self.is_item_stackable(item):
            if item['number'] > 1:
                item['number'] -= 1
            else:
                self.delete_item_from_inventory(item_id)
        else:
            self.delete_item_from_inventory(item_id)
        
        self.save()

    def delete_item_from_inventory(self, item_id):
        item_id = str(item_id)
        if self.if_item_exists(item_id):
            if self.find_item_position_on_grid(item_id) != False: # item is on grid
                self.remove_item_from_inventory_grid(item_id)
                del self.items[item_id]

            elif self.find_the_item_occupied_slot(item_id) != False: # item is at 
                self.remove_item_from_slot(item_id)
                del self.items[item_id]
                
            self.save()
