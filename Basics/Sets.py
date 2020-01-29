#  Set manipulation
print("Basic Set Manipulation:")
print("s1 = {1,3,2,4,5}\n")

s = {1, 3, 2, 4, 5}

s.add(6)
print("s.add(6) =", s)

s.remove(1)
print("s.remove(1) =", s)

s.update([7, 8, 9])
print("s.update([7, 8, 9]) =", s)

len(s)
print("len(s) =", len(s))

s.discard(2)
print("s.discard(2) =", s)

print("s.pop() =", s.pop())

s.clear()
print("s.clear() =", s)

#  Other Set manipulation
print("Other Set Manipulation:")
print("s2 = {1,3,2,4,5} | s3 = {6,7,8,9,0} | s4\n")

s2 = {1, 3, 2, 4, 5}
s3 = {6, 7, 8, 9, 1}

s4 = s2.union(s3)
print("s4 = s2.union(s3) =", s4)

s4 = s2.copy()
print("s4 = s2.copy() =", s4)

s4 = s2.difference(s3)
print("s4 = s2.difference(s3) =", s4)

s2.difference_update(s3)
print("s2.difference_update(s3) =", s2)

s2 = {1, 3, 2, 4, 5}

s4 = s2.intersection(s3)
print("s4 = s2.intersection(s3) =", s4)

s2.intersection_update(s3)
print("s2.intersection_update(s3) =", s2)

s2 = {1, 3, 2, 4, 5}

print("s2.isdisjoint(s3) =", s2.isdisjoint(s3))
print("s2.issuperset(s3) =", s2.issuperset(s3))

s4 = s2.symmetric_difference(s3)
print("s4 = s2.symmetric_difference(s3) =", s4)

s2.symmetric_difference_update(s3)
print("s2.symmetric_difference_update(s3) =", s2)

x = frozenset({"apple", "banana", "cherry"})
print(x)

