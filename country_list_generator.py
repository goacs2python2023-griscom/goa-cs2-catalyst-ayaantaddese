with open('airport_data.csv', 'r') as file:
    lines = file.readlines()
    countries = set()
    
    for line in lines:
        country = line.strip().split(',')[3]
        if '"' in country:
            country = line.strip().split(',')[4]
        countries.add(country)

sorted_countries = sorted(countries)

with open('country_list.txt', 'w') as file:
    for country in sorted_countries:
        file.write(country + '\n')
