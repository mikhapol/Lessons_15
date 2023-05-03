class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10


dev_1 = Developer('Ivan', 'Ivanov', 60000)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.fullname())
