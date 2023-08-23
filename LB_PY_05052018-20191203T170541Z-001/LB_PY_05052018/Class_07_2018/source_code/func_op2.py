'''
def method():
    a = 10 # local
    print("Print from method",a)

#############
print(a)
method()
'''
'''
a = 0
def funct0():
    print("in funct0 ",a)

def funct1():
    global a
    a = 100
    print("in funct1 ",a)


funct0()
funct1()
print("in global ",a)
funct0()

'''

#global
x = 0
def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
        print("inner:", x)
    inner()
    print("outer:", x)

outer()
#inner()
print("global:", x)
'''
def Sum (a,b):
    return a+b
'''