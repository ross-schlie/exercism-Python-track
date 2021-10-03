"""exercism inventory management (dicts) module."""


def create_inventory(items):
    """
    Create a dictionary from a list.

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """

    inventory = {}
    for item in items:
        if inventory.get(item) is None:
            inventory[item] = 1
        else:
            inventory[item] += 1

    return inventory


def add_items(inventory, items):
    """
    Update inventory, adding from a list of items.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """

    for item in items:
        if inventory.get(item) is None:
            inventory[item] = 1
        else:
            inventory[item] += 1

    return inventory


def decrement_items(inventory, items):
    """
    Update inventory, removing items in list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """

    for item in items:
        if inventory.get(item) is not None and inventory.get(item) > 0:
            inventory[item] -= 1

    return inventory


def remove_item(inventory, item):
    """
    Remove an item from inventory.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """

    if inventory.get(item) is not None:
        inventory.pop(item)

    return inventory


def list_inventory(inventory):
    """
    List out inventory (items > 0).

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    inventory_list = []
    # alternatly, use popitem and check value finaly reverse list
    for item in inventory:
        if inventory[item] != 0:
            inventory_list.append(tuple([item, inventory[item]]))

    return inventory_list
