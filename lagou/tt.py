class A:
    name = 'a'

    def __init__(self):
        self.n = 2


a = A()
b = A()
A.name = 2
a.n = 2
print(a.name)
print(a.n)
print(b.name)
print(b.n)
