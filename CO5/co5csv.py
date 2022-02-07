#co5q4
import csv
with open("trip.csv") as f:
    data=csv.reader(f)
    for row in data:
        print(f'{row[2]}')