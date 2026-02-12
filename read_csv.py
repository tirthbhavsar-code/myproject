import csv

with open("C:\\Users\\91875\\OneDrive\\Documents\\data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
