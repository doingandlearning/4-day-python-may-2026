# Lab 07 Extra - Task 6: Lambda Functions for Statistical Analysis (no map/filter)

print("=" * 50)
print("Task 6: Lambda Functions for Statistical Analysis")
print("=" * 50)

# Sample measurement data
measurements = [12.3, 15.7, 18.2, 14.1, 16.8, 13.9, 17.4, 15.2, 19.1, 14.6]

print(f"Sample measurements: {measurements}")
print(f"Number of measurements: {len(measurements)}")

# Use lambda with max() and min() to find extreme values
max_value = max(measurements, key=lambda x: x)
min_value = min(measurements, key=lambda x: x)
print(f"\nExtreme values:")
print(f"  Maximum: {max_value}")
print(f"  Minimum: {min_value}")

# Use lambda with sorted() to sort measurements
sorted_asc = sorted(measurements, key=lambda x: x)
sorted_desc = sorted(measurements, key=lambda x: -x)
print(f"\nSorted measurements:")
print(f"  Ascending: {sorted_asc}")
print(f"  Descending: {sorted_desc}")

# Measurements above 15 (comprehension, no filter)
above_15 = [x for x in measurements if x > 15]
print(f"\nMeasurements above 15: {above_15}")

# Convert to a 0-100 scale where 12 = 0 and 20 = 100 (comprehension + lambda)
scale = lambda x: (x - 12) * 100 / 8
scaled_measurements = [scale(x) for x in measurements]
print(f"\nMeasurements scaled to 0-100 (12→0, 20→100):")
for orig, scaled in zip(measurements, scaled_measurements):
    print(f"  {orig} → {scaled:.1f}")

# Deviations from the mean (comprehension + lambda)
mean = sum(measurements) / len(measurements)
deviation = lambda x: x - mean
deviations = [deviation(x) for x in measurements]
print(f"\nMean: {mean:.2f}")
print(f"Deviations from mean: {[round(d, 2) for d in deviations]}")

# Additional statistical analysis with lambdas
print(f"\nAdditional statistical analysis:")

# Standard deviation and values within one std dev (comprehension)
variance = sum((x - mean) ** 2 for x in measurements) / len(measurements)
std_dev = variance ** 0.5
within_one_std = [x for x in measurements if abs(x - mean) <= std_dev]
print(f"Standard deviation: {std_dev:.2f}")
print(f"Measurements within 1 std dev of mean: {within_one_std}")

# Measurements in different ranges (comprehension)
ranges = [
    (12, 14, "Low"),
    (14, 16, "Medium"),
    (16, 18, "High"),
    (18, 20, "Very High")
]

print(f"\nMeasurements by range:")
for min_val, max_val, label in ranges:
    in_range = [x for x in measurements if min_val <= x < max_val]
    print(f"  {label} ({min_val}-{max_val}): {in_range}")

# Percentile helper
def percentile(data, p):
    """Calculate percentile"""
    sorted_data = sorted(data)
    index = (p / 100) * (len(sorted_data) - 1)
    if index.is_integer():
        return sorted_data[int(index)]
    lower = sorted_data[int(index)]
    upper = sorted_data[int(index) + 1]
    return lower + (upper - lower) * (index - int(index))

percentiles = [25, 50, 75, 90, 95]
print(f"\nPercentiles:")
for p in percentiles:
    value = percentile(measurements, p)
    print(f"  {p}th percentile: {value:.2f}")

# Outliers (more than 2 std devs) (comprehension)
outliers = [x for x in measurements if abs(x - mean) > 2 * std_dev]
print(f"\nOutliers (more than 2 std dev from mean): {outliers}")

# Moving average (window size 3) using comprehension
window_size = 3
if len(measurements) >= window_size:
    moving_avg = [
        sum(measurements[i:i + window_size]) / window_size
        for i in range(len(measurements) - window_size + 1)
    ]
    print(f"\nMoving average (window size {window_size}):")
    for i, avg in enumerate(moving_avg, start=1):
        print(f"  Position {i}: {avg:.2f}")

# Mode
from collections import Counter
measurement_counts = Counter(measurements)
mode = measurement_counts.most_common(1)[0]
print(f"\nMost common measurement: {mode[0]} (appears {mode[1]} times)")

# Coefficient of variation
cv = (std_dev / mean) * 100
print(f"Coefficient of variation: {cv:.2f}%")

# Above median (comprehension)
median = percentile(measurements, 50)
above_median = [x for x in measurements if x > median]
print(f"\nMedian: {median:.2f}")
print(f"Measurements above median: {above_median}")

# Range and midrange
data_range = max_value - min_value
midrange = (max_value + min_value) / 2
print(f"\nRange: {data_range:.2f}")
print(f"Midrange: {midrange:.2f}")

# Quartiles (comprehension)
q25 = percentile(measurements, 25)
q75 = percentile(measurements, 75)
bottom_quartile = [x for x in measurements if x <= q25]
top_quartile = [x for x in measurements if x >= q75]

print(f"\nQuartile analysis:")
print(f"  Q1 (25th percentile): {q25:.2f}")
print(f"  Q3 (75th percentile): {q75:.2f}")
print(f"  Bottom quartile: {bottom_quartile}")
print(f"  Top quartile: {top_quartile}")

print("\n" + "=" * 50)
print("Task 6 completed successfully!")
print("=" * 50)
