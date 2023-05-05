class Item:

    def __init__(self, name, price, quantity=0):
        self.__check(name, price, quantity)

        self.name = name
        self.price = price
        self.quantity = quantity

    @staticmethod
    def __check(name: str, price: int | float, quantity: int) -> None:
        if not isinstance(name, str):
            raise TypeError('Название товара должно быть строкой.')

        if not isinstance(price, int | float):
            raise TypeError('Цена товара должна быть числом.')

        if not isinstance(quantity, int):
            raise TypeError('Количество товара должно быть целым числом.')


if __name__ == '__main__':
    print(Item('phone', 18000, 5))
    # <__main__.Item object at 0x0000022D9E035CD0>

    # Item(18000, 'phone', 5)
    # TypeError: Название товара должно быть строкой.

    # Item('phone', '18000', 5)
    # TypeError: Цена товара должна быть числом.

    # print(Item('phone', 1.8, 5.1))
    # TypeError: Количество товара должно быть целым числом.

    # Item('phone', 18000, 5.5)
    # TypeError: Количество товара должно быть целым числом.
