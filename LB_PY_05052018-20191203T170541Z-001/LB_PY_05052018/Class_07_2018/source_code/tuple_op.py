a = ()
b = tuple()
c = (1, 2, 3)
d = 1, 2, 3
e = 1,
f = 1  # int
g = [1, 2, 3]

print("type of a", type(a))
print("type of b", type(b))
print("type of c", type(c))
print("type of d", type(d))
print("type of e", type(e))
print("type of f", type(f))
print("type of g", type(g))

print("\nValue of a", a)
print("Value of b", b)
print("Value of c", c)
print("Value of d", d)
print("Value of e", e)
print("Value of g", g)

# print("Value of a",a)
# print(c[0])
# print(c[1])
# print(c[2])

# c.append(4)
# c[0]=10

# a.append(4)
# a[0]=10

c = (1, 2, 3)
print("\nValue of c", c)
a = list(c)
print("type of a", type(a))
print("Value of a", a)
a.append(4)
print("Value of a", a)
c = tuple(a)
print("Value of c", c)

c = tuple([1, 2, 3])
