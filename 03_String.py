#03- String

my_string1 = "This is first string."
print(my_string1)
print(my_string1[0])
print(my_string1[-1])
print(len(my_string1))
print(my_string1.index('i'))
print(my_string1.count('i'))
print(my_string1.find('str'))
print(my_string1.lower())
print(my_string1.upper())
print(my_string1.startswith('T'))
print(my_string1.endswith('T'))
print(my_string1[8:13]) #start-end index
print(my_string1[-7:-1])
print(my_string1[::2])
print(my_string1[::-1]) #reverse order
my_string2 = "  This is second string.  "
print(my_string2.strip())
print(my_string2.strip(" "))
print(my_string2.replace(" ", "*"))
print(my_string2.split(" "))
print("_".join(my_string2))
print(my_string1 + my_string2)
print(my_string1 * 2)
print("." in my_string1)
print("," not in my_string1)
my_string3 = "String: %s, Integer: %d, Double: %.2f" % ("Baris", 5, 3.1)
print(my_string3)
my_string3 = "String: {1}, Integer: {0}, Double: {2}" .format ("Barış", 7, 4.2)
print(my_string3)