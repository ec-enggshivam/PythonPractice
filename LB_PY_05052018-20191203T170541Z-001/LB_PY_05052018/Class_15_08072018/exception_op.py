
'''
value=int(input("Enter a value"))
print("Value entered is ",value)
print("Some message.....>>>>")
'''

value1=0
value2=0
try:
    value1 = int(input("Enter a value1"))
    print("Value entered is ", value1)
    print("Some message.....>>>>")
    value2= int(input("Enter a value2"))
    print("Value entered is ", value2)
    value3=value1/value2
    print("Value3 is ",value3)
    import vinay
except (ValueError,ZeroDivisionError):
    print("Enter a proper value")
except ZeroDivisionError:
    print("Value2 can not be zero")
    value2=int(input("Enter a value2"))
    value3 = value1 / value2
    print("Value3 is ", value3)
except ModuleNotFoundError as e:
    print("Module error:",e)
except:
    print("This is common message")



