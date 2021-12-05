from models.item import Item

item_1 = Item('Bran Flakes', 2.5, 2, False)
item_2 = Item('Chocolate Orange', 1.0, 5, False)
item_3 = Item('Washing-up Liquid', 1.99, 1, True)

shopping_list = [item_1, item_2, item_3]

def add_new_item(current_list, new_item):
    current_list.append(new_item)

def total_cost(current_list):
    total = 0
    for item in current_list:
        total += (item.price * item.quantity)
    total = float('{:.2f}'.format(total))
    return total

def total_items(current_list):
    total = 0
    for item in current_list:
        total += item.quantity
    return total