"""
Designed four classes: Customer, FoodItem, Catalog, Transaction.
"""


# Represents a single menu item available for purchase.
class FoodItem:
    def __init__(self, name, price, category, rating):
        self._name = name
        self._price = price
        self._category = category
        self._rating = rating

    # Returns the item's display name (e.g. "Spicy Burger").
    def getName(self):
        return self._name

    # Returns the item's price used when computing transaction totals.
    def getPrice(self):
        return self._price

    # Returns the category string used for catalog filtering (e.g. "Drinks").
    def getCategory(self):
        return self._category

    # Returns the popularity rating for this item.
    def getRating(self):
        return self._rating

    # Updates the item's price.
    def setPrice(self, price):
        pass

    # Updates the item's popularity rating.
    def setRating(self, rating):
        pass


# Manages the full collection of available food items and supports browsing.
class Catalog:
    def __init__(self, name):
        self._name = name
        self._items = []

    # Returns the catalog's name.
    def getName(self):
        return self._name

    # Returns a copy of all items currently in the catalog.
    def getItems(self):
        return list(self._items)

    # Adds a FoodItem to the catalog's item list.
    def addItem(self, item):
        pass

    # Removes a FoodItem from the catalog's item list.
    def removeItem(self, item):
        pass

    # Returns only the items whose category matches the given string.
    def filterByCategory(self, category):
        pass


# Represents a single purchase session grouping one or more food items.
class Transaction:
    def __init__(self):
        self._items = []
        self._total_cost = 0

    # Returns a copy of the items in this transaction.
    def getItems(self):
        return list(self._items)

    # Returns the running total cost; kept in sync by addItem/removeItem.
    def getTotalCost(self):
        return self._total_cost

    # Adds a FoodItem and increments total_cost by the item's price.
    def addItem(self, item):
        pass

    # Removes a FoodItem and decrements total_cost by the item's price.
    def removeItem(self, item):
        pass


# Represents a registered user who can browse items and place orders.
class Customer:
    def __init__(self, name):
        self._name = name
        self._current_transaction = None
        self._past_transactions = []

    # Returns the customer's name.
    def getName(self):
        return self._name

    # Returns the in-progress Transaction, or None if no order is active.
    def getCurrentTransaction(self):
        return self._current_transaction

    # Returns a copy of all completed transactions for this customer.
    def getPastTransactions(self):
        return list(self._past_transactions)

    # Completes the current_transaction, moves it to past_transactions, and clears current_transaction.
    # To build an order, call Transaction.addItem() directly on the current_transaction before calling order().
    def order(self):
        pass
