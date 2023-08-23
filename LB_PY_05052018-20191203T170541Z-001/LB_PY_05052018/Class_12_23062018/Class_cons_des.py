"""
This is a Sample Class.

"""


class Person:
    """
    This is person class
    """
    Total_count = 0

    def __init__(self, name, age):
        """
        Init method to person class
        :param name:
        :param age:
        """
        # print("Inside the __init__")
        # print("Self is ",self)
        self.name = name
        self.age = age
        Person.Total_count = Person.Total_count + 1

    def __str__(self):
        """
        Method to print the object
        :return:
        """
        return 'Person({0},{1})'.format(self.name, self.age)

    def __del__(self):
        """
        Method called during object going out of scope
        """
        # print("Inside the __del__")
        Person.Total_count = Person.Total_count - 1

    def print_details(self):
        """

        :return:
        """
        print("Person Name is", self.name)
        print("Person Age is", self.age)

    def celebrateBirthday(self):
        """

        :return:
        """
        self.age = self.age + 1

    def get_total_count(self):
        return Person.Total_count

    @classmethod
    def get_person_count(cls):
        return Person.Total_count

    def get_count():
        return Person.Total_count

    get_count = staticmethod(get_count)


# var="12"
# var=int(var)


def celebrate_Birthday(P):
    p = Person("", 0)
    # sum=sum+val
    p.age = P.age + 1
    p.name = P.name
    return p


'''
L1=["Raju",27]
print(L1)
print(L1[0])
print(L1[1])

P1=Person("Raju",27)
#P2=Person("Manju",25)
#P3=Person("Ramesh",30)

#P4=celebrate_Birthday(P3)
#P4.print_details()
#P3.print_details()

#print(P1)
P1.print_details()
P1.celebrateBirthday()

print(Person.__dict__)
print(Person. __doc__)
print(Person.__name__)
print(Person. __module__)
print(Person. __bases__)

#print(P1)

#print(P2)
#print(P3)

P1=Person("Mahesh",32)
print(P1)
P1.print_details()
P2=P1
print(id(P1))
print(id(P2))
del(P1)

P2.print_details()
print(id(P2))
print(id(P1))
'''

# print(P1.name)
# print(P1.age)

P1 = Person("Raju", 25)
# print(P1.dob)
# Person.dob="12031990"
# print(P1.dob)

print(P1)
P2 = Person("R", 25)
P3 = Person("A", 25)
P4 = Person("J", 25)
P5 = Person("U", 25)

print(Person.Total_count)

print(P1.get_total_count())

del (P2)
del (P3)
del (P4)

# print(Person.Total_count)
# print(P1.get_total_count())
# print(Person.get_person_count())
print(Person.get_count())
print(P5.get_total_count())
print(P1.get_total_count())
