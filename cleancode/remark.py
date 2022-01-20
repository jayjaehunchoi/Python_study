class Product:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)


# TODO
# XXX
# FIXME
if __name__ == '__main__':
    for idx in range(1, 11):
        print(idx)

    product_list = []
    # product_list.extend([Product("모니터"), Product("키보드"), Product("스피커")]) not good

    items = [Product("모니터"), Product("키보드"), Product("스피커")]
    product_list.extend(items)

    for product in product_list:
        product.print_name()

