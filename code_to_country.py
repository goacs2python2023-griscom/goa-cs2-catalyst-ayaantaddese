import csv

def converter_cc(airport_code):
    with open("airport_data.csv", 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header line
        for row in reader:
            if row[4] == airport_code:
                return row[3]
    return None

file = open("flightpaths.txt", "r")
file1 = open("countrypaths.txt","w")
for line in file:
    