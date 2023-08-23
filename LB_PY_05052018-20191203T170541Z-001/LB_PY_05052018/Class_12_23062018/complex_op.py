

class complex_num:
    """
    complex number class def


    """
    total_count=0
    def __init__(self,real,img):
        """

        :param real:
        :param img:
        """
        self.real=real
        self.img=img
        self.__sample=0
        complex_num.total_count=complex_num.total_count+1

    def __str__(self):
        return '[{0}+{1}j]'.format(self.real,self.img)

    def __add__(self, other):
        temp=complex_num(0, 0)
        temp.real=self.real+ other.real
        temp.img = self.img + other.img
        return temp

    def __sub__(self, other):
        temp=complex_num(0,0)
        temp.real = self.real - other.real
        temp.img = self.img - other.img
        return temp

    @classmethod
    def get_count(cls):
        return complex_num.total_count


v1=complex_num(1,2)
print(v1)

v2=complex_num(3,5)
print(v2)

v3=v2-v1
v4=v1+v2

print(v3)
print(v4)
print(complex_num.get_count())


print(v1.get_count())

print(v1._complex_num__sample)