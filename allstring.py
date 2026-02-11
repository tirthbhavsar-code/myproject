text = "python scripting"

# 1. Upper & lower
print("\nUpper:", text.upper())
print("Lower:", text.lower())

# 2. Title & capitalize
print("Title:", text.title())
print("Capitalize:", text.capitalize())

# 3. Length
print("Length:", len(text))

# 4. Replace
print("Replace:", text.replace("python", "java"))

# 5. Find position
print("Find:", text.find("script"))

# 6. Count word
print("Count:", text.count("p"))

# 7. Check start & end
print("Starts with python:", text.startswith("python"))
print("Ends with ing:", text.endswith("ing"))

# 8. Check alphabet/number
a = "Python"
b = "12345"

print("\nIs alpha:", a.isalpha())
print("Is digit:", b.isdigit())

# 9. Remove space
c = "   hello BinaryPenguin   "
print("Strip:", c.strip())

# 10. Split string
d = "apple,banana,mango"
print("Split:", d.split(","))

# 11. Join string
list1 = ["Python", "is", "easy"]
print("Join:", " ".join(list1))

# 12. Index access
name = "Python"
print("\nFirst letter:", name[0])
print("Last letter:", name[-1])

# 13. Loop string
print("\nLoop string:")
for i in name:
    print(i)

# 14. f-string
myname = "Tirth"
age = 25
print(f"\nMy name is {myname} and age is {age}")


