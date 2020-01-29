a = 2
b = 5
t = True
f = False

#  Basic IF / ELIF / ELSE
if b > a:
    print("b > a")
elif b == a:
    print("b == a")
else:
    print("b < a")

#  Shorthand IF / ELIF / ELSE
if a > b: print("a > b")

print("a > b") if a > b else print("a <= b")

print("a > b") if a > b else print("a < b") if a < b else print("a == b")

#  Multiple conditions
if a < b and t:
    print("a > b and t")

if f or t:
    print("f or t")

#  Nested ifs
if t:
    print("t")
    if a < b:
        print("a < b")
    else:
        print("a >= b")

#  Pass statement
if t:
    pass
