 
n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)
avg=sum(a)/n
print("Sum of elements in the list: ",sum(a))
print("Average of elements in the list",round(avg,2))
