new_dictionary = {}
print(new_dictionary)
print(type(new_dictionary))

person_list = [{
                "name":"Leonardo",
               "country":"Italy",
               "city": "Udine",
               },
{
                "name":"Marko",
               "city": "Windhoek",
               }
]


for person in person_list:
    print(f"{person["name"]} is from the city of {person["city"]} in the country of {person.get("country", "I don't know")}")

first_person = person_list[0]

print(first_person)
print("name" in first_person)
print("Leonardo" in first_person.keys())
print("Leonardo" in first_person.values())
print(first_person.items())

for item in first_person.items():
    print(f"{item[0]} has the value {item[1]}")

for key, value in first_person.items():
    print(f"{key} has the value {value}")


new_set = set()
name = 4

new_set.add(name)
print(new_set)

name = 6
print(new_set)



new_list = [name]
print(new_list)

name = 5
print(new_list)


new_set.add((1,2,3))
print(new_set)



