

class Person(object):
    """
    Person class stores information about the person
    """
    global_count=0
    def __init__(self,name,id):
        """
        Constructor function
        :param name: Has vale name of the person
        :param id: Id of the person
        """
        print("Inside the base init")
        self.name=name
        self.age=id
        Person.global_count=Person.global_count+1
        #global global_val
        #global_val=global_val+1

    def __str__(self):
        """
        To return the elements of Class
        :return: return the elements of class
        """
#        print("Inside the str")
        return "Person ({0},{1})".format(self.name,self.age)

    def __del__(self):
        """
        Distructor to perform operation
        :return:
        """
#        print("Inside the del")
        pass

    def celebrateBirthday(self):
        """
        celebrateBirthday: Function to increment the Age
        """
        self.age =self.age+1

    def printDetals(self):
        """
        printDetals: Method to print the person details
        """
        print("Name is",self.name)
        print("Age is", self.age)

    @classmethod
    def getTotalCount(cls):
        return Person.global_count


'''

P= Person("Vinay",1)

l=list()

print(l)
print(P)

#P.name="Vinay"
#P.id=1

print(P.name)
print(P.age)

P.place="Bangalore"
print(P.place)
P2=Person("Manju",2)
print(P2.name)
print(P2.age)

P2.celebrateBirthday()
print(P2.age)
#P2.printDetals()

Person.getTotalCount()

print(Person.__dict__)
print(Person.__doc__)
print(Person.__name__)
print(Person.__module__)
print(Person.__bases__)

print(P2.global_count)
print(P.global_count)
P.global_count=5
print(P2.global_count)
print(P.global_count)
print(Person.getTotalCount())
'''


class Employee(Person):
    '''
    def __init__(self,name,age,salary):
        self.salary=salary
        print("Inside the Employee Init")
        super().__init__(name,age)
    '''

    def setSalary(self,salary):
        self.salary=salary
        #super(Employee, self).__del__()

    def printDetals(self):
        #super(Employee, self).printDetals()

        Person.printDetals(self)
        print("Salary is", self.salary)
        pass



E1=Employee("Raju","25")

E1.setSalary(15000)

E1.printDetals()


class A:
    def display(self):
        print("Inside A")


class B:
    def display(self):
        print("Inside B")

class C(B,A):
    pass


c=C()
c.display()

