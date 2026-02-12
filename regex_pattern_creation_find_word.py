import re

text = "Python scripting"

result = re.search("Python", text)

if result:
    print("Word found")
