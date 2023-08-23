
l1=[0,1,2,3]
print("l1 is",l1)
l2=l1
print("l1 has ",id(l1))
print("l2 has ",id(l2))


'''
l2=l1
print("l1 is",l1)
print("l2 is",l2)

l1[0]=10
print("l1 is",l1)
print("l2 is",l2)
'''
l2=l1

l3=l1[:]
l4 = list(l1)
print("l3 has ",id(l3))
l1[1]=20
print("l1 is",l1)
print("l3 is",l3)
print("l4 is",l4)

#print(l4[0])
#print(l4[1])

l=[0,1,2,3,4,5,6]
#length=len(l)
for i in range(len(l)):
#for i in range(length):
    print(l[i])




