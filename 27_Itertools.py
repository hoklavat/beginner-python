#27- Itertools

from itertools import *

list1 = [1, 2, 3, 'a', 'b', 'c']
list2 = [101, 102, 103, 'X', 'Y']

print(chain(list1, list2))
print(list(chain(list1, list2)))
for i in chain(list1, list2):
    print(i)
    
for i in count(10, 2.5):
    if i <= 50:
        print(i)
    else:
        break

x = range(10, 15)
y = 10
for i in cycle(x):
    print(i)
    y-=1
    if(y == 0):
        break

print(list(filterfalse(lambda x: x < 5, [0, 1, 2, 3, 4, 5, 6, 7])))
print(list(range(10))[2:9:2])
print(list(islice(range(10), 2, 9, 2)))