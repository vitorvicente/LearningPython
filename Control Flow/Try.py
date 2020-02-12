try:
    print(x)
except:
    print("An exception occurred")


try:
    print(y)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")


try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished")


#x = -1
#if x < 0:
#    raise Exception("Sorry, no numbers below zero")

#x = "hello"
#if not type(x) is int:
#    raise TypeError("Only integers are allowed")
