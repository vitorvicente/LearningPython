a = ["Ford", "Volvo", "BMW"]

print(a[0])

a[0] = "Tesla"

print(len(a))

for x in a:
    print(x)

a.append("Honda")


a.pop(0)

a.remove("Volvo")

b = a.copy()

a.clear()
print(a)

b.append("Honda")
print(b.count("Honda"))

b.extend(["Renault, Buggatti"])

print(b.index("Renault"))

b.reverse()

b.sort()
