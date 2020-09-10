#26- Iterator

my_list = [1, 2, 3, 4, 5, 6, 7]
for element in my_list:
    print(element)

#Iterator
my_iter = iter(my_list)
print(type(my_iter))
print(next(my_iter))

#Generator Function
def my_gen(x, y):
    for i in range(x):
        print("i is %d" % i)
        print("y is %d" % y)
        yield i % y

my_object = my_gen(10, 5)
print(my_object)
print(type(my_object))
next(my_object)

gen_exp = (x for x in range(5))
print(gen_exp)
print(type(gen_exp))
next(gen_exp)