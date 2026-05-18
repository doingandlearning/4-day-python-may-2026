# Lab 07 Extra - Task 4: Practical Engineering Applications (List Comprehensions)

from operator import itemgetter

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

# Sort by strength-to-weight ratio (no lambda: sort tuple of (ratio, material))
_sw_pairs = [((m[2] / m[1]), m) for m in materials]
strength_weight_ratio = [m for _, m in sorted(_sw_pairs, key=itemgetter(0), reverse=True)]

print(f"\nMaterials sorted by strength-to-weight ratio (highest first):")
print("Material        Strength/Weight Ratio")
print("-" * 40)
for material in strength_weight_ratio:
    ratio = material[2] / material[1]
    print(f"{material[0]:<15} {ratio:.6f}")

# Materials cheaper than $5 per kg (filter -> list comprehension)
cheap_materials = [m for m in materials if m[3] < 5.0]
print(f"\nMaterials cheaper than $5/kg:")
for material in cheap_materials:
    print(f"  {material[0]}: ${material[3]:.2f}/kg")

# Sort by cost efficiency (strength/cost) without lambda
_ce_pairs = [((m[2] / m[3]), m) for m in materials]
cost_efficiency = [m for _, m in sorted(_ce_pairs, key=itemgetter(0), reverse=True)]

print(f"\nMaterials sorted by cost efficiency (strength per dollar):")
print("Material        Strength/Cost Ratio")
print("-" * 40)
for material in cost_efficiency:
    efficiency = material[2] / material[3]
    print(f"{material[0]:<15} {efficiency:.2f}")

# Strength per dollar for each material (lambda -> comprehension)
spd_list = [(m[0], m[2] / m[3]) for m in materials]
print(f"\nStrength per dollar for each material:")
for name, spd in spd_list:
    print(f"  {name}: {spd:.2f} MPa/$")

# Sort by density (lightest first) with itemgetter
lightest_first = sorted(materials, key=itemgetter(1))
print(f"\nMaterials sorted by density (lightest first):")
print("Material        Density(kg/m³)")
print("-" * 30)
for material in lightest_first:
    print(f"{material[0]:<15} {material[1]}")

# Additional engineering analysis
print(f"\nAdditional engineering analysis:")

# Aerospace candidates (filter -> list comprehension)
aerospace_candidates = [m for m in materials if m[2] > 300 and m[1] < 3000]
print(f"Aerospace candidates (strength > 300 MPa, density < 3000 kg/m³):")
for material in aerospace_candidates:
    print(f"  {material[0]}: {material[2]} MPa, {material[1]} kg/m³")

# Construction candidates (filter -> list comprehension)
construction_candidates = [m for m in materials if m[2] > 100 and m[3] < 10]
print(f"\nConstruction candidates (strength > 100 MPa, cost < $10/kg):")
for material in construction_candidates:
    print(f"  {material[0]}: {material[2]} MPa, ${material[3]}/kg")

# Cost for 1 cubic meter of each material (comprehension)
volume_costs = [(m[0], m[1] * m[3]) for m in materials]
print(f"\nCost for 1 cubic meter of each material:")
print("Material        Volume Cost")
print("-" * 25)
for name, vcost in volume_costs:
    print(f"{name:<15} ${vcost:,.2f}")

# Most cost-effective material for a given strength requirement (no lambda)
required_strength = 200  # MPa
suitable_materials = [m for m in materials if m[2] >= required_strength]
if suitable_materials:
    most_cost_effective = min(suitable_materials, key=itemgetter(3))
    print(f"\nMost cost-effective material for {required_strength} MPa requirement:")
    print(f"  {most_cost_effective[0]}: {most_cost_effective[2]} MPa at ${most_cost_effective[3]}/kg")
else:
    print(f"\nNo materials meet the {required_strength} MPa requirement")

# Weight savings compared to steel
steel_density = materials[0][1]  # Steel is first in the list
print(f"\nWeight savings compared to steel (density {steel_density} kg/m³):")
print("Material        Weight Savings")
print("-" * 30)
for material in materials[1:]:  # Skip steel itself
    savings = ((steel_density - material[1]) / steel_density) * 100
    print(f"{material[0]:<15} {savings:.1f}%")

# Overall score (strength/weight * strength/cost) without lambda
_score_pairs = [(((m[2] / m[1]) * (m[2] / m[3])), m) for m in materials]
overall_score = [m for _, m in sorted(_score_pairs, key=itemgetter(0), reverse=True)]

print(f"\nMaterials ranked by overall score (strength/weight * cost efficiency):")
print("Material        Overall Score")
print("-" * 30)
for material in overall_score:
    score = (material[2] / material[1]) * (material[2] / material[3])
    print(f"{material[0]:<15} {score:.4f}")

print("\n" + "=" * 50)
print("Task 4 completed successfully!")
print("=" * 50)
