#  Data Types
print("Data Types:")

x = "Hello World"
print(x, type(x))

x = 20
print(x, type(x))

x = 20.5
print(x, type(x))

x = 1j
print(x, type(x))

x = ["apple", "banana", "cherry"]
print(x, type(x))

x = ("apple", "banana", "cherry")
print(x, type(x))

x = range(6)
print(x, type(x))

x = {"name" : "John", "age" : 36}
print(x, type(x))

x = {"apple", "banana", "cherry"}
print(x, type(x))

x = frozenset({"apple", "banana", "cherry"})
print(x, type(x))

x = True
print(x, type(x))

x = b"Hello"
print(x, type(x))

x = bytearray(5)
print(x, type(x))

x = memoryview(bytes(5))
print(x, type(x))

print("\n")


#  Setting Specific Data Types
print("Setting Specific Data Types:")

x = str("Hello World")
print(x, type(x))

x = int(20)
print(x, type(x))

x = float(20.5)
print(x, type(x))

x = complex(1j)
print(x, type(x))

x = list(("apple", "banana", "cherry"))
print(x, type(x))

x = tuple(("apple", "banana", "cherry"))
print(x, type(x))

x = range(6)
print(x, type(x))

x = dict(name="John", age=36)
print(x, type(x))

x = set(("apple", "banana", "cherry"))
print(x, type(x))

x = frozenset(("apple", "banana", "cherry"))
print(x, type(x))

x = bool(5)
print(x, type(x))

x = bytes(5)
print(x, type(x))

x = bytearray(5)
print(x, type(x))

x = memoryview(bytes(5))
print(x, type(x))

print("\n")


#  Casting
print("Type Casting:")

x = int(1)
y = int(2.8)
z = int("3")
print(x, y, z)

x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x, y, z, w)

x = str("s1")
y = str(2)
z = str(3.0)
print(x, y, z)

