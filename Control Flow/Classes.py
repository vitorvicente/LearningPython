class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("Hello, my name is", self.name)


p1 = Person("John", 36)

print(p1.name)

p1.intro()


class Student(Person):
    def __init__(self, name, age, g):
        self.grade = g
        super().__init__(name, age)


p2 = Student("Tom", 19, 2022)

p2.intro()
