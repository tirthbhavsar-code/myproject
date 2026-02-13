class Student:
    def __init__(self, name, age):
        self.name = name     # object attribute
        self.age = age

s1 = Student("Tirth", 23)
s2 = Student("Rahul", 25)

print(s1.name, s1.age)
print(s2.name, s2.age)
