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

shared_connections = {}

for country1 in connections:
    for country2 in connections:
        if country1 != country2:
            shared_edges = len(connections[country1].intersection(connections[country2]))
            if shared_edges > 0:
                pair = tuple(sorted([country1, country2]))
                shared_connections[pair] = shared_edges

sorted_connections = sorted(shared_connections.items(), key=lambda x: x[1], reverse=True)

with open('connections.txt', 'w') as txtfile:
    for (country1, country2), num_shared_edges in sorted_connections:
        txtfile.write(f"{country1} + {country2}: {num_shared_edges}\n")
