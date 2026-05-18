#                   012345678
favourite_number = "forty two"  # str -> string -> ordered list of characters
print(favourite_number)
print(type(favourite_number))

print(favourite_number.upper())
print(favourite_number)

print(favourite_number.ljust(20))
print(favourite_number.center(20))
print(favourite_number.rjust(20))

print(favourite_number.find("two"))
print(favourite_number.find("Jon"))

print("; ".join(["Jon", "Marko", "Leonardo"]))
print(favourite_number.join(["Jon", "Marko", "Leonardo"]))

first_name = "Kevin"
last_name = "Cunningham"

# concatenating -> join strings together
full_name = first_name + " " + last_name
print(full_name)

message = full_name + "has a favourite number which is" + str(42)

message = f"{full_name} has a favourite number which is {42}"
print(message)

print('I can\'t do that')
print("He said, \"I can't do that\"\nThis will be on the next line\nThis on the one after")
print(f'''{full_name} said, "I can't do that"
"Do it anyway" he was told''')
