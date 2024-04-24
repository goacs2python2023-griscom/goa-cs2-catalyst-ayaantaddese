import csv

def get_gdp_per_capita(country):
    with open('gdp_data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == country:
                return int(row[3])  
    return None

def process_connection(line):
    parts = line.split(':')
    countries, connections = parts[0].split('+'), int(parts[1].strip())
    country1, country2 = countries[0].strip(), countries[1].strip()    
    gdp_per_capita1, gdp_per_capita2 = get_gdp_per_capita(country1), get_gdp_per_capita(country2)
    
    if gdp_per_capita1 is not None and gdp_per_capita2 is not None and connections >= 2:
        avg_gdp_per_capita = int((gdp_per_capita1 + gdp_per_capita2) / 2)
        return [f"{country1} + {country2}", avg_gdp_per_capita, connections]
    return None

with open('connections.txt', 'r') as file, open("visualization1_data_generator.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    writer.writerow(["Countries", "Average GDP per Capita", "Connections"])  
    
    lines = file.readlines()
    for line in lines:
        x = process_connection(line.strip())
        if x:
            writer.writerow(x)
