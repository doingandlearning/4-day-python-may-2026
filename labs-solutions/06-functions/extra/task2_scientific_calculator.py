# Lab 06 Extra - Task 2: Scientific Calculator Functions
# Practice with functions for basic scientific calculations

print("=" * 50)
print("Task 2: Scientific Calculator Functions")
print("=" * 50)

import math

def calculate_area_circle(radius):
    """Calculate the area of a circle"""
    area = math.pi * radius ** 2
    return area

def calculate_volume_sphere(radius):
    """Calculate the volume of a sphere"""
    volume = (4/3) * math.pi * radius ** 3
    return volume

def calculate_density(mass, volume):
    """Calculate density given mass and volume"""
    density = mass / volume
    return density

def calculate_pressure(force, area):
    """Calculate pressure given force and area"""
    pressure = force / area
    return pressure

def calculate_kinetic_energy(mass, velocity):
    """Calculate kinetic energy given mass and velocity"""
    kinetic_energy = 0.5 * mass * velocity ** 2
    return kinetic_energy

# Test the functions with sample values
print("Testing scientific calculator functions:")

# Test circle area
radius = 5.0
area = calculate_area_circle(radius)
print(f"Area of circle with radius {radius}: {area:.2f} square units")

# Test sphere volume
radius = 3.0
volume = calculate_volume_sphere(radius)
print(f"Volume of sphere with radius {radius}: {volume:.2f} cubic units")

# Test density calculation
mass = 100.0  # kg
volume = 0.5  # m³
density = calculate_density(mass, volume)
print(f"Density of {mass} kg in {volume} m³: {density:.2f} kg/m³")

# Test pressure calculation
force = 500.0  # Newtons
area = 0.1     # m²
pressure = calculate_pressure(force, area)
print(f"Pressure with {force} N force on {area} m² area: {pressure:.2f} Pa")

# Test kinetic energy calculation
mass = 2.0     # kg
velocity = 10.0  # m/s
kinetic_energy = calculate_kinetic_energy(mass, velocity)
print(f"Kinetic energy of {mass} kg moving at {velocity} m/s: {kinetic_energy:.2f} J")

# Additional test cases
print("\nAdditional test cases:")

# Multiple circle areas
radii = [1, 2, 3, 4, 5]
print("Circle areas for different radii:")
for r in radii:
    area = calculate_area_circle(r)
    print(f"  Radius {r}: {area:.2f} square units")

# Density of different materials
materials = [
    ("Water", 1000, 1.0),      # kg, m³
    ("Iron", 7870, 1.0),       # kg, m³
    ("Aluminum", 2700, 1.0)    # kg, m³
]

print("\nDensities of different materials:")
for material, mass, volume in materials:
    density = calculate_density(mass, volume)
    print(f"  {material}: {density:.0f} kg/m³")

# Kinetic energy at different velocities
velocities = [5, 10, 15, 20]  # m/s
mass = 1.0  # kg
print(f"\nKinetic energy for {mass} kg at different velocities:")
for v in velocities:
    ke = calculate_kinetic_energy(mass, v)
    print(f"  {v} m/s: {ke:.1f} J")

print("\n" + "=" * 50)
print("Task 2 completed successfully!")
print("=" * 50)
