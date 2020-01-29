#  Basic Tuple Manipulation
print("Basic Tuple Manipulation:")
print("t = ('apple', 'banana', 'cherry')\n")

t = ("apple", "banana", "cherry")

print("t[1] =", t[1])
print("t[-1] =", t[-1])
print("t[1:2] =", t[1:2])
print("t[:-1] =", t[:-1])
print("len(t) =", len(t))
print("t.count('apple') =", t.count("apple"))
print("t.index('apple') =", t.index("apple"))

#  Change Tuple Values
t1 = list(t)
t1[1] = "kiwi"
t = tuple(t1)
print(t)

#  Loop Through Tuples
for x in t:
    print(x)

#  Check if Item Exists
if "apple" in t:
    print("Yes")

#  Create a One Item Tuple
t2 = ("apple",)
print(type(t2))

#  Combine Two Tuples
t3 = ("a", "b" , "c")
t4 = (1, 2, 3)
t5 = t3 + t4
print(t5)





