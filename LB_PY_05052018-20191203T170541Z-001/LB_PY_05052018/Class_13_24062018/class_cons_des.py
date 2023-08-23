

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
        print("Person name is",self.name)
        print("Person age is", self.age)

    @classmethod
    def getTotalCount(cls):
        return Person.global_count


    def getdetails(value):
        print("Value is",value)
        return Person.global_count

    getdetails=staticmethod(getdetails)

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
#    pass
    def __init__(self,name,age,id,salary):
        super().__init__(name,age)
        self.id = id
        self.salary=salary


    def set_details(self,id,salary):
        self.id=id
        self.salary=salary


    def printDetals(self):
        #Person.printDetals(self)
        super().printDetals()
        print("Employee id is ",self.id)
        print("Employee salary is ", self.salary)



E1=Employee("Vinay","30",101,25000)

#E1.setSalary(15000)

E1.printDetals()
print(Employee.__bases__)



