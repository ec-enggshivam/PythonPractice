
class A:
    def __init__(self):
        super().__init__()
        print("inside A")

    def display(self):
        super().display()
        print(">>>>>A<<<<<")

    def __del__(self):
        print("in des A")

class B:
    def __init__(self):
        print("inside B")

    def display(self):
        print(">>>>>B<<<<<")

    def __del__(self):
        print("in des B")



class C(A,B):
    def __init__(self):
        super().__init__()
        print("inside C")

    def display(self):
        super().display()
        print(">>>>>C<<<<<")

    def __del__(self):
        print("in des C")
        super().__del__()

c=C()
c.display()
C.display(c)
print("C",C.__bases__)