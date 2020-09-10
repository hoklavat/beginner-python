#21- File Handling

myfile = open("a:\\Python\\Routers.txt", "r")
print(myfile.mode)
print(myfile.read())
print(myfile.tell())
myfile.seek(0)
print(myfile.tell())
print(myfile.read(5))
myfile.seek(0)
print(myfile.readline())
print(myfile.readline())
myfile.seek(0)
for line in myfile.readlines():
    if line.startswith("A"):
        print(line)
myfile.close()

newfile = open("a:\\Python\\NewFile.txt", "w")
newfile.write("I like Python!\nDo you?")
newfile.writelines(["Cisco", "Juniper", "HP"])
newfile.writelines(("Cisco1", "Juniper1", "HP1"))
newfile.close()
newfile = open("a:\\Python\\NewFile.txt", "a")
newfile.write("This string is appended.")
newfile.close()
newfile = open("a:\\Python\\NewFile.txt", "r+")
newfile.write("Something else")
newfile.seek(0)
print(newfile.read())
newfile.close()
print(newfile.closed)

with open("a:\\Python\\NewFile2.txt", "w") as f: #file automatically closed
    f.write("Hello Python!")

print(f.closed)