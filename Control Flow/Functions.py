def my_function():
    print("Hello from a function")
    return


def my_function_2(a):
    print("Hello from a function", a)
    return


def my_function_3(a="hello"):
    print(a, "Hello from a function")


my_function()
my_function_2("hi")
my_function_3()


def my_function_4():
    return 1


print(my_function_4())


def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)

#  Lambda Functions

x = lambda a: a + 10
print(x(5))

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))


def myfunc(n):
    return lambda a : a * n


mytripler = myfunc(3)

print(mytripler(11))





