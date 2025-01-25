## Week 7 Assignments

# Comma Code
spam = ['apples', 'bananas', 'tofu', 'cats']

def list_to_string(items):
    if not items:  # Check if the list is empty
        return ""
    elif len(items) == 1:  # If the list has only one item, return it as is
        return items[0]
    else:  # Join all items with a comma and a space, and add "and" before the last item
        return ", ".join(items[:-1]) + ", and " + items[-1]

spam = ['apples', 'bananas', 'tofu', 'cats']
empty_list = []
one_item_list = ['apples']

print(list_to_string(spam))  # Output: 'apples, bananas, tofu, and cats'
print(list_to_string(empty_list))  # Output: ''
print(list_to_string(one_item_list))  # Output: 'apples'

# Coin Flip Streaks
import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    # Generate a list of 100 random 'heads' or 'tails'
    coin_flips = [random.choice(['H', 'T']) for _ in range(100)]

    # Check for a streak of 6 heads or tails in a row
    streak = 1  # Current streak count
    for i in range(1, len(coin_flips)):
        if coin_flips[i] == coin_flips[i - 1]:  # Check if the current flip matches the previous one
            streak += 1
            if streak == 6:  # A streak of 6 found
                numberOfStreaks += 1
                break  # Stop checking further for this experiment
        else:
            streak = 1  # Reset streak count if sequence breaks

print('Chance of streak: %s%%' % (numberOfStreaks / 100))

# Back to The Dungeon
# Fantasy Game Inventory
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for item, count in inventory.items():
        print(f"{count} {item}")
        item_total += count  # Add the count of each item to the total
    print("Total number of items: " + str(item_total))

displayInventory(stuff)

# List to Dictionary Function For Fantasy Game
def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory[item] = inventory.get(item, 0) + 1  # Add 1 to the item count, defaulting to 0 if it doesn't exist
    return inventory

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for item, count in inventory.items():
        print(f"{count} {item}")
        item_total += count
    print("Total number of items: " + str(item_total))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot)

displayInventory(inv)


