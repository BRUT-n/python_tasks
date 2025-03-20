"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for item in items_to_add:
        current_cart.setdefault(item, 0)
        current_cart[item] += 1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    list_of_notes = {}
    for note in notes:
        list_of_notes.setdefault(note, 1)
    return list_of_notes


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    # fulfillment_cart = dict(sorted({}.items())) 
    fulfillment_cart = {}
    
    for item in cart.keys():
        value = cart[item]
        aisle_and_refrigeration = aisle_mapping[item]
        fulfillment_cart[item] = [value, *aisle_and_refrigeration]

    return dict(sorted(fulfillment_cart.items(), reverse=True))



def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for item, value in fulfillment_cart.items():
        cart_count = fulfillment_cart[item][0]
        store_count = store_inventory[item][0]
        result_count = store_count - cart_count
        if result_count == 0:
            result_count = "Out of Stock"
        store_inventory[item][0] = result_count
    return store_inventory



#testing

# #task_1
# print(add_item({'Banana': 3, 'Apple': 2, 'Orange': 1}, ('Apple', 'Apple', 'Orange', 'Apple', 'Banana')))
# # {'Banana': 4, 'Apple': 5, 'Orange': 2}
# print(add_item({'Banana': 3, 'Apple': 2, 'Orange': 1}, ['Banana', 'Orange', 'Blueberries', 'Banana']))
# # {'Banana': 5, 'Apple': 2, 'Orange': 2, 'Blueberries': 1}


# #task_2
# print(read_notes(('Banana','Apple', 'Orange')))
# # {'Banana': 1, 'Apple': 1, 'Orange': 1}
# print(read_notes(['Blueberries', 'Pear', 'Orange', 'Banana', 'Apple']))
# # {'Blueberries' : 1, 'Pear' : 1, 'Orange' : 1, 'Banana' : 1, 'Apple' : 1}


# #task_3
# print(update_recipes({'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
#                     'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}},
# (('Banana Bread', {'Banana': 4,  'Walnuts': 2, 'Flour': 1, 'Butter': 1, 'Milk': 2, 'Eggs': 3}),)))
# ...

# # {'Banana Bread' : {'Banana': 4,  'Apple': 1, 'Walnuts': 2, 'Flour': 1, 'Butter': 1, 'Milk': 2, 'Eggs': 3},
# #  'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}}

# # task_4
# print(sort_entries({'Banana': 3, 'Apple': 2, 'Orange': 1}))
# # {'Apple': 2, 'Banana':3, 'Orange': 1}


# task_5
# print(send_to_store({'Banana': 3, 'Apple': 2, 'Orange': 1, 'Milk': 2},
#                   {'Banana': ['Aisle 5', False], 'Apple': ['Aisle 4', False], 'Orange': ['Aisle 4', False], 'Milk': ['Aisle 2', True]}))
# {'Orange': [1, 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True], 'Banana': [3, 'Aisle 5', False], 'Apple': [2, 'Aisle 4', False]}


# # task_6
# print(update_store_inventory({'Orange': [1, 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True], 'Banana': [3, 'Aisle 5', False], 'Apple': [2, 'Aisle 4', False]},
# {'Banana': [15, 'Aisle 5', False], 'Apple': [12, 'Aisle 4', False], 'Orange': [1, 'Aisle 4', False], 'Milk': [4, 'Aisle 2', True]}))

# # {'Banana': [12, 'Aisle 5', False], 'Apple': [10, 'Aisle 4', False], 'Orange': ['Out of Stock', 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True]}