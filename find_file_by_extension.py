import os


# 1. USER INPUT
path = input("Enter folder path: ")
ext = input("Enter file extension (example: .txt or .pdf): ")

# 2. CHECK PATH
if not os.path.exists(path):
    print("Path not found")
    exit()

print("\nFiles found:\n")

# 3. FIND FILES
found = False

for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(ext):
            print(os.path.join(root, file))
            found = True

if not found:
    print("No files found with this extension")

print("\n Search completed")
