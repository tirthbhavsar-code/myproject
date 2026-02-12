import re

text = "Python is easy"

result = re.search("Python", text)

if result:
    print("Found")
else:
    print("Not found")
