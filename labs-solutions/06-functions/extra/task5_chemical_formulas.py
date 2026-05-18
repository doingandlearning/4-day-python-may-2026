# Lab 06 Extra - Task 5: Chemical Formula Functions
# Practice with functions for basic chemistry calculations

print("=" * 50)
print("Task 5: Chemical Formula Functions")
print("=" * 50)

import math

def calculate_molar_mass(atomic_masses):
    """Calculate total molar mass from atomic masses"""
    total_mass = sum(atomic_masses)
    return total_mass

def calculate_moles(mass, molar_mass):
    """Calculate number of moles given mass and molar mass"""
    moles = mass / molar_mass
    return moles

def calculate_concentration(moles, volume):
    """Calculate molarity given moles and volume in liters"""
    concentration = moles / volume
    return concentration

def calculate_ph(hydrogen_ion_concentration):
    """Calculate pH from hydrogen ion concentration"""
    ph = -math.log10(hydrogen_ion_concentration)
    return ph

def calculate_mass_from_moles(moles, molar_mass):
    """Calculate mass given moles and molar mass"""
    mass = moles * molar_mass
    return mass

def calculate_volume_from_concentration(moles, concentration):
    """Calculate volume given moles and concentration"""
    volume = moles / concentration
    return volume

# Test with CO₂ (Carbon Dioxide)
print("Testing chemical formula functions with CO₂:")

# CO₂: 1 Carbon (12.01) + 2 Oxygen (16.00 each)
co2_atomic_masses = [12.01, 16.00, 16.00]
co2_molar_mass = calculate_molar_mass(co2_atomic_masses)
print(f"CO₂ molar mass: {co2_molar_mass:.2f} g/mol")

# Test moles calculation
mass_co2 = 44.0  # grams
moles_co2 = calculate_moles(mass_co2, co2_molar_mass)
print(f"Moles of CO₂ in {mass_co2}g: {moles_co2:.3f} mol")

# Test concentration calculation
volume = 1.0  # liters
concentration_co2 = calculate_concentration(moles_co2, volume)
print(f"Concentration of CO₂ in {volume}L: {concentration_co2:.3f} M")

# Test pH calculation
h_ion_concentrations = [0.001, 0.0001, 0.00001, 0.000001]
print(f"\npH calculations:")
for h_concentration in h_ion_concentrations:
    ph = calculate_ph(h_concentration)
    print(f"  [H⁺] = {h_concentration} M → pH = {ph:.1f}")

# Test with different compounds
print(f"\nTesting with different compounds:")

# Water (H₂O)
h2o_atomic_masses = [1.01, 1.01, 16.00]
h2o_molar_mass = calculate_molar_mass(h2o_atomic_masses)
print(f"H₂O molar mass: {h2o_molar_mass:.2f} g/mol")

# Methane (CH₄)
ch4_atomic_masses = [12.01, 1.01, 1.01, 1.01, 1.01]
ch4_molar_mass = calculate_molar_mass(ch4_atomic_masses)
print(f"CH₄ molar mass: {ch4_molar_mass:.2f} g/mol")

# Sodium Chloride (NaCl)
nacl_atomic_masses = [22.99, 35.45]
nacl_molar_mass = calculate_molar_mass(nacl_atomic_masses)
print(f"NaCl molar mass: {nacl_molar_mass:.2f} g/mol")

# Practical examples
print(f"\nPractical examples:")

# Calculate mass needed for specific moles
desired_moles = 0.5
mass_needed = calculate_mass_from_moles(desired_moles, co2_molar_mass)
print(f"Mass needed for {desired_moles} mol of CO₂: {mass_needed:.2f} g")

# Calculate volume needed for specific concentration
desired_concentration = 0.1  # M
volume_needed = calculate_volume_from_concentration(moles_co2, desired_concentration)
print(f"Volume needed for {desired_concentration} M CO₂: {volume_needed:.2f} L")

# pH of common solutions
common_solutions = [
    ("Stomach acid", 0.01),
    ("Lemon juice", 0.001),
    ("Vinegar", 0.0001),
    ("Pure water", 0.0000001),
    ("Baking soda", 0.00000001)
]

print(f"\npH of common solutions:")
for solution, h_concentration in common_solutions:
    ph = calculate_ph(h_concentration)
    print(f"  {solution}: pH = {ph:.1f}")

# Buffer solution example
print(f"\nBuffer solution example:")
acid_concentration = 0.1  # M
base_concentration = 0.1  # M
# Simplified pH calculation for a buffer
ph_buffer = 7.0 + math.log10(base_concentration / acid_concentration)
print(f"Buffer with {acid_concentration}M acid and {base_concentration}M base: pH = {ph_buffer:.1f}")

print("\n" + "=" * 50)
print("Task 5 completed successfully!")
print("=" * 50)
