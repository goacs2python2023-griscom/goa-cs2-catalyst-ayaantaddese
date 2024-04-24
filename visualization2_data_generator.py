import csv

def get_gdp(country):
    with open('gdp_data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == country:
                return int(row[1])  
    return None

def process_connection(line):
    parts = line.split(':')
    country, connections = parts[0].strip(), int(parts[1].strip())
    gdp = get_gdp(country)
    
    if gdp is not None and connections >= 5:
        return [country, gdp, connections]
    return None

with open('connections_per_country.txt', 'r') as file, open("visualization2_data_generator.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    writer.writerow(["Countries", "GDP", "Connections"])  # Write headers
    
    lines = file.readlines()
    for line in lines:
        x = process_connection(line.strip())
        if x:
            writer.writerow(x)
