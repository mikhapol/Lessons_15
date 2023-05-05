from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod  # TypeError: Can't instantiate abstract class Vehicle with abstract method go
    def go(self):
        pass


class Car(Vehicle):

    def go(self):
        print("Вы едете на машине")


class Motorcycle(Vehicle):

    # pass # TypeError: Can't instantiate abstract class Motorcycle with abstract method go
    def go(self):
        print("Вы едете на мотоцикле")


def test_go(vehicle):
    vehicle.go()


# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()
# vehicle.go()
car.go()
motorcycle.go()
print('~~~~~~~~~')
call = [car, motorcycle]
for v in call:
    v.go()
print('~~~~~~~~~')
test_go(car)         # Выводит "Езда на автомобиле"
test_go(motorcycle)  # Выводит "Езда на мотоцикле"
