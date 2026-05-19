cities = set(("Paris", "Rome", "Geneva", "Oslo", "Chennai", "Berlin"))
print(cities)

cities_in_countries_beginning_with_i = {'Rome', 'Chennai', 'Reykjavik'}
print(cities_in_countries_beginning_with_i)

cities.add('London')
cities.add('PaRis')

if 'Belfast' in cities:
    cities.remove('Belfast')

print(cities)

print(cities.intersection(cities_in_countries_beginning_with_i))
print(cities.difference(cities_in_countries_beginning_with_i))

countries = ["Italy", "Italy", "Portugal", "Brazil",
             "Italy", "Germany", "Namibia", "India", "Northern Ireland"]

new_countries = []

for country in countries:
    if country not in new_countries:
        new_countries.append(country)

print(sorted(new_countries))

# [] -> {} (deduplicate) -> [] -> sort it
countries = sorted(list(set(countries)))  # depulicate list
print(countries)







