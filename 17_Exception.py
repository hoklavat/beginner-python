#17- Exception Handling

#for i in range(10) Syntax Error

#for i in rnge(10): Name Error
#    print(i)

#print(4/0) Zero Division Error

for i in range(5):
    try:
        print(i/0)
    except ZeroDivisionError as e:
        print(e, "-> Division by zero is not allowed.")
    except NameError:
        print("Name Error.")
    except ValueError:
        print("Value Error.")
    except:
        print("Any Other Exception.")
    else:
        print("No Exception.")
    finally:
        print("Exception or Not.")
