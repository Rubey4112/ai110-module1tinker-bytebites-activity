"""
Designed four classes: Customer, FoodItem, Catalog, Transaction.
"""


class FoodItem:
    def __init__(self, name, price, category, rating):
        self._name = name
        self._price = price
        self._category = category
        self._rating = rating

    def getName(self):
        return self._name

    def getPrice(self):
        return self._price

    def getCategory(self):
        return self._category

    def getRating(self):
        return self._rating

    def setPrice(self, price):
        pass

    def setRating(self, rating):
        pass


class Catalog:
    def __init__(self, name):
        self._name = name
        self._items = []

    def getName(self):
        return self._name

    def getItems(self):
        return list(self._items)

    def addItem(self, item):
        pass

    def removeItem(self, item):
        pass

    def filterByCategory(self, category):
        pass


class Transaction:
    def __init__(self):
        self._items = []
        self._total_cost = 0

    def getItems(self):
        return list(self._items)

    def getTotalCost(self):
        return self._total_cost

    def addItem(self, item):
        pass

    def removeItem(self, item):
        pass


class Customer:
    def __init__(self, name):
        self._name = name
        self._current_transaction = None
        self._past_transactions = []

    def getName(self):
        return self._name

    def getCurrentTransaction(self):
        return self._current_transaction

    def getPastTransactions(self):
        return list(self._past_transactions)

    def order(self):
        pass
