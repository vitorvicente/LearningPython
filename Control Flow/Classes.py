class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("Hello, my name is", self.name)


p1 = Person("John", 36)

print(p1.name)

p1.intro()
