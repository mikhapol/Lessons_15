# Задача 3. Mixins

Программист начал реализацию класса 
Vehicle
:

    class Vehicle:

        def __init__(self, position):  # position: кортеж (10, 20)
            self.position = position
    
        def travel(self, destination):
            route = self.calculate_route(source=self.position, to=destination)
            self.move_along(route)
    
        @staticmethod
        def calculate_route(source, to):
            return 0  # to be realized
    
        def move_along(self, route):
            print("moving")

От класса 
Vehicle
 будет наследоваться два новых класса, подлежащих дальйшей реализации, — 
Car
 и 
Airplane
:

    class Car(Vehicle):
        pass
    
    
    class Airplane(Vehicle):
        pass

Подключите функционал радио к машине таким образом, чтобы не добавлять его к самолету.

>> Используйте класс-миксин, который самостоятельно создайте. Реализация миксина может быть минимальной — так, чтобы ожидаемое поведение соблюдалось. Пропишите инициализатор в классе 
Car
.

Ожидаемое поведение:

    car = Car((10, 20))
    car.turn_on_radio('Moscow FM')
    # Playing Moscow FM