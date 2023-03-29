# import pytest
# import copy
from hexlet_pytest.lesson6 import Right


def test_cart1():
    cart = Right()
    cart.add_item({'name': 'car', 'price': 3}, 5)
    assert len(cart.get_items()) == 1
    cart.add_item({'name': 'house', 'price': 10}, 2)
    assert len(cart.get_items()) == 2
    assert cart.get_cost() == 35
    cart.add_item({'name': 'house', 'price': 10}, 1)
    assert len(cart.get_items()) == 3
    assert cart.get_count() == 8