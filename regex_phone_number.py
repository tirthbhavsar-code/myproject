import re

num = input("Enter number: ")

if re.fullmatch(r"\d{10}", num):
    print("Valid number")
else:
    print("Invalid")
