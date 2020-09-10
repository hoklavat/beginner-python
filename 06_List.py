#06- List

list1 = []
print(type(list1))
list1 = ["String", 10, 2.5, True, -10]
print(len(list1))
print(list1[2])
list1[2] = "Baris"
print(list1[2])
list2 = [-10, 2.3, 4, 75]
print(min(list2))
print(max(list2))
list2.append(145)
print(list2)
del list2[1]
print(list2)
list2.pop(0)
print(list2)
list2.remove(75)
print(list2)
list2.insert(2, 456)
print(list2)
list1.extend(list2)
print(list1)
print(list1.index(456))
print(list1.count(4))
list2 = [4, 1, -2, 90, 0, -80]
list2.sort()
print(list2)
list2.reverse()
print(list2)
print(sorted(list2))
print(sorted(list2, reverse = True))
print(list1 + list2)
print(list2 * 2)
print(list2[0:3])
print(list2[3:])
print(list2[::2])  #step 2
print(list2[::-1]) #reversed order

