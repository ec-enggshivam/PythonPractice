"""
l1=[2,3,4,5,1]
l1.sort(reverse=False)
print("Sorted l1",l1)

l=['Gaurav','Abhishek','Rahul','Krishna']

print(l)

l.sort()
print("Sorted l1",l)

"""
# L=[['Abhishek', 10], ['Gaurav', 11], ('Rahul', 8), ('Krishna', 9)]
L = [('Abhishek', 10), ('Gaurav', 11,), ('Rahul', 8), ('Krishna', 9)]

print(L)

sort_list = lambda val: val[1]
# Syntax of sort() :
# list_name.sort() – it sorts in ascending order
# list_name.sort(reverse=True) – it sorts in descending order
# list_name.sort(key=…, reverse=…) – it sorts according to user’s choice
#
# Parameters:
# By default, sort() doesn’t require any extra parameters. However, it has two optional parameters:#
# reverse – If true, the list is sorted in descending order
# key – function that serves as a key for the sort comparison
#
# Return value:
# It returns a sorted list according to the passed parameter.
L.sort(key=sort_list, reverse=False)
print("After sort", L)
