f = open("demofile.txt", "r")
print(f.read())
f.close()

a = open("demofile.txt", "r")
print(a.read(5))
a.close()

b = open("demofile.txt", "r")
print(b.readline())
print(b.readline())
b.close()

c = open("demofile.txt", "r")
for x in c:
    print(x)
c.close()

