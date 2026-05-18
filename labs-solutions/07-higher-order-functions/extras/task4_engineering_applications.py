# Lab 07 Extra - Task 4: Practical Engineering Applications
# Practice with lambda functions for engineering material selection

print("=" * 50)
print("Task 4: Practical Engineering Applications")
print("=" * 50)

# Sample material data: (material, density, strength, cost_per_kg)
materials = [
    ("Steel", 7850, 400, 2.50),
    ("Aluminum", 2700, 200, 3.20),
    ("Titanium", 4500, 900, 25.00),
    ("Carbon_Fiber", 1600, 600, 45.00),
    ("Wood", 600, 50, 0.80)
]

print("Material properties:")
print("Material        Density(kg/m³)  Strength(MPa)  Cost($/kg)")
print("-" * 55)
for material in materials:
    print(f"{material[0]:<15} {material[1]:<15} {material[2]:<13} {material[3]:<10}")

# Sort materials by strength-to-weight ratio (strength/density)
strength_weight_ratio = sorted(materials, key=lambda x: x[2]/x[1], reverse=True)
print(f"\nMaterials sorted by strength-to-weight ratio (highest first):")
print("Material        Strength/Weight Ratio")
print("-" * 40)
for material in strength_weight_ratio:
    ratio = material[2] / material[1]
    print(f"{material[0]:<15} {ratio:.6f}")

# Find materials cheaper than $5 per kg
cheap_materials = list(filter(lambda x: x[3] < 5.0, materials))
print(f"\nMaterials cheaper than $5/kg:")
for material in cheap_materials:
    print(f"  {material[0]}: ${material[3]:.2f}/kg")

# Sort materials by cost efficiency (strength/cost)
cost_efficiency = sorted(materials, key=lambda x: x[2]/x[3], reverse=True)
print(f"\nMaterials sorted by cost efficiency (strength per dollar):")
print("Material        Strength/Cost Ratio")
print("-" * 40)
for material in cost_efficiency:
    efficiency = material[2] / material[3]
    print(f"{material[0]:<15} {efficiency:.2f}")

# Create a lambda to calculate strength per dollar
strength_per_dollar = lambda material: material[2] / material[3]
print(f"\nStrength per dollar for each material:")
for material in materials:
    spd = strength_per_dollar(material)
    print(f"  {material[0]}: {spd:.2f} MPa/$")

# Sort materials by density (lightest first)
lightest_first = sorted(materials, key=lambda x: x[1])
print(f"\nMaterials sorted by density (lightest first):")
print("Material        Density(kg/m³)")
print("-" * 30)
for material in lightest_first:
    print(f"{material[0]:<15} {material[1]}")

# Additional engineering analysis
print(f"\nAdditional engineering analysis:")

# Find materials suitable for aerospace (high strength, low density)
aerospace_candidates = list(filter(lambda x: x[2] > 300 and x[1] < 3000, materials))
print(f"Aerospace candidates (strength > 300 MPa, density < 3000 kg/m³):")
for material in aerospace_candidates:
    print(f"  {material[0]}: {material[2]} MPa, {material[1]} kg/m³")

# Find materials suitable for construction (good strength, reasonable cost)
construction_candidates = list(filter(lambda x: x[2] > 100 and x[3] < 10, materials))
print(f"\nConstruction candidates (strength > 100 MPa, cost < $10/kg):")
for material in construction_candidates:
    print(f"  {material[0]}: {material[2]} MPa, ${material[3]}/kg")

# Calculate total cost for 1 cubic meter of each material
print(f"\nCost for 1 cubic meter of each material:")
print("Material        Volume Cost")
print("-" * 25)
for material in materials:
    volume_cost = material[1] * material[3]  # density * cost_per_kg
    print(f"{material[0]:<15} ${volume_cost:,.2f}")

# Find the most cost-effective material for a given strength requirement
required_strength = 200  # MPa
suitable_materials = list(filter(lambda x: x[2] >= required_strength, materials))
if suitable_materials:
    most_cost_effective = min(suitable_materials, key=lambda x: x[3])
    print(f"\nMost cost-effective material for {required_strength} MPa requirement:")
    print(f"  {most_cost_effective[0]}: {most_cost_effective[2]} MPa at ${most_cost_effective[3]}/kg")
else:
    print(f"\nNo materials meet the {required_strength} MPa requirement")

# Calculate weight savings compared to steel
steel_density = materials[0][1]  # Steel is first in the list
print(f"\nWeight savings compared to steel (density {steel_density} kg/m³):")
print("Material        Weight Savings")
print("-" * 30)
for material in materials[1:]:  # Skip steel itself
    savings = ((steel_density - material[1]) / steel_density) * 100
    print(f"{material[0]:<15} {savings:.1f}%")

# Find materials with best overall score (strength/weight * cost_efficiency)
overall_score = sorted(materials, key=lambda x: (x[2]/x[1]) * (x[2]/x[3]), reverse=True)
print(f"\nMaterials ranked by overall score (strength/weight * cost efficiency):")
print("Material        Overall Score")
print("-" * 30)
for material in overall_score:
    score = (material[2]/material[1]) * (material[2]/material[3])
    print(f"{material[0]:<15} {score:.4f}")

print("\n" + "=" * 50)
print("Task 4 completed successfully!")
print("=" * 50)
