class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def full_info(self):
        return print(f'Я, {self.first} {self.last}, зарабатываю {self.pay}')


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def __add__(self, other):
        if not isinstance(other, Employee):
            raise ValueError('Складывать можно только объекты Employee и дочерние от них.')
        return self.pay + other.pay


dev_1 = Developer('Ivan', 'Ivanov', 60000, 'Python')
dev_2 = Developer('Petr', 'Petrov', 70000, 'Java')
print(dev_1 + dev_2)

emp_1 = Employee('Petr', 'Petrov', 50000)
print(dev_1 + emp_1)

# print(dev_2 + 10000)
