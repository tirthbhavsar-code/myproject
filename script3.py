print("===== SIMPLE PYTHON BASIC SCRIPT =====")

# 1. PRINT
print("\nHello World")
print("Welcome to Python scripting")

# 2. VARIABLES
name = "Tirth"
age = 25
city = "Ahmedabad"

print("\n--- VARIABLES ---")
print("Name:", name)
print("Age:", age)
print("City:", city)

# 3. USER INPUT
print("\n--- USER INPUT ---")
user_name = input("Enter your name: ")
print("Welcome", user_name)

# 4. NUMBER INPUT
print("\n--- NUMBER INPUT ---")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Multiplication:", num1 * num2)

# 5. STRING PRACTICE
print("\n--- STRING PRACTICE ---")
text = "python scripting"

print("Upper:", text.upper())
print("Lower:", text.lower())
print("Length:", len(text))

# 6. DATE & TIME
import datetime

print("\n--- DATE TIME ---")
now = datetime.datetime.now()
print("Current date:", now.date())
print("Current time:", now.time())

# 7. LIST BASIC
print("\n--- LIST ---")
fruits = ["apple", "banana", "mango", "orange"]

print("Fruit list:", fruits)
print("First fruit:", fruits[0])
print("Total fruits:", len(fruits))

# 8. ADD ITEM LIST
fruits.append("grapes")
print("New list:", fruits)

# 9. SIMPLE LOOP
print("\n--- LOOP ---")
for i in range(1, 6):
    print("Number:", i)

# 10. PRINT TABLE
print("\n--- TABLE ---")
n = int(input("Enter number for table: "))
for i in range(1, 11):
    print(n, "x", i, "=", n*i)

# 11. BASIC MATH
print("\n--- MATH ---")
a = 10
b = 5

print("Add:", a+b)
print("Sub:", a-b)
print("Mul:", a*b)
print("Div:", a/b)

# 12. TYPE CHECK
print("\n--- TYPE CHECK ---")
print(type(name))
print(type(age))
print(type(10.5))

# 13. SIMPLE MESSAGE LOOP
print("\n--- MESSAGE LOOP ---")
for i in range(3):
    print("Python is easy")

# 14. END
print("\n===== SCRIPT FINISHED =====")
print("Thank you for using Python")
