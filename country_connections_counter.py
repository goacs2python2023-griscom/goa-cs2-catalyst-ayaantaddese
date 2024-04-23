connections = {}

def add_edge(country1, country2):
    connections.setdefault(country1, set()).add(country2)
    connections.setdefault(country2, set()).add(country1)

with open('countrypaths.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if not line: continue
        countries = line.split('-', 1)
        if len(countries) != 2: continue
        country1, country2 = countries
        add_edge(country1, country2)

country_connections = {country: len(connections[country]) for country in connections}
sorted_countries = sorted(country_connections.items(), key=lambda x: x[1], reverse=True)

for country, num_connections in sorted_countries:
    print(f"{country}: {num_connections} connections")
