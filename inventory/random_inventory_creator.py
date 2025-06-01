import random
import math
from .inventory_types import ALL_ITEMS_DROP_CHANCES, ITEMS_POSSIBLE_BASE_STATS, ITEMS_POSSIBLE_VARIANTS, ALL_ITEMS_VARIANTS_DROP_CHANCES, ALL_ITEMS_SIZES_EQUIPMENT

def gaussian_distribution(x, peak_point, standard_deviation):
    """
    Compute the value of a Gaussian distribution function.

    Parameters:
    - x: The variable (unknown) for which you want to calculate the function value.
    - peak_point: The point at which the function reaches its maximum value.
    - standard_deviation: The standard deviation, which controls the width of the curve.

    Returns:
    - The function value at point x.

    Note: The function value is between 0 and 1, with the maximum value (1) occurring at the peak_point.
    """
    if standard_deviation <= 0:
        raise ValueError("Standard deviation must be greater than zero.")

    exponent = -((x - peak_point) ** 2) / (2 * (standard_deviation ** 2))

    return math.exp(exponent)

def prepare_variants_for_level(all_possibilities, item_level):
    possibilities_at_lvl = {}

    for variant_name, variant_data in all_possibilities.items():
        if variant_data["level_required"] <= item_level:
            gaussian_value = gaussian_distribution(item_level, variant_data["peak_lvl_point"], variant_data["standard_deviation"])
            possibilities_at_lvl[variant_name] = max(round(variant_data["max_chance"] * (gaussian_value)), 10)
    
    return possibilities_at_lvl

def weighted_random_selection(all_possibilities):
    """
    Selects an item from a collection of items with probabilities proportional to their assigned weights.

    Parameters:
    - chances (dict): A dictionary where keys represent items and values represent their respective weights or chances.

    Returns:
    - item: The selected item based on the weighted random selection.

    Description:
    This function takes a dictionary of items and their associated weights (or chances). The weights should be positive integers.
    It calculates the total sum of all weights and generates a random number between 1 and the total sum.
    Then, it iterates through the items and checks if the random number falls within the cumulative chance range for each item.
    The item whose chance range includes the random number is selected and returned.
    The function allows you to perform a weighted random selection, where items with higher weights have a greater likelihood of being chosen.
    """

    # Calculate the total sum of chances
    total_chances = sum(all_possibilities.values())
    
    # Generate a random number between 0 and the total chances
    # print(total_chances)
    # print("ERROR!!!!: ", total_chances)
    random_num = random.randint(1, total_chances)

    # Iterate through the items and check if the random number falls within the chance range
    cumulative_chance = 0
    for item, chance in all_possibilities.items():
        cumulative_chance += chance
        if random_num <= cumulative_chance:
            return item

def CustomTitle(item_name):
    return ' '.join(word.capitalize() if not word.startswith("'") else word for word in item_name.split())


def create_random_item(item_level):
    """
    Create a random item and add it to the player's inventory if there is available space.
    """

    new_item = {}
    possibilities_at_lvl = {} 
    while len(possibilities_at_lvl) == 0:
        new_item['type'] = weighted_random_selection(ALL_ITEMS_DROP_CHANCES)
        new_item['size'] = ALL_ITEMS_SIZES_EQUIPMENT[new_item['type']]
        # new_item['type']     = random.choice(['belt'])
        possibilities_at_lvl = prepare_variants_for_level(ALL_ITEMS_VARIANTS_DROP_CHANCES[new_item['type']], item_level)
    new_item['variant']  = weighted_random_selection(possibilities_at_lvl)
    new_item['name']     = CustomTitle(new_item['variant'])
    new_item['image']    = ITEMS_POSSIBLE_VARIANTS[new_item['type']][new_item['variant']]['image_path']

    if new_item['variant'] in ITEMS_POSSIBLE_BASE_STATS[new_item['type']]:
        new_item['base_stats'] = {}
        
        for stat_name, stat_data in ITEMS_POSSIBLE_BASE_STATS[new_item['type']][new_item['variant']].items():
            if stat_data['stat_type'] == 'double_value':
                low_value  = random.randint(stat_data['min_low_value'](item_level), stat_data['max_low_value'](item_level))
                high_value = random.randint(stat_data['min_high_value'](item_level), stat_data['max_high_value'](item_level))

                new_item['base_stats'][stat_name] = { "stat_type" : 'double_value', "low_value" : low_value, 'high_value' : high_value }
            
            if stat_data['stat_type'] == 'single_value_int':
                # print("WWWWWWWWWWWW ", stat_name, stat_data['min_value'](item_level), stat_data['max_value'](item_level))
                value = random.randint(stat_data['min_value'](item_level), stat_data['max_value'](item_level))

                new_item['base_stats'][stat_name] = { "stat_type" : 'single_value_int', "value" : value }
            
            if stat_data['stat_type'] == 'single_value_float':
                value = random.uniform(stat_data['min_value'](item_level), stat_data['max_value'](item_level))
                value = round(value, 2)

                new_item['base_stats'][stat_name] = { "stat_type" : 'single_value_float', "value" : value }

    new_item['price'] = item_level * random.randint(1, 10)

    return new_item
