import csv

total_amount = 0
multiplication = 0 

with open("csv/Day54Totals (1).csv") as file2:
  reader = csv.DictReader(file2)
  for row in reader:
    print(row["Cost"], end = "   ")
    print(row["Quantity"], end = "   ")
    multiplication = eval(row["Cost"])*eval(row["Quantity"])
    print(round(multiplication,2))
    total_amount += round(multiplication,2)

print()
print(f"Total Amount = {round(total_amount, 2)}")