#11- Type Conversion

num1 = 5
str1 = str(5)
print(type(str1))
str2 = "5"
num2 = int(str2)
print(type(num2))
str3 = "2.5"
flt1 = float(str3)
print(type(flt1))
tup1 = (1 ,2, 3)
list1 = list(tup1)
print(type(list1))
list2 = (4, 5, 6)
tup2 = tuple(list2)
print(type(tup2))
set1 = set(list1)
print(type(set1))
print(bin(10))
print(hex(10))
print(int(0b1111)) #int(num_bin ,2)
print(int(0xFF)) #int(num_bin ,16)
