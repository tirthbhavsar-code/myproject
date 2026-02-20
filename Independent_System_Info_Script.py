import platform
import os

print("System Information")
print("-------------------")

print("OS Name:", os.name)
print("System:", platform.system())
print("Release:", platform.release())
print("Processor:", platform.processor())