import re

text = "My number is 9876543210"

numbers = re.findall(r"\d", text)
print(numbers)
