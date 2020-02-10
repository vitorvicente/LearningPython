import json

x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])

x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
y = json.dumps(x)
print(y)

print(json.dumps({"name": "John", "age": 30}))  # dic
print(json.dumps(["apple", "bananas"]))  # list
print(json.dumps(("apple", "bananas")))  # tuple
print(json.dumps("hello"))  # string
print(json.dumps(42))  # int
print(json.dumps(31.76))  # float
print(json.dumps(True))  # True
print(json.dumps(False))  # False
print(json.dumps(None))  # None

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
print(json.dumps(x, indent=4))
print(json.dumps(x, indent=4, separators=(". ", " = ")))
print(json.dumps(x, indent=4, sort_keys=True))


