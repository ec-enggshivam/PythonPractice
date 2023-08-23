
#string operations
var1="Hello"
var2="world"

print("var1: ", var1)

print("len(var1): ", len(var1))

print("Make Hello all caps ->var1.upper():", var1.upper())

print("Make world all small ->var2.lower():", var2.lower())

print("***************")
var3=var1+' '+var2
print("var3:", var3)
print(len(var3))
print("var3.isdigit()??? >", var3.isdigit())
print("***************")

var3='1234abc'
print(var3)
print(len(var3))
print(var3.isdigit())

print("***************")
var1=input("Enter a number: ")

if(var1.isdigit()):
    print(var1, "is valid input")    
else:
    print("Invalid input")

print("***************")    

var1='Hello world'
print(var1)
print("var1.count('l'): ",var1.count('l'))

print("var1.find('H'):", var1.find('H'))
print("var1[0]:", var1[0])
print("var1[1]:", var1[1])
print("var1[4]:", var1[4])
print(var1[1:50])
print("***************")    
var1='123456789'
print(var1)
print("var1[::1]: ", var1[::1])
print("var1[::2]: ", var1[::2])
print("var1[::4]: ", var1[::4])
print("var1[-1:0:-1]: ", var1[-5:0:-1])
#print(var1[::-2])
print("***************")
var1='123456789'
print(var1[0])
print(len(var1))
print(var1[len(var1)-3])
print("***************")
naam = input("enter a string:")
print("Reverse the string: ", naam[::-1])
print("***************")
'''
var1='hello_world'
print(var1)
#print(var1.replace('_',' '))
var2=var1.replace('_',' ')
print(var2)
print(var1)
var3=var1.split('_')
print(var3)
var3=var2.split(' ')
print(var3)

var2='$a$b$c$d'
var3=var2.split('$')
print(var3)

var4='$'.join(var3)
print(var4)



print(var1)
print("*******")
print(var1[::1])
print("*******")
print(var1[::-1])
print("*******")
print(var1[::2])
print(var1[::-2])
print("*******")
print(var1[::4])
print("*******")

var1='123456789'
print(var1[0])
print(len(var1))
#print(var1[len(var1)-1])
var1="*******"

print("*******")
print("  *  ")
print("  *  ")
print("  *  ")
print("  *  ")
#print(var1[8])
print(var1[2])
'''
print("*******")
var1=" 1 2 3 4 5"
var2=var1.split(' ')
print(var2)

var3=' '.join(var2)
print(var3)
