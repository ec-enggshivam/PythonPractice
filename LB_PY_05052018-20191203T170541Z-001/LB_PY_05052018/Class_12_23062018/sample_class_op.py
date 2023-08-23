
class Person(object):
    def __init__(self,name,age,dob):
        self.name=name
        self.age=age
        self.__dob=dob

    def __str__(self):
        return 'Person({0},{1})'.format(self.name,self.age)

    def __repr__(self):
        return '%s(%r%r)' % (self.__class__, self.name,self.age)




P1=Person("Raju",25,"10/02/1993")


print(P1.name)
print(P1.age)
print(P1._Person__dob)

print(repr(P1))
print(str(P1))


print(Person.__dict__)
print(Person.__doc__)
print(Person.__name__)
print(Person.__module__)
print(Person.__bases__)


