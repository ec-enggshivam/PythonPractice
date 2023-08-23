import sys

print(sys.argv)
for i in range(len(sys.argv)):
    print(sys.argv[i])

x = (1,2,3)
print(type(x))
x = (1,)
print(type(x))
x = 1
print(type(x))
x = 1,
print(type(x))
