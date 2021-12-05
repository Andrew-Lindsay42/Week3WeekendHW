import unittest

from models.item import Item
from models.shopping_list import add_new_item, total_cost, total_items

class TestList(unittest.TestCase):
    def setUp(self):
        item_1 = Item('Apple', 1.0, 2, False)
        item_2 = Item('Orange', 1.5, 1, False)
        item_3 = Item('Banana', 1.23, 3, True)

        self.shopping_list = [item_1, item_2, item_3]

    def test_can_add_item(self):
        grapes = Item('Grapes', 1.23, 1, True)
        add_new_item(self.shopping_list, grapes)
        self.assertEqual(4, len(self.shopping_list))

    def test_total_cost_no_discount(self):
        self.assertEqual(7.19, total_cost(self.shopping_list))

    def test_total_cost_discount(self):
        plums = Item('Plums', 1, 5, False)
        add_new_item(self.shopping_list, plums)
        self.assertEqual(11.69, total_cost(self.shopping_list))

    def test_total_items(self):
        self.assertEqual(6, total_items(self.shopping_list))
