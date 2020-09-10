#08- Tuple

tuple1 = ()
print(type(tuple1))
tuple1 = (9)
print(type(tuple1))
tuple1 = (1, 2, 3, 4, 5)
print(type(tuple1))
print(tuple1[1])
#tuple1[1] = 0 Error: unmutable elements
(a, b, c, d, e) = tuple1
print(a)
print(len(tuple1))
print(max(tuple1))
print(min(tuple1))
print(tuple1 + (1 ,2 ,3))
print(tuple1 * 2)
print(tuple1[3:5])
del tuple1