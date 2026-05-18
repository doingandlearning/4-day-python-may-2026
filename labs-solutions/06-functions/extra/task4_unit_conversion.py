# Lab 06 Extra - Task 4: Unit Conversion Functions
# Practice with functions for common unit conversions

print("=" * 50)
print("Task 4: Unit Conversion Functions")
print("=" * 50)

def meters_to_feet(meters):
    """Convert meters to feet"""
    feet = meters * 3.28084
    return feet

def feet_to_meters(feet):
    """Convert feet to meters"""
    meters = feet / 3.28084
    return meters

def kilograms_to_pounds(kg):
    """Convert kilograms to pounds"""
    pounds = kg * 2.20462
    return pounds

def pounds_to_kilograms(lbs):
    """Convert pounds to kilograms"""
    kg = lbs / 2.20462
    return kg

def liters_to_gallons(liters):
    """Convert liters to gallons"""
    gallons = liters * 0.264172
    return gallons

def gallons_to_liters(gallons):
    """Convert gallons to liters"""
    liters = gallons / 0.264172
    return liters

# Test the conversion functions
print("Testing unit conversion functions:")

# Test length conversions
lengths_m = [1, 5, 10, 100]
print("\nLength conversions (meters to feet):")
for meters in lengths_m:
    feet = meters_to_feet(meters)
    print(f"  {meters} m = {feet:.2f} ft")

# Test reverse conversion
lengths_ft = [3.28, 16.40, 32.81, 328.08]
print("\nLength conversions (feet to meters):")
for feet in lengths_ft:
    meters = feet_to_meters(feet)
    print(f"  {feet} ft = {meters:.2f} m")

# Test mass conversions
masses_kg = [1, 10, 50, 100]
print("\nMass conversions (kilograms to pounds):")
for kg in masses_kg:
    lbs = kilograms_to_pounds(kg)
    print(f"  {kg} kg = {lbs:.2f} lbs")

# Test reverse conversion
masses_lbs = [2.20, 22.05, 110.23, 220.46]
print("\nMass conversions (pounds to kilograms):")
for lbs in masses_lbs:
    kg = pounds_to_kilograms(lbs)
    print(f"  {lbs} lbs = {kg:.2f} kg")

# Test volume conversions
volumes_l = [1, 5, 10, 50]
print("\nVolume conversions (liters to gallons):")
for liters in volumes_l:
    gallons = liters_to_gallons(liters)
    print(f"  {liters} L = {gallons:.2f} gal")

# Test reverse conversion
volumes_gal = [0.26, 1.32, 2.64, 13.21]
print("\nVolume conversions (gallons to liters):")
for gallons in volumes_gal:
    liters = gallons_to_liters(gallons)
    print(f"  {gallons} gal = {liters:.2f} L")

# Additional practical examples
print("\nPractical examples:")

# Room dimensions
room_length_m = 4.5
room_width_m = 3.2
room_length_ft = meters_to_feet(room_length_m)
room_width_ft = meters_to_feet(room_width_m)
print(f"Room dimensions: {room_length_m}m x {room_width_m}m = {room_length_ft:.1f}ft x {room_width_ft:.1f}ft")

# Person's weight
weight_kg = 70
weight_lbs = kilograms_to_pounds(weight_kg)
print(f"Person's weight: {weight_kg} kg = {weight_lbs:.1f} lbs")

# Car fuel tank
tank_capacity_l = 60
tank_capacity_gal = liters_to_gallons(tank_capacity_l)
print(f"Car fuel tank: {tank_capacity_l} L = {tank_capacity_gal:.1f} gal")

# Round trip conversion test
print("\nRound trip conversion test (should return original values):")
original_m = 10
converted_ft = meters_to_feet(original_m)
back_to_m = feet_to_meters(converted_ft)
print(f"10 m → {converted_ft:.2f} ft → {back_to_m:.2f} m")

original_kg = 25
converted_lbs = kilograms_to_pounds(original_kg)
back_to_kg = pounds_to_kilograms(converted_lbs)
print(f"25 kg → {converted_lbs:.2f} lbs → {back_to_kg:.2f} kg")

print("\n" + "=" * 50)
print("Task 4 completed successfully!")
print("=" * 50)
