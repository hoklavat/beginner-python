#18- Function

def function1(x): #parameter x
    "This is our first function."
    print(x)
  
function1("Hello World!") #argument Hello World!

def function2(x, y, z = 3):
    return(x+y+z)

print(function2("Hello ", "World", "!"))
print(function2(y = 1, x = 5))

def function3(x, *args):
    print(x)
    for argument in args:
        print(argument)

function3("Hello", 1, 2, 3)