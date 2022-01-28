import pytest
from object_oriented_programming.main import FruitStore, Product
from unittest import mock


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


# 통합 테스트 - 잘되는 경우와 예외 경우 모두 살펴보기
def test_sell_product_well(fruit_store):
    product_id = 1
    pre_money = fruit_store._money

    # 상품 가져오기
    product = fruit_store.show_product(product_id=product_id)

    _product = fruit_store.sell_product(product_id=product_id, money=product.price)

    assert fruit_store._money == product.price
    assert not fruit_store.show_product(product_id=product_id)


def test_sell_product_not_found(fruit_store):
    product_id = 100

    with pytest.raises(Exception):
        fruit_store.sell_product(product_id=product_id, money=0)


# 외부 api테스트
# 온전히 통제할 수 없다 (어떤 값이 올지 모름)
# 다른 환경의 데이터에 영향을 주면 안된다 -> 따라서 Mocking이 필요하다.
def test_show_product_api(real_store):
    # given
    product_id = 1
    # when
    product = real_store.show_product(product_id=product_id)

    # then - test failed
    #assert product == Product(name="사과", price=1000)


def test_show_product_mock(real_store, mock_products, mock_api):
    # given
    product_id = 1
    mock_product = mock_products[product_id]
    # when

    product = real_store.show_product(product_id=product_id)

    # then
    assert product == Product(name=mock_product["title"], price=mock_product["price"])