from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, surname, pay):
        print('Добавлен сотрудник')
        self.name = name
        self.surname = surname
        self.pay = pay
        super().__init__()  # при class Developer(Employee, MixinLog):


class MixinLog:     # воспользоваться миксинами
    ID = 0

    # def __init__(self, name, surname, pay):   # при class Developer(MixinLog, Employee):
        # super().__init__(name, surname, pay)  # при class Developer(MixinLog, Employee):
    def __init__(self):                         # при class Developer(Employee, MixinLog):
        MixinLog.ID += 1
        print(f'Добавлен сотрудник с номером: {self.ID}')


class Developer(Employee, MixinLog):
#(<class '__main__.Developer'>, <class '__main__.Employee'>, <class 'abc.ABC'>, <class '__main__.MixinLog'>, <class 'object'>)

# class Developer(MixinLog, Employee):
# (<class '__main__.Developer'>, <class '__main__.MixinLog'>, <class '__main__.Employee'>, <class 'abc.ABC'>, <class 'object'>)

    def __init__(self, name, surname, pay, prog_lang):
        print('Добавлен разработчик')
        super().__init__(name, surname, pay)
        self.prog_lang = prog_lang


dev1 = Developer('Иван', 'Иванов', 100_000, 'Python')
dev2 = Developer('Иван', 'Иванов', 100_000, 'Python')
dev3 = Developer('Иван', 'Иванов', 100_000, 'Python')
dev4 = Developer('Иван', 'Иванов', 100_000, 'Python')
print(dev1.__dict__)
print(Developer.__mro__)
