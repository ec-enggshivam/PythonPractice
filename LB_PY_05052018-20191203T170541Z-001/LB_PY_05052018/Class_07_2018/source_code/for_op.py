import random

l=[2,4,6,8,10]

#for i in range(10):
for i in l:
    if(i==4):
        continue
    var=random.randrange(1,11)
    print("value of i is",i,"random number is",var,"and sqr is", var*var)
    if(i==5):
        break

else:
    print("completed")


