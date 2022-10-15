from collections import defaultdict
from item import Item

dummy = Item(-1, 0, 0, 0)


class Cart():
    def __init__(self):
        self.subtotal = 0
        self.discount = 0
        self.tax = 0
        self.total = 0
        self.itemList = [dummy]

    def addItem(self, item: Item) -> None:
        self.itemList.append(item)

    def removeItem(self) -> None:
        if (self.itemList):
            removedItem = self.itemList.pop()
            self.subtotal -= removedItem.price * removedItem.quantity

    def calculateSubtotal(self):
        subtotal = 0
        for item in self.itemList:
            subtotal += item.price * item.quantity

        self.subtotal = subtotal

    def updateItem(self, item: Item) -> None:
        self.itemList[int(item.id)] = item
        self.calculateSubtotal()

    def calculateTotal(self) -> None:
        self.calculateSubtotal()
        self.total = self.subtotal * \
            (1 - self.discount/100) * (1 + self.tax/100)

        self.total = round(self.total, 2)
