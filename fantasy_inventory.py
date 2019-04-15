# You are creating a fantasy video game. The data structure to model the player’s inventory will be a dictionary where
# the keys are string values describing the item in the inventory and the value is an integer value detailing how many
# of that item the player has. For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1,
# 'arrow': 12} means the player has 1 rope, 6 torches, 42 gold coins, and so on.
#
# Write a function named displayInventory() that would take any possible “inventory” and display it like the following:
#
#
# Inventory:
# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch
# 1 dagger
# Total number of items: 62


example_inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):
    total_items = 0
    print('\nInventory: ')
    for key, value in inventory.items():
        print(str(value), key)
        total_items += value
    print('\nTotal number of items:')
    return total_items


print(display_inventory(example_inventory))


##############################################
##############################################

# Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary
# representing the player’s inventory (like in the previous project) and the addedItems parameter is a list like
# dragon_loot. The addToInventory() function should return a dictionary that represents the updated inventory. Note
# that the addedItems list can contain multiples of the same item.

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def add_to_inventory(inventory, added_items):
    updated_inventory = {}
    updated_inventory.update(inventory)
    for item in added_items:
        for key, value in inventory.items():
            if item == key:
                updated_inventory[key] += 1
            elif item not in inventory:
                updated_inventory.update({item: 1})
    return updated_inventory


example_inventory = add_to_inventory(example_inventory, dragon_loot)

print(display_inventory(example_inventory))

