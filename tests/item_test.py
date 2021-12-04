import unittest

from models.Item import Item

class TestItem(unittest.TestCase):
    def setUp(self):
        self.item = Item('Bran Flakes', 2.5, 2, False)

    def test_item_has_name(self):
        self.assertEqual('Bran Flakes', self.item.name)

    def test_item_has_price(self):
        self.assertEqual(2.5, self.item.price)

    def test_item_has_quantity(self):
        self.assertEqual(2, self.item.quantity)
        
    def test_item_is_bought_false(self):
        self.assertEqual(False, self.item.bought)

    def test_item_is_bought_not_true(self):
        self.assertFalse(True, self.item.bought)