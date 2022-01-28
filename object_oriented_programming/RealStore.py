from object_oriented_programming.main import Store, Product
import requests


class RealStore(Store):
    def __init__(self, url="https://fakestoreapi.com"):
        self._money = 0
        self.name = "과일가게"
        self.url = url

    def set_money(self, money):
        self._money = money

    def show_product(self, product_id):
        res = requests.get(f"{self.url}/products/{product_id}")
        product = res.json()
        return Product(name=product["title"], price=product["price"])

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
        res = requests.delete(f"{self.url}/products/{product_id}")
        product = res.json()
        return Product(name=product["title"], price=product["price"])

    def _return_money(self, money):
        if self._money < money:
            raise Exception("잔돈이 부족합니다.")
        self._money -= money


if __name__ == '__main__':
    store = RealStore()
    result = store.show_product(product_id=1)
    print(result)