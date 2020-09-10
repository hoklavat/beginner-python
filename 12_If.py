#12- If, Elif, Else

x = 5
if x > 5:
    print("x is greater than 5")
    print(x*5)
elif x == 5:
    print("x is equal to 5")
else:
    print("x is not greater than 5")
if x == 5 and type(x) is int:
    print("x is equal to 5. x is integer.")
elif x == 10 and type(x) is int:
    print("x is equal to 10. x is integer.")