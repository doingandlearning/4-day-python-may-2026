# Lab 07 Extra - Task 1: Sorting Scientific Data with Lambdas
# Practice with lambda functions for sorting experimental data

print("=" * 50)
print("Task 1: Sorting Scientific Data with Lambdas")
print("=" * 50)

# Sample experimental data: (experiment_id, temperature, pressure, result)
experiments = [
    ("EXP_001", 25.3, 101.2, 0.85),
    ("EXP_002", 30.1, 98.7, 0.92),
    ("EXP_003", 22.8, 103.1, 0.78),
    ("EXP_004", 28.5, 99.8, 0.88),
    ("EXP_005", 26.7, 102.3, 0.91)
]

print("Original experimental data:")
for exp in experiments:
    print(f"  {exp[0]}: Temp={exp[1]}°C, Pressure={exp[2]}kPa, Result={exp[3]}")

# Sort by temperature (ascending)
sorted_by_temp = sorted(experiments, key=lambda x: x[1])
print(f"\nSorted by temperature (ascending):")
for exp in sorted_by_temp:
    print(f"  {exp[0]}: {exp[1]}°C")

# Sort by pressure (descending)
sorted_by_pressure = sorted(experiments, key=lambda x: x[2], reverse=True)
print(f"\nSorted by pressure (descending):")
for exp in sorted_by_pressure:
    print(f"  {exp[0]}: {exp[2]}kPa")

# Sort by result (descending)
sorted_by_result = sorted(experiments, key=lambda x: x[3], reverse=True)
print(f"\nSorted by result (descending):")
for exp in sorted_by_result:
    print(f"  {exp[0]}: {exp[3]}")

# Sort by experiment ID alphabetically
sorted_by_id = sorted(experiments, key=lambda x: x[0])
print(f"\nSorted by experiment ID (alphabetical):")
for exp in sorted_by_id:
    print(f"  {exp[0]}: {exp[1]}°C, {exp[2]}kPa, {exp[3]}")

# Custom sort: high results AND low temperatures
# Use negative result for descending, positive temperature for ascending
custom_sorted = sorted(experiments, key=lambda x: (-x[3], x[1]))
print(f"\nCustom sort (high result, low temperature):")
for exp in custom_sorted:
    print(f"  {exp[0]}: Result={exp[3]}, Temp={exp[1]}°C")

# Additional sorting examples
print(f"\nAdditional sorting examples:")

# Sort by pressure-to-temperature ratio
pressure_temp_ratio = sorted(experiments, key=lambda x: x[2]/x[1], reverse=True)
print("Sorted by pressure-to-temperature ratio (highest first):")
for exp in pressure_temp_ratio:
    ratio = exp[2]/exp[1]
    print(f"  {exp[0]}: Ratio={ratio:.3f}")

# Sort by result efficiency (result per degree temperature)
result_efficiency = sorted(experiments, key=lambda x: x[3]/x[1], reverse=True)
print("\nSorted by result efficiency (result per degree):")
for exp in result_efficiency:
    efficiency = exp[3]/exp[1]
    print(f"  {exp[0]}: Efficiency={efficiency:.4f}")

# Sort by multiple criteria: result (desc), then temperature (asc), then pressure (desc)
multi_criteria = sorted(experiments, key=lambda x: (-x[3], x[1], -x[2]))
print("\nMulti-criteria sort (result desc, temp asc, pressure desc):")
for exp in multi_criteria:
    print(f"  {exp[0]}: Result={exp[3]}, Temp={exp[1]}°C, Pressure={exp[2]}kPa")


# Alternative approach - to use a standard score/weighted sum
print("\n" + "=" * 50)
print("Alternative Approach: Standard Score/Weighted Sum")
print("=" * 50)

import statistics

def calculate_standard_scores(data, metric_index):
    """Calculate z-scores for a given metric across all experiments."""
    values = [exp[metric_index] for exp in data]
    mean_val = statistics.mean(values)
    std_val = statistics.stdev(values) if len(values) > 1 else 1
    
    return [(val - mean_val) / std_val for val in values]

def create_weighted_score(experiments, weights):
    """
    Create a weighted composite score using standardized values.
    weights: dict with metric indices as keys and weights as values
    """
    # Calculate standard scores for each metric
    std_scores = {}
    for metric_idx in weights.keys():
        std_scores[metric_idx] = calculate_standard_scores(experiments, metric_idx)
    
    # Create weighted composite scores
    weighted_scores = []
    for i, exp in enumerate(experiments):
        composite_score = 0
        for metric_idx, weight in weights.items():
            composite_score += std_scores[metric_idx][i] * weight
        weighted_scores.append((exp, composite_score))
    
    return weighted_scores

# Define weights for different metrics
# Positive weights mean higher values are better, negative weights mean lower values are better
weights_scenarios = {
    "High Result, Low Temperature": {3: 1.0, 1: -0.5, 2: 0.2},  # Result good, temp bad, pressure slightly good
    "Balanced Performance": {3: 0.4, 1: -0.3, 2: 0.3},         # Balanced approach
    "Result Focused": {3: 1.0, 1: 0.0, 2: 0.0},                # Only care about result
    "Efficiency Focused": {3: 0.6, 1: -0.4, 2: 0.0},           # Result per temperature
}

print("Original experimental data:")
for exp in experiments:
    print(f"  {exp[0]}: Temp={exp[1]}°C, Pressure={exp[2]}kPa, Result={exp[3]}")

# Calculate and display standard scores
print(f"\nStandard Scores (z-scores):")
temp_scores = calculate_standard_scores(experiments, 1)
pressure_scores = calculate_standard_scores(experiments, 2)
result_scores = calculate_standard_scores(experiments, 3)

for i, exp in enumerate(experiments):
    print(f"  {exp[0]}: Temp_z={temp_scores[i]:.3f}, Pressure_z={pressure_scores[i]:.3f}, Result_z={result_scores[i]:.3f}")

# Apply different weighting scenarios
for scenario_name, weights in weights_scenarios.items():
    print(f"\n{scenario_name} (weights: {weights}):")
    weighted_scores = create_weighted_score(experiments, weights)
    
    # Sort by weighted score (descending)
    sorted_by_weight = sorted(weighted_scores, key=lambda x: x[1], reverse=True)
    
    for exp, score in sorted_by_weight:
        print(f"  {exp[0]}: Score={score:.3f} (Result={exp[3]}, Temp={exp[1]}°C, Pressure={exp[2]}kPa)")

# Advanced: Interactive weight adjustment
print(f"\nAdvanced: Custom Weight Adjustment")
print("You can modify the weights dictionary to experiment with different priorities:")
print("weights = {3: 1.0, 1: -0.5, 2: 0.2}  # Result=1.0, Temp=-0.5, Pressure=0.2")
print("Negative weights for temperature mean lower temperatures are preferred")
print("Positive weights mean higher values are preferred")

print("\n" + "=" * 50)
print("Task 1 completed successfully!")
print("=" * 50)
