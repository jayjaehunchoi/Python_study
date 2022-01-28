import pytest

from object_oriented_programming.main import FruitStore, Product, User


# fixture : 매번 새로운 객체를 생성하지 않고 공통된 객체는 아래처럼 작성하면 된다.
@pytest.fixture(scope="function")
def fruit_store():
    return FruitStore(
        products={
            1: Product(name="사과", price=1000),
            2: Product(name="바나나", price=2000)
        }
    )


@pytest.fixture(scope="function")
def user(fruit_store):
    return User(money=100000, store=fruit_store)
