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

    def applyDiscount(self) -> None:
        self.subtotal -= self.discount * self.subtotal

    def calculateTotal(self):
        self.total = self.subtotal * self.tax
