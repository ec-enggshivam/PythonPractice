
'''
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]

sum = lambda a,b: a+b

print("l1",l1)
print('l2',l2)

l3=list(map(sum,l1,l2))
print("l3",l3)

L=[1,2,3,4,5]
print("L",L)
sqa = lambda a: a*a

L1=list(map(sqa,L))
print("L1",L1)

import functools
L=[1,2,3,4,5]

sum = lambda a,b: a+b

result=functools.reduce(sum,L)

print("Result",result)


L=[1,2,3,4,5,6]

is_even= lambda a : True if(a%3==0) else False

print("L",L)
L1=list(filter(is_even,L))
print("L1",L1)
'''
string="hello world abcd mmdm md vlmd "

replace_space=lambda val : '*' if(val==' ') else val
print("string",string)
l1=list(map(replace_space,string))
print(l1)

string1=''.join(l1)
print("string1",string1)
