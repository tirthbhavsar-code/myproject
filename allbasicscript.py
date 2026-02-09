import os
import platform
import datetime

print("===== BASIC PYTHON AUTOMATION SCRIPT =====")

# 1. SYSTEM INFO
print("\n--- SYSTEM INFORMATION ---")
print("OS:", platform.system())
print("OS Version:", platform.version())
print("Machine:", platform.machine())   
print("Processor:", platform.processor())

# 2. CURRENT DATE & TIME
print("\n--- DATE & TIME ---")
now = datetime.datetime.now()
print("Current Date:", now.date())
print("Current Time:", now.time())

# 3. CREATE FOLDER
print("\n--- CREATE FOLDER ---")
folder_name = "demo_folder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder created:", folder_name)
else:
    print("Folder already exists")

# 4. CREATE FILE & WRITE DATA
print("\n--- CREATE FILE ---")
file_path = os.path.join(folder_name, "report.txt")

with open(file_path, "w") as file:
    file.write("Python Automation Report\n")
    file.write("========================\n")
    file.write("OS: " + platform.system() + "\n")
    file.write("Date: " + str(now.date()) + "\n")
    file.write("Time: " + str(now.time()) + "\n")

print("File created:", file_path)

# 5. READ FILE
print("\n--- READ FILE ---")
with open(file_path, "r") as file:
    content = file.read()
    print(content)

# 6. LIST FILES IN FOLDER
print("\n--- FILES IN CURRENT DIRECTORY ---")
files = os.listdir(".")
for f in files:
    print(f)

# 7. USER INPUT
print("\n--- USER INPUT ---")
name = input("Enter your name: ")
print("Hello", name)

# 8. SIMPLE CALCULATOR
print("\n--- CALCULATOR ---")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Add:", num1 + num2)
print("Sub:", num1 - num2)
print("Mul:", num1 * num2)
print("Div:", num1 / num2)

# 9. LOOP EXAMPLE
print("\n--- LOOP 1 to 5 ---")
for i in range(1, 6):
    print("Number:", i)

# 10. AUTO LOG FILE
print("\n--- CREATE LOG ---")
log_file = "log.txt"

with open(log_file, "a") as log:
    log.write(f"Script run at {datetime.datetime.now()}\n")

print("Log saved")
print("\n===== SCRIPT FINISHED =====")
