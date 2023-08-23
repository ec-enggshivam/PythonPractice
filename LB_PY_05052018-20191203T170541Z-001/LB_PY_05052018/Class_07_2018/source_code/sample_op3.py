"""
val=print("Hello world")

print(val)



val=1
sum=0
def print_10_nat(N):
    global val
    global sum
    if(val<=N):
        print(val,end=' ')
        sum=sum+val
        val=val+1
        print_10_nat(N)
    else:
        print("Sum is",sum)


print_10_nat(6)

"""


def Concat(a="hi", b="hello", c="good", d="morning"):
    result = a + ' ' + b + ' ' + c + ' ' + d
    print(result)


Concat("hi", "hello", "good", "morning")
Concat()
Concat("111")
Concat("111", '222')
Concat("111", 'b', '333')
Concat("111", '222', '333', '444')
