# test_order.py
import pytest
from order import Order

@pytest.fixture
def order():
    return Order(stock=10)

def test_purchase_success(order):
    result = order.purchase(3)
    assert result == "Order successful"
    assert order.stock == 7

def test_purchase_not_enough_stock(order):
    result = order.purchase(20)
    assert result == "Not enough stock"
    assert order.stock == 10

def test_purchase_invalid(order):
    result = order.purchase(0)
    assert result == "Invalid quantity"
    assert order.stock == 10
