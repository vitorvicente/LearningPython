#  List manipulation
print("Basic List Manipulation:")
print("l1 = [1,3,2,4,5]\n")

l1 = [1, 3, 2, 4, 5]

print("l1[0] =", l1[0])
print("len(l1) =", len(l1))
print("sorted(l1) =", sorted(l1))

l1.append(6)
print("l1.append(6) =", l1)

l1.extend([7, 8, 9])
print("l1.extend[7, 8, 9] =", l1)

l1.insert(0, 0)
print("l1.insert(0, 0) =", l1)

l1.remove(3)
print("l1.remove(3) =", l1)

print("l1.pop =", l1.pop())

l1.reverse()
print("l1.reverse =", l1)

print("l1.count(1) =", l1.count(1))
print("l1.index(5)=", l1.index(5))

print("l1[1:4] =", l1[1:4])
print("l1[3:] =", l1[3:])
print("l1[:4] =", l1[:4])
print("l1[1:-2] =", l1[1:-2])

print("l1.copy() =", l1.copy())

l1.clear()
print("l1.clear() =", l1)

