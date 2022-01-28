import pytest

from object_oriented_programming.RealStore import RealStore
from object_oriented_programming.main import FruitStore, Product, User
API_URL = "https://fakestoreapi.com/products"

# fixture : 매번 새로운 객체를 생성하지 않고 공통된 객체는 아래처럼 작성하면 된다.
@pytest.fixture(scope="function")
def fruit_store():
    return FruitStore(
        products={
            1: Product(name="사과", price=1000),
            2: Product(name="바나나", price=500000)
        }
    )


@pytest.fixture(scope="function")
def user(fruit_store):
    return User(money=100000, store=fruit_store)


@pytest.fixture(scope="function")
def real_store():
    return RealStore()


@pytest.fixture(scope="function")
def mock_products():
    return {
        1: {"title": "사과", "price": "1000"},
        2: {"title": "바나나", "price": "500000"}
    }


# pip install requests_mock > 빠르게 mock patch 할 수 있게 도와주는 라이브러리
# 한 곳에 mocking이 필요한 request들을 모아서 외부 의존성을 참고하는 모든 테스트를 관리할 수 있다.
@pytest.fixture(scope="function")
def mock_api(requests_mock, mock_products):
    mock_product1 = mock_products[1]
    mock_product2 = mock_products[2]

    requests_mock.get(f"{API_URL}/1", json=mock_product1)
    requests_mock.get(f"{API_URL}/2", json=mock_product2)
    requests_mock.delete(f"{API_URL}/1", json=mock_product1)
    requests_mock.delete(f"{API_URL}/2", json=mock_product2)