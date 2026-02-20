import os
import platform
import datetime

print("===== AUTOMATION SCRIPT =====")

print("OS Name:", platform.system())
print("User:", os.getlogin())

now = datetime.datetime.now()
print("Date:", now.date())
print("Time:", now.time())

print("Script running successfully on this OS")
