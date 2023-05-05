# *Задача 1(4). Миксин

Имеется следующий класс 
MultBy
:

    class MultBy(ShowMultBy):
       """Класс, который использует миксин ShowMultBy."""
   
       def __init__(self, factor):
           self.factor = factor
   
       def multiply(self, x):
           return x * self.factor

Реализуйте класс 
ShowMultBy
, чтобы выполнялся ожидаемый вывод.

* Ожидаемый вывод:

      f = MultBy(10)
      f.show_res_for(20)
      # Множитель: 10, Аргумент: 20,  Результат: 200
   
      sh = ShowMultBy()
      # TypeError: Can't instantiate abstract class ShowMultBy with abstract method ...
