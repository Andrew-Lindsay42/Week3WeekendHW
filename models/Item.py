class Item:
    def __init__(self, name, price, quantity, bought):
        self.name = name
        self.quantity = quantity
        if self.quantity >= 5:
            self.price = price * 0.9
        else:
            self.price = price
        self.bought = bought