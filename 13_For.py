#13- For

Names = ["Ali", "Ahmet", "Mehmet", "George", "Michael"]
for name in Names:
    print(name)
else:
    print("The End")

Number = "1234567890"
for n in Number:
    print(n)

Range = range(10)
for n in Range:
    print(n * 2)
    
for e in range(len(Names)):
    print(Names[e])
    
for index, element in enumerate(Names):
    print(index, element)