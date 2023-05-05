# Задача 2. Функции issubclass() и isinstance()

* Создай класс 
Item
 со следующими полями:

* name
 — название товара,
* price
 — цена товара,
* quantity
 — количество товара.

       class Item:

            def __init__(self, name, price, quantity=0):
    
              self.__check(name, price, quantity)
    
              self.name = name
              self.price = price
              self.quantity = quantity

Реализуйте метод 
__check
, который проверяет допустимость данных при инициализации товара.

Ожидаемое поведение:

>>> Item('phone', 18000, 5)
<__main__.Item object at 0x0000022D9E035CD0>


>>> Item(18000, 'phone', 5)
TypeError: Название товара должно быть строкой.

>>> Item('phone', '18000', 5)
TypeError: Цена товара должна быть числом.


>>> Item('phone', 18000, 5.5)
TypeError: Количество товара должно быть целым числом.