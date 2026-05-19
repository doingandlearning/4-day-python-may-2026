people = [
    {"name": "Alice", "age": 25, "salary": 70000},
    {"name": "Bob", "age": 17, "salary": 0},
    {"name": "Charlie", "age": 32, "salary": 120000},
    {"name": "Diana", "age": 15, "salary": 0},
    {"name": "Eve", "age": 45, "salary": 95000},
]

names = []
for person in people:
    if person["salary"] > 0:
        names.append(person["name"])
print(names)

def get_name(person):
    return person["name"]

names_map = map(get_name,
                     filter(lambda p: p["salary"] > 0, people))
print(names_map)

names_comp = [p.get("name") for p in people if p["salary"] > 0]
print(names_comp)

