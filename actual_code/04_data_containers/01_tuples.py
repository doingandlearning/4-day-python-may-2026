empty_tuple = ()
empty_tuple = tuple()
print(empty_tuple)
print(type(empty_tuple))

#                0          1          2        3
name_tuple = ("Amira", "Guilherme", "Marko", "Jon", True, 3)

print(name_tuple[1])
print(name_tuple[::-1])  # start:end:step
print(name_tuple[:3])   # start:end
print(name_tuple[2:])  # slicing the tuple

print("Kevin" in name_tuple)
print("Amira" in name_tuple)
print("Guilherme" in name_tuple)

print(name_tuple.count("Guilherme"))
print(name_tuple.count("Leonardo"))

if "Leonardo" in name_tuple:
    print(name_tuple.index("Leonardo"))

for name in name_tuple:
    print(f"{name} is {name_tuple.index(name)} and works at CERN")

coords = (3,4, 5)
x_coord = coords[0]
y_coord = coords[1]
z_coord = coords[2]

# unpacking
x_coord, y_coord, z_coord = coords

particles_detected = ((2,3,4), (1,3,4), (5,4,2), (2,3))

for x, y, z in particles_detected:
    print(f"Particle detected at x ordinate {x}, y ordinate {y}, z ordinate {z}")