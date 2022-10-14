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

    def calculateSubTotal(self):
        for item in self.itemList:
            self.subtotal += item.price * item.quantity

    def updateItem(self, item: Item) -> None:
        self.itemList[int(item.id)] = item
        self.calculateSubTotal()

    def calculateTotal(self) -> None:
        self.total = self.subtotal * \
            (1 - self.discount/100) * (1 + self.tax/100)

        self.total = round(self.total, 2)
