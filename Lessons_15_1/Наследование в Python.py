class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.pay_raise = None
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay_raise = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10


dev_1 = Employee('Ivan', 'Ivanov', 60000)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.fullname())
print(f'{dev_1.fullname()} = {dev_1.pay}  с коэффициентом {Employee.raise_amt} = {dev_1.pay_raise}')
print('---------')
dev_1 = Developer('Ivan', 'Ivanov', 60000)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.fullname())
print(f'{dev_1.fullname()} = {dev_1.pay}  с коэффициентом {Developer.raise_amt} = {dev_1.pay_raise}')
