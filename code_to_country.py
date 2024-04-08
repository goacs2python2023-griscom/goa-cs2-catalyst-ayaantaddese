import csv

def converter_cc(airport_code):
    with open("airport_data.csv", 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) 
        for row in reader:
            if row[4] == airport_code:
                return row[3]
    return None

with open("flightpaths.txt", "r") as file, open("countrypaths.txt", "w") as file1:
    for line in file:
        parts = line.strip().split("-")
        file1.write(converter_cc(parts[0]) + "-" + converter_cc(parts[1]) + "\n")
