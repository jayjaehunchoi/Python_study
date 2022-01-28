import pytest

from object_oriented_programming.main import FruitStore, Product


def test_show_product(fruit_store):
    # given
    product_id = 1
    # when
    product = fruit_store.show_product(product_id=product_id)

    # then
    assert product == Product(name="사과", price=1000)


def test_take_money(fruit_store):
    price = 100
    pre_money = fruit_store._money

    fruit_store._take_money(money=price)

    assert fruit_store._money == pre_money + price


def test_return_money(fruit_store):
    price = 100

    with pytest.raises(Exception):
        fruit_store._return_money(money=price)


def test_take_out_product(fruit_store):
    product_id = 1

    product = fruit_store._take_out_product(product_id=product_id)

    assert product == Product(name="사과", price=1000)
    assert not fruit_store._products.get(product_id, None)
