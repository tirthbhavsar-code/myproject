import csv

with open("C:\\Users\\91875\\OneDrive\\Documents\\data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print("Name:", row["Name"])
        print("Age:", row["Age"])
        print("City:", row["City"])
        print("------")
