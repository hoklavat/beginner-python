#07- Set, Frozen Set

list1 = [1, 6, 3, 3, 7, 9, 2, 5]
print(list1)
print(set(list1))
set1 = {1, 5, 8, 4, 7, 8, 1, 0} #duplicate elements reduced to one
print(set1)
print(type(set1))
print(len(set1))
print(8 in set1)
set1.add(16)
print(set1)
set1.remove(8)
print(set1)
set2 = {1, 2, 3, 4, 5}
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.union(set2))
print(set1.pop())
set2.clear()
print(set2)
fs1 = frozenset([1, 2, 3, 4, 5]) #unmodifiable set
fs2 = frozenset([6, 7 , 8, 9, 0])
print(fs1.union(fs2))
