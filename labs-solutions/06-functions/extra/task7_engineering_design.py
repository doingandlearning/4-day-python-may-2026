# Lab 06 Extra - Task 7: Engineering Design Functions
# Practice with functions for basic engineering calculations

print("=" * 50)
print("Task 7: Engineering Design Functions")
print("=" * 50)

def calculate_stress(force, area):
    """Calculate stress given force and area"""
    stress = force / area
    return stress

def calculate_strain(original_length, change_in_length):
    """Calculate strain given original length and change in length"""
    strain = change_in_length / original_length
    return strain

def calculate_youngs_modulus(stress, strain):
    """Calculate Young's modulus given stress and strain"""
    if strain == 0:
        return float('inf')  # Avoid division by zero
    youngs_modulus = stress / strain
    return youngs_modulus

def calculate_heat_transfer(area, temperature_diff, time, thermal_conductivity):
    """Calculate heat transfer given area, temperature difference, time, and thermal conductivity"""
    heat_transfer = thermal_conductivity * area * temperature_diff * time
    return heat_transfer

def calculate_efficiency(useful_output, total_input):
    """Calculate efficiency percentage given useful output and total input"""
    if total_input == 0:
        return 0
    efficiency = (useful_output / total_input) * 100
    return efficiency

def calculate_power(work, time):
    """Calculate power given work and time"""
    if time == 0:
        return 0
    power = work / time
    return power

def calculate_momentum(mass, velocity):
    """Calculate momentum given mass and velocity"""
    momentum = mass * velocity
    return momentum

# Test the engineering functions
print("Testing engineering design functions:")

# Test stress calculation
force = 1000  # Newtons
area = 0.01   # m²
stress = calculate_stress(force, area)
print(f"Stress with {force}N force on {area}m² area: {stress:.0f} Pa")

# Test strain calculation
original_length = 1.0  # meters
change_in_length = 0.001  # meters
strain = calculate_strain(original_length, change_in_length)
print(f"Strain with {change_in_length}m change in {original_length}m length: {strain:.6f}")

# Test Young's modulus calculation
youngs_modulus = calculate_youngs_modulus(stress, strain)
print(f"Young's modulus: {youngs_modulus:.0f} Pa")

# Test heat transfer calculation
area = 2.0  # m²
temp_diff = 50  # °C
time = 3600  # seconds (1 hour)
thermal_conductivity = 0.6  # W/(m·K)
heat_transfer = calculate_heat_transfer(area, temp_diff, time, thermal_conductivity)
print(f"Heat transfer: {heat_transfer:.0f} J")

# Test efficiency calculation
useful_output = 800  # Watts
total_input = 1000   # Watts
efficiency = calculate_efficiency(useful_output, total_input)
print(f"Efficiency: {efficiency:.1f}%")

# Test power calculation
work = 5000  # Joules
time = 10    # seconds
power = calculate_power(work, time)
print(f"Power: {power:.0f} W")

# Test momentum calculation
mass = 2.0   # kg
velocity = 15  # m/s
momentum = calculate_momentum(mass, velocity)
print(f"Momentum: {momentum:.1f} kg·m/s")

# Additional practical examples
print("\nAdditional practical examples:")

# Material testing
print("Material testing example:")
materials = [
    ("Steel", 200e9, 0.3),      # Young's modulus (Pa), Poisson's ratio
    ("Aluminum", 70e9, 0.33),
    ("Concrete", 30e9, 0.2),
    ("Wood", 12e9, 0.4)
]

test_force = 5000  # N
test_area = 0.005  # m²
test_stress = calculate_stress(test_force, test_area)

print(f"Test stress: {test_stress:.0f} Pa")
for material, youngs_mod, poisson in materials:
    test_strain = test_stress / youngs_mod
    print(f"  {material}: strain = {test_strain:.6f}")

# Heat transfer through different materials
print("\nHeat transfer through different materials:")
wall_area = 10  # m²
temp_diff = 20  # °C
time_period = 3600  # s

materials_thermal = [
    ("Steel", 50),      # W/(m·K)
    ("Aluminum", 205),
    ("Concrete", 1.7),
    ("Wood", 0.12)
]

for material, thermal_cond in materials_thermal:
    heat = calculate_heat_transfer(wall_area, temp_diff, time_period, thermal_cond)
    print(f"  {material}: {heat:.0f} J")

# Machine efficiency analysis
print("\nMachine efficiency analysis:")
machines = [
    ("Motor A", 850, 1000),
    ("Motor B", 750, 900),
    ("Motor C", 920, 1000),
    ("Motor D", 680, 800)
]

for machine, useful, total in machines:
    eff = calculate_efficiency(useful, total)
    print(f"  {machine}: {eff:.1f}% efficiency")

# Structural analysis
print("\nStructural analysis example:")
beam_length = 5.0  # m
beam_area = 0.1    # m²
applied_force = 2000  # N

beam_stress = calculate_stress(applied_force, beam_area)
print(f"Beam stress: {beam_stress:.0f} Pa")

# Safety factor calculation
yield_strength = 250e6  # Pa
safety_factor = yield_strength / beam_stress
print(f"Safety factor: {safety_factor:.1f}")

if safety_factor > 2.0:
    print("  Design is safe (safety factor > 2.0)")
else:
    print("  Design needs review (safety factor < 2.0)")

print("\n" + "=" * 50)
print("Task 7 completed successfully!")
print("=" * 50)
