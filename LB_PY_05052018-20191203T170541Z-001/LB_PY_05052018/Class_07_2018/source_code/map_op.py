
a={}
b=dict()
c={0:'zero',1:'one',2:'two',3:'three'}
d = dict(one=1, two=2, three=3)
e = dict([('two', 2), ('one', 1), ('three', 3)])

#c[1] 'one'
var=int(input("entre sigle "))
print(c[var])
'''
print("type of a is",type(a))
print("type of b is",type(b))
print("type of c is",type(c))
print("type of d is",type(d))
print("type of e is",type(e))
'''
#print("Value of a is",a)
#print("Value of b is",b)
print("Value of c is",c)
#print("Value of d is",d)
#print("Value of e is",e)

#c[0]='zero'
#print(c[0])
print(c[1])
print(c[2])
print(c[3])
'''
c[0]='Zero'
print("Value of c is",c)
c[0]='zero'

print("Value of c is",c)
c[1]='1'
print("Value of c is",c)
'''
'''
print(d['one'])
print(d['two'])
print(d['three'])

print(e['three'])

del(c[1])

print (c)

c.pop(2)
print (c)
'''
print(c.items())
print(c.keys())
print(c.values())
print(1 in c)

