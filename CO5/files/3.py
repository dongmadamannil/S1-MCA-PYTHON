import csv
listofcsv = []
csv_file=open('file2.csv') 
file_obj = csv.reader(csv_file)
for rows in file_obj:
      listofcsv.append(rows)

print(listofcsv)
