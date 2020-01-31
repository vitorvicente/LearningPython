#  Basic Dictionaries Manipulation
d = {
  "name": "Vitor",
  "class": 2023,
  "major": "CS"
}
print(d)

print(d["name"])
print(d.get("name"))

d["class"] = 23
print(d)

print(d.items())
print(d.keys())
print(d.values())

if "name" in d:
    print(True)

print(len(d))

d["minor"] = "none"
print(d)

d.pop("minor")
print(d)

d["minor"] = "none"
print(d)

d.popitem()
print(d)

d2 = d.copy()
print(d2)

d2.clear()
print(d2)

#  Other Dictionaries Manipulation

x = ("name", "class", "major")
y = (0)

d3 = dict.fromkeys(x, y)
print(d3)

x = d3.setdefault("class", 2023)
print(x)

d3.update({"class": 2023})
print(d3)

