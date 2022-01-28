# 객체 지향으로 코드 짜기
# 1. Store 추상화
# 2. 의존성 주입
# 3. Store 에서 상품과, 돈에 접근하는 메서드를 생성해준다. (캡슐화)
# 4. User 결제 로직 수정

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: int


class Store(ABC):
    @abstractmethod
    def __init__(self):
        self._money = 0
        self.name = ""
        self._products = {}

    @abstractmethod
    def show_product(self, product_id):
        pass

    @abstractmethod
    def sell_product(self, product_id, money):
        pass


class FruitStore(Store):
    def __init__(self, products):
        self._money = 0
        self.name = "과일가게"
        self._products = products

    def set_money(self, money):
        self._money = money

    def set_products(self, products):
        self._products = products

    def show_product(self, product_id):
        return self._products[product_id]

    def sell_product(self, product_id, money):
        product = self.show_product(product_id)
        if not product:
            raise Exception("상품이 존재하지 않습니다.")

        self._take_money(money)
        try:
            _product = self._take_out_product(product_id)
        except Exception as e:
            self._return_money(money)
            raise e

        return _product

    def _take_money(self, money):
        self._money += money

    def _take_out_product(self, product_id):
        return self._products.pop(product_id)

    def _return_money(self, money):
        if self._money < money:
            raise Exception("잔돈이 부족합니다.")
        self._money -= money


class User:
    def __init__(self, money, store: Store):
        self._money = money
        self.store = store
        self.belongs = []

    def get_money(self):
        return self._money

    def get_belongs(self):
        return self.belongs

    def get_store(self):
        return self.store

    def see_product(self, product_id):
        product = self.store.show_product(product_id=product_id)
        return product

    def purchase_product(self, product_id):
        product = self.see_product(product_id=product_id)
        price = product.price
        if self._check_money_enough(price):
            self._give_money(price)  # 사용자가 돈 내기
            try:
                my_product = self.store.sell_product(product_id, price)
                self._add_belong(my_product)
                return my_product
            except Exception as e:
                self._take_money(price)
                print(f"구매 중 문제 발생{str(e)}")

        else:
            raise Exception("잔돈이 부족합니다")

    def _check_money_enough(self, price):
        return self._money >= price

    def _give_money(self, money):
        if not self._check_money_enough(price=money):
            raise Exception("금액이 부족합니다.")
        self._money -= money

    def _take_money(self, money):
        self._money += money

    def _add_belong(self, product):
        self.belongs.append(product)


if __name__ == "__main__":
    store = FruitStore(
        products={
            1: Product(name="사과", price=1000),
            2: Product(name="바나나", price=2000)
        }
    )
    user = User(money=10000, store=store)
    user.purchase_product(product_id=1)
    print(f"user의 잔돈 : {user.get_money()}")
    print(f"user가 구매한 상품 : {user.get_belongs()}")
