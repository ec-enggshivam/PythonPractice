class MyException(Exception):
    def __str__(self):
        return "MyException"


def sample_exp():
    l=[1,2,3,4,5,6,7,8,9,10,11]
    try:
      #import vinay
      #raise MyException
      x=int(input("Enter the first number"))
      y=int(input("Enter the second number"))
      z=x/y
      print(z)
      print(l[10])

    #except(ValueError,IndexError,ZeroDivisionError):
    #  print("Inside the tupple exp")
    except ValueError:
      print("I get VE")
    except IndexError:
      print("I get IE")
    except ZeroDivisionError:
      print(" I get ZDE")
      raise MyException
    except Exception as e:
      print ("I got some other error:",e)
      x = int(input("Enter the first number"))
    else:
      print ("No execption")
      #raise MyException
      x = int(input("Enter the first number"))
    finally:
      print("I do always")
      raise MyException

try:
    sample_exp()
except MyException as e:
    print(e)
except:
    print("common message")

print("Rest of app goes here")
