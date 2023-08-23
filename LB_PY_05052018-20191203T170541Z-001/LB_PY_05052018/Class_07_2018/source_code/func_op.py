'''
def print_pat():
    print("*******")
    print("   *   ")
    print("   *   ")
    print("   *   ")
    print("   *   ")

print_pat()

def ConvertCtoF():
    C=int(input("Enter a value"))
    F=((9/5)*C+32)
    print("C=",C,"F=",F)

ConvertCtoF()
'''

# var=var+1
'''
def ConvertCtoF(C):
    #print(id(C))
    F=((9/5)*C+32)
    print("C=",C,"F=",F)
    C=C+1
    print("C=", C, "F=", F)
    print(id(C))

C=int(input("Enter a value"))
print(id(C))
print("C Before func call is",C)
ConvertCtoF(C)
print("C after func call is",C)

#print("Hello World")
#string.count('i')
'''
var = 1
print(type(var))
var = "string"
print(type(var))


def ConvertCtoF(C):
    return ((9 / 5) * C + 32)


print(type(ConvertCtoF))

C = int(input("Enter a value"))
F = ConvertCtoF(C)
# print("C is",C,"F is",F)
if (F >= 85 and F < 99):
    print("Temperature is normal")
elif (F >= 99 and F < 102):
    print("You have light fever")
elif (F >= 102):
    print("Take him to hospital")
