import re

pattern = re.compile("Python")

text = "Python is easy"

result = pattern.search(text)

if result:
    print("Found")
