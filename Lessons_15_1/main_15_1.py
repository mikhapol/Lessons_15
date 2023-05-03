class Employee:
    raise_coef = 1.04

    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.pay = pay

    def raise_pay(self):
        self.pay *= self.raise_coef
        self.pay = round(self.pay)

    def __add__(self, other):
        # if isinstance(other, self.__class__):
        if issubclass(other.__class__, self.__class__):
            return self.pay + other.pay
        # return None
        raise Exception


class Developer(Employee):
    raise_coef = 1.1

    def __init__(self, name, surname, pay, prog_lang):
        super().__init__(name, surname, pay)
        self.prog_lang = prog_lang


emp1 = Employee('Михаил', 'Михайлович', 50000)
print(emp1.__dict__)
print('---------')
print(emp1.pay)
emp1.raise_pay()
print(emp1.pay)
print('~~~~~~~~~')

dev1 = Developer('Иван', 'Иванов', 100000, 'python')
dev2 = Developer('Петр', 'Петров', 150000, 'java')

print(dev1.__dict__)
print('---------')
print(dev1.pay)

dev1.raise_pay()
print(dev1.pay)
print('---------')
print(dev2.pay)

dev2.raise_pay()
print(dev2.pay)
print('---------')
print(dev1.prog_lang, dev2.prog_lang)
print('~~~~~~~~~')
total_pay = emp1 + dev1
total_pay_2 = dev1 + dev2
# total_pay = dev1 + 100000
print(f"{total_pay} состоит из {emp1.pay} и {dev1.pay}")
print(f"{total_pay_2} состоит из {dev1.pay} и {dev2.pay}")
