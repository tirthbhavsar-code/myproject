import os
import time

# 1. USER INPUT
path = input("Enter folder path: ")
days = int(input("Delete files older than how many days?: "))

# 2. CHECK PATH
if not os.path.exists(path):
    print("Folder not found")
    exit()

# 3. CURRENT TIME
now = time.time()
deleted = 0

# 4. CHECK FILES
for root, dirs, files in os.walk(path):
    for file in files:
        file_path = os.path.join(root, file)
        
        # FILE MODIFIED TIME
        file_time = os.stat(file_path).st_mtime
        
        # DAYS CHECK
        if (now - file_time) > (days * 86400):
            print("Deleting:", file_path)
            os.remove(file_path)
            deleted += 1

print("\nTotal files deleted:", deleted)
print("Script finished")
 





 