from abc import ABC, abstractmethod


class ShowMultBy(ABC):
    @abstractmethod
    def show_res_for(self, x):
        pass


class MultBy(ShowMultBy):
    """Класс, который использует миксин ShowMultBy."""

    def __init__(self, factor):
        self.factor = factor

    def multiply(self, x):
        return x * self.factor

    def show_res_for(self, x):
        print(f'Множитель: {x}, Аргумент: {self.factor},  Результат: {self.multiply(x)}')


if __name__ == '__main__':
    # Ожидаемый вывод:

    f = MultBy(10)
    f.show_res_for(20)
    # Множитель: 10, Аргумент: 20,  Результат: 200

    # sh = ShowMultBy()
    # TypeError: Can't instantiate abstract class ShowMultBy with abstract method ...
