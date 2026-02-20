import os

path = "C:\\Users\\Tirth\\Desktop"

for root, dirs, files in os.walk(path):
    print("Current Path:", root)
    print("Folders:", dirs)
    print("Files:", files)
    print("--------------")
