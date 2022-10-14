from collections import defaultdict
from item import Item

dummy = Item(-1, 0, 0, 0)


class Cart():
    def __init__(self):
        self.discount = 0
        self.tax = 100
        self.pretax_totalprice = self.subtotal - \
            (self.subtotal * (self.discount / 100))
        self.aftertax_totalprice = self.pretax_totalprice * self.tax
        self.itemList = [dummy]

    def addItem(self, item: Item) -> None:
        self.itemList.append(item)

    def removeItem(self) -> None:
        self.itemList.pop()

    def updateItem(self, item: Item) -> None:
        self.itemList[item.id] = item

    def applyDiscount(self) -> None:

    def calculateSubTotal(self):
        self.subtotal = 0.00

    def calculateTotal(self) -> float:
        return self.aftertax_totalprice
