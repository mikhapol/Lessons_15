class MyList(list):
    def __new__(cls, *args, **kwargs):
        print('Работает магический метод: __new__')
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, value):
        print('Работает магический метод: __init__')
        super().__init__(value)

    def __getitem__(self, item):
        print('Работает магический метод: __getitem__')
        return super().__getitem__(item)

    def __str__(self):
        print('Работает магический метод: __str__')
        return super().__str__()

    def __len__(self):
        print('Работает магический метод: __len__')
        return super().__len__()


if __name__ == '__main__':
    lst = MyList(['Jone', 'Snow', 'Java'])

    if not lst[2] == 'Python':
        lst[2] = 'Python'

    print(lst)
    print(f'Количество элементов списка: {len(lst)}.')

# Работает магический метод     # __new__
# Работает магический метод     # __init__
# Работает магический метод     # __getitem__
# Работает магический метод     # __str__
# ['Jone', 'Snow', 'Python']
# Работает магический метод     # __len__
# 3
