

class complex_num:

    def __init__(self,real,img):
        self.real=real
        self.img=img

    def __del__(self):
        pass

    def __str__(self):
        return 'complex({0},{1}j)'.format(self.real,self.img)

    def __add__(one,other):
        sum=complex_num(0,0)
        sum.real=one.real+other.real
        sum.img=one.img+other.img
        return sum



    def __sub__(self, other):
        result = complex_num(0, 0)
        result.real = self.real - other.real
        result.img = self.img - other.img
        return result


c1=complex_num(1,2)
print(c1)
c2=complex_num(3,5)
print(c2)

#c3=c1.add(c2)
#print(c3)
c4=c1+c2
print(c4)
c5=c2-c1
print(c5)
c6=c1-c2
print(c6)

#var1=1
#var2=2
#var3=var1+var2


