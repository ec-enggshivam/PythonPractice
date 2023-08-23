class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.rupee = 1000
        print('Inside constructor of A',self.name,self.age)
    def display(self):
        print('display of class A')

class B(A):
    def __init__(self):
        super().__init__('abc',28)
        print('Inside constructor of B')
        print('derived values',self.name,self.age)

    def display(self):
        super().display()
        print('display of class B')

class C(A):
    def __init__(self):
        super().__init__()
        print('Inside constructor of C')

    def display(self):
        super().display()
        print('display of class C')

class D(C,B):
    def __init__(self):
        super().__init__()
        print('Inside constructor of D')
'''
    def display(self):
        super().display()
        print('display of class D')
'''

d1 = D()
d1.display()
