fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

print("\n")

for x in "banana":
    print(x)

print("\n")

for x in fruits:
    print(x)
    if x == "banana":
        break

print("\n")

for x in fruits:
    if x == "banana":
        continue
    print(x)

#  Range Function

print("\n")

for x in range(6):
    print(x)

print("\n")

for x in range(2, 6):
    print(x)

print("\n")

for x in range(2, 30, 3):
    print(x)

print("\n")

for x in range(6):
    print(x)
else:
    print("Finally finished!")

#  Nested Loops

print("\n")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

#  Pass statement

print("\n")

for x in [0, 1, 2]:
    pass
