# Create a dictionary to define items on our menu with their respective keys and values.
menu = {
    "Margherita Pizza": "A classic pizza with fresh mozzarella, tomatoes, basil, and a drizzle of olive oil.",
    "Pepperoni": "A delicious pizza topped with spicy pepperoni and melted mozzarella cheese.",
    "Ham Pizza": "A freshly baked classic pizza with tomato sauce, mozzarella cheese, and large slices of ham.",
    "Hawaiian": "A tropical combination of ham, pineapple, and mozzarella cheese.",
    "Cheesy Garlic Bread": "Freshly baked bread topped with melted butter and garlic.",
    "Lava Cake": "Our signature chocolate cake with a melted chocolate center, perfect for birthdays and events!"
}

# Create a function that defines the pizza descriptions
# Create an unknown_menu_item so that when the user trys to check an item that is not on the menu, we can return that message
unknown_menu_item = "We apologize, that item is not on the menu!"

def get_menu_descriptions(menu, item_name):
    return menu.get(item_name, unknown_menu_item)

# Checks to see if our function works
# print(get_menu_descriptions(menu, "Mac & Cheese"))
# print(get_menu_descriptions(menu, "Ham Pizza"))
# It works. (This meets requirement one of defining a function)

# Lets also add another function to create new pizzas
def add_menu_item(menu, item_name, description):
    if item_name in menu:
        print(f"{item_name} is already on the menu!")
    else:
        menu[item_name] = description
        print(f"{item_name} has been added to the menu!")

# Let's try calling our new function
# add_menu_item(menu, "BBQ Chicken", "Grilled Chicke, onions, and cilantro on a tangy BBQ tomato sauce base.")
# It works. (This meets the second requirement in the rubric.)

# Let's try iterating through the menu utilizing a for-loop now!
for item, description in menu.items():
    print(f"{item}: {description}")
