class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass

cl = D()
print(cl.__dict__)
print(D.__mro__)