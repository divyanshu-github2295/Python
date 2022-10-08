import csv
import sys
from tabulate import tabulate

file = open(sys.argv[1], "r")
reader = csv.DictReader(file)
pizzza = []
if sys.argv[1] == "sicilian.csv":
    for row in reader:
        pizzza.append({"Sicilian Pizza":row["Sicilian Pizza"], "Small":row["Small"], "Lagre":row["Large"]})
elif sys.argv[1] == "regular.csv":
    for row in reader:
        pizzza.append({"Regular Pizza":row["Regular Pizza"], "Small":row["Small"], "Lagre":row["Large"]})

print(tabulate(pizzza, headers="keys", tablefmt="grid"))