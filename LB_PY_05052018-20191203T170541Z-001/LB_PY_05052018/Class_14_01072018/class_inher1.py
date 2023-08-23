
class A:
    def __init__(self):

        print("inside A")

    def display(self):

        print(">>>>>A<<<<<")

    def __del__(self):
        print("in des A")

class B(A):
    def __init__(self):
        super().__init__()
        print("inside B")

    def display(self):
        super().display()
        print(">>>>>B<<<<<")

    def __del__(self):
        print("in des B")
        super().__del__()


class C(A):
    def __init__(self):
        super().__init__()
        print("inside C")

    def display(self):
        super().display()
        print(">>>>>C<<<<<")

    def __del__(self):
        print("in des C")
        super().__del__()



b=B()
b.display()
B.display(b)
print("B",B.__bases__)

c=C()
c.display()
C.display(c)
print("C",C.__bases__)