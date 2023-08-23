
a=[]

b=list()

c=[1,2,3]


'''
print("type of a is",type(a))
print("type of b is",type(b))
print("type of c is",type(c))

print("Value of a is",a)
print("Value of b is",b)
'''
print("Value of c is",c)
'''
print(c[0])
print(c[1])
print(c[2])

c[0]=10
c[1]=20
c[2]=30

print("Value of c is",c)

print(c[0])
print(c[1])
print(c[2])
'''
print("Value of a is",a)
a.append(4)
print("Value of a is",a)

a.insert(0,0)
print("Value of a is",a)
'''
a.insert(3,2.5)
print("Value of a is",a)

c.insert(3,'A')
print("Value of c is",c)

print(c[-1])

c.insert(-1,7)
print("Value of c is",c)
'''
c=[5,4,3,2,1,0]
print("Value of c is",c)
'''
#c.sort()
#print("Value of c is",c)


c.pop(2)
print("Value of c is",c)

print(6 not in c)
print(5 in c)

c.remove(5)
print("Value of c is",c)

'''

print(min(c))
print(max(c))
print(len(c))

l=c[1:4]
print(l)

l1=[0,1,2,3]
l2=[4,5,6,7]
print(l1)
print(l2)
l3=l1+l2
print(l3)
l3=l1*3 # l1+l1+l1
print("l3 is",l3)
l4=l1+l1+l1
print("l4 is",l4)
