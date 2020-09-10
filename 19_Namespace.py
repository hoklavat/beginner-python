#19- Namespace

my_var = 10 #Global Namespace

def my_var_func():
    #global my_var
    my_var = 5 #Local Namespace
    print(my_var)
    return(my_var)

print(my_var_func())
print(my_var)

