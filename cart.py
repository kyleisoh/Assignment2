from collections import defaultdict
from item import Item


class Cart():

    def __init__(self):
        self.subtotal = 0.00
        self.discount = 0
        self.pretax_totalprice = self.subtotal - \
            (self.subtotal * (self.discount / 100))
        self.aftertax_totalprice = self.pretax_totalprice * 1.15
        self.cart = {}

    def addItem(self, item: Item) -> None:
        id, name, price, quantity = item.id, item.name, item.price, item.quantity
        if (id not in self.cart):
            self.cart[id] = [name, price, quantity]

        else:
            # the item with the same id exists in our cart, update the name, price, quantity
            self.cart[id][0] = name
            self.cart[id][1] = price
            self.cart[id][2] = quantity

    def removeItem(self, item: Item) -> None:
        id = self.item.id
        self.cart.pop(id)

    def applyDiscount(self, discount) -> None:
        self.discount = discount

    def applyTax(self) -> float:
        return self.aftertax_totalprice
