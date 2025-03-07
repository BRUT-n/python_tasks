"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    done_dict = {}
    for item in items:
        done_dict.setdefault(item, items.count(item))
    return done_dict



def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory
        


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    for item in items:
        if item in inventory:
            if inventory[item] > 0:
                inventory[item] -= 1
            else:
                inventory[item] = 0
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    pass


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    pass





print(add_items({"coal":1}, ["wood", "iron", "coal", "wood"]))
# {"coal":2, "wood":2, "iron":1}


print(add_items({"coal":1}, ["wood", "iron", "coal", "wood"]))
# {"coal":2, "wood":2, "iron":1}

print(decrement_items({"coal":2, "wood":1, "diamond":2}, ["coal", "coal", "wood", "wood", "diamond"]))
# {"coal":0, "wood":0, "diamond":1}


print(remove_item({"coal":2, "wood":1, "diamond":2}, "coal"))
# {"wood":1, "diamond":2}

print(remove_item({"coal":2, "wood":1, "diamond":2}, "gold"))
# {"coal":2, "wood":1, "diamond":2}


print(list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}))
# [('coal', 7), ('diamond', 2), ('iron', 7), ('wood', 11)]