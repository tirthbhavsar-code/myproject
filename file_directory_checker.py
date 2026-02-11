import os

# Take path from user
path = input("Enter folder path: ")

# Check path exists or not
if os.path.exists(path):

    print("\nFiles and Directories in path:\n")

    # Read all items in folder
    for item in os.listdir(path):

        full_path = os.path.join(path, item)

        # Check file
        if os.path.isfile(full_path):
            print("File :", item)

        # Check folder
        elif os.path.isdir(full_path):
            print("Folder :", item)

else:
    print("Path not found")
