import csv

unique_values = set()

with open('airport_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    
    for row in csvreader:
        unique_values.add(row[3])

unique_values = list(unique_values)
unique_values.sort()
with open('country_list.txt', 'w') as txtfile:
    for value in unique_values:
            txtfile.write(value + '\n') 
