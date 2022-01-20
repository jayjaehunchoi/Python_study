user_data = "data"
is_valid = True


def send_data():
    print(user_data)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


product = Product("아이폰", 1400)

if __name__ == '__main__':
    print(product.price)

    if is_valid:
        send_data()
