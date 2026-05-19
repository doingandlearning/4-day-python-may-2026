def add(a, b):
    return a + b

add_alt = lambda a, b: a + b

print(add(1,2))
print(add_alt(1,2))

cities_and_temperatures = [
    ("Geneva", 18),
    ("Zurich", 16),
    ("Paris", 22),
    ("London", 15),
    ("New York", 24),
    ("Tokyo", 27),
    ("Sydney", 20),
]

def get_temperature(item):
    return item[1]

def get_length_of_city_name(item):
    return len(item[0])

print(sorted(cities_and_temperatures, key=lambda item: item[1]))

