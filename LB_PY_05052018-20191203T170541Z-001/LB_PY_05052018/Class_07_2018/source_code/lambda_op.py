def square_fun(a):
    return a * a


square = lambda a: a * a

print(square(5))

abs_val = lambda a: -a if a < 0 else a

print(abs_val(-5))
print(abs_val(8))

Sum = lambda a, b: a + b

print(Sum(2, 3))
