import pytest
from models import Customer, Catalog, FoodItem, Transaction


def test_add_and_get_item_from_catalog():
    catalog = Catalog("Main Menu")
    burger = FoodItem("Spicy Burger", 8.99, "Burgers", 4.5)
    catalog.addItem(burger)
    assert burger in catalog.getItems()


def test_calculate_total_with_multiple_items():
    transaction = Transaction()
    transaction.addItem(FoodItem("Spicy Burger", 8.99, "Burgers", 4.5))
    transaction.addItem(FoodItem("Large Soda", 2.49, "Drinks", 4.0))
    assert transaction.getTotalCost() == pytest.approx(11.48)


def test_order_total_is_zero_when_empty():
    transaction = Transaction()
    assert transaction.getTotalCost() == 0


def test_filter_drinks_only_returns_liquid_items():
    catalog = Catalog("Main Menu")
    catalog.addItem(FoodItem("Large Soda", 2.49, "Drinks", 4.0))
    catalog.addItem(FoodItem("Water Bottle", 1.00, "Drinks", 3.8))
    catalog.addItem(FoodItem("Spicy Burger", 8.99, "Burgers", 4.5))
    drinks = catalog.filterByCategory("Drinks")
    assert len(drinks) == 2
    assert all(item.getCategory() == "Drinks" for item in drinks)


# --- Customer tests ---

def test_customer_name():
    customer = Customer("Alice")
    assert customer.getName() == "Alice"


def test_new_customer_has_no_current_transaction():
    customer = Customer("Alice")
    assert customer.getCurrentTransaction() is None


def test_new_customer_has_no_past_transactions():
    customer = Customer("Alice")
    assert customer.getPastTransactions() == []


def test_order_moves_transaction_to_past():
    customer = Customer("Alice")
    transaction = Transaction()
    customer._current_transaction = transaction
    customer.order()
    assert transaction in customer.getPastTransactions()


def test_order_clears_current_transaction():
    customer = Customer("Alice")
    customer._current_transaction = Transaction()
    customer.order()
    assert customer.getCurrentTransaction() is None


def test_order_accumulates_multiple_past_transactions():
    customer = Customer("Alice")
    for _ in range(3):
        customer._current_transaction = Transaction()
        customer.order()
    assert len(customer.getPastTransactions()) == 3


def test_order_does_nothing_when_no_current_transaction():
    customer = Customer("Alice")
    customer.order()
    assert customer.getPastTransactions() == []
    assert customer.getCurrentTransaction() is None