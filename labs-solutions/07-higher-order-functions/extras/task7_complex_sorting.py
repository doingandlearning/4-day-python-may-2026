# Lab 07 Extra - Task 7: Complex Sorting with Multiple Criteria
# Practice with complex sorting using lambdas with multiple criteria

print("=" * 50)
print("Task 7: Complex Sorting with Multiple Criteria")
print("=" * 50)

# Sample equipment data: (name, age_years, efficiency, maintenance_cost)
equipment = [
    ("Pump_A", 5, 0.85, 1200),
    ("Pump_B", 3, 0.92, 800),
    ("Pump_C", 8, 0.78, 1500),
    ("Pump_D", 2, 0.95, 600),
    ("Pump_E", 6, 0.88, 1100)
]

print("Equipment data:")
print("Name      Age  Efficiency  Maintenance Cost")
print("-" * 45)
for eq in equipment:
    print(f"{eq[0]:<8} {eq[1]:<4} {eq[2]:<11} ${eq[3]:<15}")

# Sort by efficiency (highest first), then by age (lowest first)
efficiency_age_sorted = sorted(equipment, key=lambda x: (-x[2], x[1]))
print(f"\nSorted by efficiency (desc), then age (asc):")
print("Name      Efficiency  Age")
print("-" * 25)
for eq in efficiency_age_sorted:
    print(f"{eq[0]:<8} {eq[2]:<11} {eq[1]}")

# Sort by maintenance cost per year of age
cost_per_year = sorted(equipment, key=lambda x: x[3]/x[1])
print(f"\nSorted by maintenance cost per year:")
print("Name      Cost/Year")
print("-" * 20)
for eq in cost_per_year:
    cost_per_year_val = eq[3] / eq[1]
    print(f"{eq[0]:<8} ${cost_per_year_val:.2f}")

# Sort by overall score: efficiency - (age/10) - (maintenance_cost/10000)
overall_score = sorted(equipment, key=lambda x: x[2] - (x[1]/10) - (x[3]/10000), reverse=True)
print(f"\nSorted by overall score (efficiency - age/10 - cost/10000):")
print("Name      Overall Score")
print("-" * 25)
for eq in overall_score:
    score = eq[2] - (eq[1]/10) - (eq[3]/10000)
    print(f"{eq[0]:<8} {score:.4f}")

# Create a lambda to calculate strength per dollar
value_score = lambda eq: eq[2] / eq[3]  # efficiency per dollar
print(f"\nValue score (efficiency per dollar) for each equipment:")
for eq in equipment:
    vs = value_score(eq)
    print(f"  {eq[0]}: {vs:.6f}")

# Sort by value score (highest first)
value_sorted = sorted(equipment, key=lambda x: x[2]/x[3], reverse=True)
print(f"\nSorted by value score (efficiency per dollar):")
print("Name      Value Score")
print("-" * 20)
for eq in value_sorted:
    vs = eq[2] / eq[3]
    print(f"{eq[0]:<8} {vs:.6f}")

# Additional complex sorting examples
print(f"\nAdditional complex sorting examples:")

# Sort by efficiency, then by cost, then by age
efficiency_cost_age = sorted(equipment, key=lambda x: (-x[2], x[3], x[1]))
print(f"Sorted by efficiency (desc), cost (asc), age (asc):")
for eq in efficiency_cost_age:
    print(f"  {eq[0]}: Eff={eq[2]}, Cost=${eq[3]}, Age={eq[1]}")

# Sort by age group, then by efficiency within each group
age_groups = sorted(equipment, key=lambda x: (x[1]//3, -x[2]))
print(f"\nSorted by age group (0-2, 3-5, 6+), then efficiency:")
for eq in age_groups:
    age_group = eq[1] // 3
    print(f"  {eq[0]}: Age Group {age_group}, Eff={eq[2]}, Age={eq[1]}")

# Sort by maintenance urgency (old + high cost = urgent)
urgency = sorted(equipment, key=lambda x: x[1] * x[3], reverse=True)
print(f"\nSorted by maintenance urgency (age × cost):")
for eq in urgency:
    urgency_score = eq[1] * eq[3]
    print(f"  {eq[0]}: Urgency Score {urgency_score} (Age {eq[1]} × Cost ${eq[3]})")

# Sort by efficiency per year of remaining life (assuming 10-year lifespan)
remaining_life = sorted(equipment, key=lambda x: x[2] / (10 - x[1]) if x[1] < 10 else 0, reverse=True)
print(f"\nSorted by efficiency per year of remaining life (10-year lifespan):")
for eq in remaining_life:
    if eq[1] < 10:
        eff_per_year = eq[2] / (10 - eq[1])
        print(f"  {eq[0]}: {eff_per_year:.4f} (Eff {eq[2]} / {10-eq[1]} years)")
    else:
        print(f"  {eq[0]}: Past lifespan")

# Sort by cost-effectiveness considering both efficiency and age
cost_effectiveness = sorted(equipment, key=lambda x: (x[2] * (10 - x[1])) / x[3] if x[1] < 10 else 0, reverse=True)
print(f"\nSorted by cost-effectiveness (efficiency × remaining_life / cost):")
for eq in cost_effectiveness:
    if eq[1] < 10:
        ce = (eq[2] * (10 - eq[1])) / eq[3]
        print(f"  {eq[0]}: {ce:.4f}")
    else:
        print(f"  {eq[0]}: Past lifespan")

# Find the best equipment for different scenarios
print(f"\nBest equipment for different scenarios:")

# Most efficient
most_efficient = max(equipment, key=lambda x: x[2])
print(f"  Most efficient: {most_efficient[0]} ({most_efficient[2]})")

# Cheapest to maintain
cheapest_maintenance = min(equipment, key=lambda x: x[3])
print(f"  Cheapest maintenance: {cheapest_maintenance[0]} (${cheapest_maintenance[3]})")

# Newest
newest = min(equipment, key=lambda x: x[1])
print(f"  Newest: {newest[0]} ({newest[1]} years old)")

# Best value (efficiency per dollar)
best_value = max(equipment, key=lambda x: x[2]/x[3])
print(f"  Best value: {best_value[0]} ({best_value[2]/best_value[3]:.6f} efficiency per dollar)")

# Most urgent maintenance (oldest + highest cost)
most_urgent = max(equipment, key=lambda x: x[1] * x[3])
print(f"  Most urgent maintenance: {most_urgent[0]} (age {most_urgent[1]} × cost ${most_urgent[3]})")

print("\n" + "=" * 50)
print("Task 7 completed successfully!")
print("=" * 50)
