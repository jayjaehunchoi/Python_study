import pytest


def test_check_money(user):
    cheap_price = 500
    expensive_price = 10000000

    can_buy = user._check_money_enough(cheap_price)
    assert can_buy

    cannot_buy = user._check_money_enough(expensive_price)
    assert not cannot_buy


def test_give_money_cheaper(user):
    price = 500
    pre_money = user._money
    user._give_money(price)
    post_money = user._money

    assert post_money == pre_money - price


def test_give_money_expensive(user):
    price = 10000000
    with pytest.raises(Exception):
        user._give_money(money=price)


def test_purchase_product_well(user):
    product_id = 1
    pre_user_money = user._money

    product = user.purchase_product(product_id=product_id)

    assert user.get_money() == pre_user_money - product.price
    assert user.get_belongs() == [product]


def test_purchase_product_expensive(user):
    product_id = 2

    with pytest.raises(Exception):
        user.purchase_product(product_id=product_id)
