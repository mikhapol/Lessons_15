class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def full_info(self):
        return print(f'Я, {self.first} {self.last}, зарабатываю {self.pay}')

    def code(self):
        print("Я программирую как сотрудник.")


class Developer(Employee):
    # Переопределяем метод базового класса
    def __init__(self, first, last, pay, prog_lang):
        # Вызываем метод базового класса
        super().__init__(first, last, pay)
        # Дополнительный код
        self.prog_lang = prog_lang

    # Переопределение метода code()
    def code(self):
        print("Сейчас я занимаюсь программированием как разработчик!")


emp_1 = Employee('Ivan', 'Ivanov', 60000)

emp_1.full_info()  # Вызов метода базового класса Employee
emp_1.code()  # Вызов переопределенного метода класса Employee
print('~~~~~~~~~')

dev_1 = Developer('Ivan', 'Ivanov', 60000, 'Python')
dev_2 = Developer('Petr', 'Petrov', 70000, 'Java')

dev_1.full_info()  # Вызов метода базового класса Employee
dev_1.code()  # Вызов переопределенного метода класса Developer
print('---------')
dev_2.full_info()  # Вызов метода базового класса Employee
dev_2.code()  # Вызов переопределенного метода класса Developer
print('---------')


