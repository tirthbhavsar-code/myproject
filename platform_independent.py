import os

print("Python Automation Script Started")

# folder name
folder_name = "MyFiles"

# check folder exists or not
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder created:", folder_name)
else:
    print("Folder already exists")

# create file inside folder
file_path = os.path.join(folder_name, "demo.txt")

# write data in file
with open(file_path, "w") as file:
    file.write("Hello! This file created using Python automation.\n")
    file.write("Python is platform independent.")

print("File created and data written successfully")
