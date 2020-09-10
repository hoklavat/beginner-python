#25- Lambda Expressions

a = lambda x, y: x * y //lambda arguments: return_value conditions
print(a)
print(type(a))
print(a(2,5))

def myfunc(mylist):
    list_xy = []
    for x in range(10):
        for y in range(5):
            result = x * y
            list_xy.append(result)
    return list_xy + mylist
    
print(myfunc([100, 101, 102]))

b = lambda mylist: [x * y for x in range(10) for y in range(5)] + mylist
print(b([100, 101, 102]))

def product10(a):
    return a * 10

r1 = range(10)
print(list(map(product10, r1)))
print(list(map(lambda a: a * 10, r1)))
print(list(filter(lambda a: a > 5, r1)))