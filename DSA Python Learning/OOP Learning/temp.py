import csv
with open("C:\\Shreyansh_C\\DSA Python practice\\OOP Learning\\temp.csv","r") as f:
    reader=csv.DictReader(f)
    reader=list(reader)
print(reader)