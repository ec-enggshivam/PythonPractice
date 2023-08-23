
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
        print(">>>>>B<<<<<")

    def __del__(self):
        print("in des B")
        super().__del__()


class C(B):
    def __init__(self):
        super().__init__()
        print("inside C")

    def display(self):
        print(">>>>>C<<<<<")

    def __del__(self):
        print("in des C")
        super().__del__()

c=C()
c.display()
C.display(c)
print("C",C.__bases__)

