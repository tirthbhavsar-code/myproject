import re

text = "My age is 25"

result = re.findall(r"\d", text)
print(result)
