"""
Designed four classes: Customer, FoodItem, Collection, Transaction.
"""


class FoodItem:
    def __init__(self, name, price, category, rating):
        self._name = name
        self._price = price
        self._category = category
        self._rating = rating

    def getName(self):
        pass

    def getPrice(self):
        pass

    def getCategory(self):
        pass

    def getRating(self):
        pass

    def setPrice(self, price):
        pass

    def setRating(self, rating):
        pass


class Collection:
    def __init__(self, name):
        self._name = name
        self._items = []

    def getName(self):
        pass

    def getItems(self):
        pass

    def addItem(self, item):
        pass

    def removeItem(self, item):
        pass


class Transaction:
    def __init__(self):
        self._items = []
        self._total_cost = 0

    def getItems(self):
        pass

    def getTotalCost(self):
        pass

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
        pass

    def getCurrentTransaction(self):
        pass

    def getPastTransactions(self):
        pass

    def order(self):
        pass
