"""
def Add(a,b):
    return a+b

def Sub(a,b):
    return a-b

def Mul(a,b):
    return a*b

def Div(a,b):
    return a/b
"""
Add = lambda a, b: a + b
Sub = lambda a, b: a - b
Mul = lambda a, b: a * b
Div = lambda a, b: a / b

cal_d = {1: Add, 2: Sub, 3: Mul, 4: Div}
cal_op = ['+', '-', '*', '/']

while True:
    print("1.Add\n2.Sub\n3.Mul\n4.Div\n5.Exit")
    Op = int(input("Select any one Operation"))
    if (Op == 5):
        print("Thanks for using the Calculator")
        break
    elif (Op >= 1 and Op < 5):
        val1 = int(input("Enter the first value"))
        val2 = int(input("Enter the Second value"))
        Result = cal_d[Op](val1, val2)
        # 1=>Add(val1,val2)
        # 2=>Sub(val1,val2)
        print("Result of ", val1, cal_op[Op - 1], val2, Result)
    else:
        print("Invalid input")
