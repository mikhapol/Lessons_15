import timeit


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_set_del(self):
        self.x += 1
        self.y = 100
        del self.y


class PointSlots:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_set_del(self):
        self.x += 1
        self.y = 100
        del self.y


p = Point(1, 2)
p.z = 100
# print(p.__dict__)

ps = PointSlots(3, 4)

t1 = timeit.timeit(p.get_set_del)
t2 = timeit.timeit(ps.get_set_del)

print(t1)
print(t2)
