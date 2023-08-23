

print("Debug mode value:",__debug__)
a=int(input("Enter a first value"))
b=int(input("Enter a second value"))
try:
    assert  b!=0, "incorrect value"
except Exception as e :
   print("Exception is:",e)
else:
    c=a/b
    print(c)


'''

    assert  a==3, "incorrect value"
except Exception as e :
   print("Exception is",e)
'''