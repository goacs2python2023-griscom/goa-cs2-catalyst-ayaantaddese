import csv

flightpaths = []

with open('airline_network.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    
    for row in csvreader:
        flightpaths.append([row[2],row[4]])

with open('flightpaths.txt', 'w') as txtfile:
    for value in flightpaths:
        txtfile.write(str(value[0]) + "-"+ str(value[1]) + '\n')
