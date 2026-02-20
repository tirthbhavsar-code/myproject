import os
import shutil

source_folder = "D:/Data"
destination_folder = "D:/Backup"

for file in os.listdir(source_folder):
    if file.endswith(".txt"):
        full_path = os.path.join(source_folder, file)
        shutil.copy(full_path, destination_folder)

print("All txt files copied successfully")
