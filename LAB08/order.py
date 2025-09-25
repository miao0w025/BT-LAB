# order.py
class Order:
    def __init__(self, stock):
        self.stock = stock

    def purchase(self, quantity):
        if quantity <= 0:
            return "Invalid quantity"
        if quantity > self.stock:
            return "Not enough stock"
        self.stock -= quantity
        return "Order successful"
