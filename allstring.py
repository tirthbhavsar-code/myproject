text = "python scripting"

# 1. Upper & lower convert krva
print("\nUpper:", text.upper())
print("Lower:", text.lower())

# 2. Title & capitalize krva
print("Title:", text.title())
print("Capitalize:", text.capitalize())

# 3. Length count krva
print("Length:", len(text))

# 4. Replace krva mate
print("Replace:", text.replace("python", "java"))

# 5. Find position mate
print("Find:", text.find("script"))

# 6. Count word ketla word che string ma check krva
print("Count:", text.count("p"))

# 7. Check start & end
print("Starts with python:", text.startswith("python"))
print("Ends with ing:", text.endswith("ing"))

# 8. Check alphabet/number
a = "Python"
b = "12345"

print("\nIs alpha:", a.isalpha())
print("Is digit:", b.isdigit())

# 9. Remove space krva
c = "   hello BinaryPenguin   "
print("Strip:", c.strip())

# 10. Split string mate
d = "apple,banana,mango"
print("Split:", d.split(","))

# 11. Join string
list1 = ["Python", "is", "easy"]
print("Join:", " ".join(list1))

# 12. Index access krva
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


