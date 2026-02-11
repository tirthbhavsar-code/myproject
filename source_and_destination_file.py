# source and destination file
source = "source.txt"
destination = "destination.txt"

# read source file
with open(source, "r") as s:
    data = s.read()

# write into destination file
with open(destination, "w") as d:
    d.write(data)

print("File copied successfully")
