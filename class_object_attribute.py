class Employee:
    company = "Google"   # class attribute

    def __init__(self, name, salary):
        self.name = name        # object attribute
        self.salary = salary

e1 = Employee("Tirth", 50000)
e2 = Employee("Rahul", 60000)

print("Employee 1:", e1.name, e1.salary, e1.company)
print("Employee 2:", e2.name, e2.salary, e2.company)
