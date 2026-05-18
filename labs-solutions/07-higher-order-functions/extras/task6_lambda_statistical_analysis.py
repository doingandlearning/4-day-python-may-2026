# Lab 07 Extra - Task 6: Lambda Functions for Statistical Analysis
# Practice with lambda functions for quick statistical calculations

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

# Use lambda with filter() to find measurements above 15
above_15 = list(filter(lambda x: x > 15, measurements))
print(f"\nMeasurements above 15: {above_15}")

# Use lambda with map() to convert measurements to a different scale
# Convert to a 0-100 scale where 12 = 0 and 20 = 100
scaled_measurements = list(map(lambda x: (x - 12) * 100 / 8, measurements))
print(f"\nMeasurements scaled to 0-100 (12→0, 20→100):")
for i, (orig, scaled) in enumerate(zip(measurements, scaled_measurements)):
    print(f"  {orig} → {scaled:.1f}")

# Create a lambda to calculate deviations from the mean
mean = sum(measurements) / len(measurements)
deviations = list(map(lambda x: x - mean, measurements))
print(f"\nMean: {mean:.2f}")
print(f"Deviations from mean: {[round(d, 2) for d in deviations]}")

# Additional statistical analysis with lambdas
print(f"\nAdditional statistical analysis:")

# Find measurements within one standard deviation of the mean
variance = sum((x - mean) ** 2 for x in measurements) / len(measurements)
std_dev = variance ** 0.5
within_one_std = list(filter(lambda x: abs(x - mean) <= std_dev, measurements))
print(f"Standard deviation: {std_dev:.2f}")
print(f"Measurements within 1 std dev of mean: {within_one_std}")

# Find measurements in different ranges
ranges = [
    (12, 14, "Low"),
    (14, 16, "Medium"),
    (16, 18, "High"),
    (18, 20, "Very High")
]

print(f"\nMeasurements by range:")
for min_val, max_val, label in ranges:
    in_range = list(filter(lambda x: min_val <= x < max_val, measurements))
    print(f"  {label} ({min_val}-{max_val}): {in_range}")

# Calculate percentiles using lambda
def percentile(data, p):
    """Calculate percentile using lambda"""
    sorted_data = sorted(data)
    index = (p / 100) * (len(sorted_data) - 1)
    if index.is_integer():
        return sorted_data[int(index)]
    else:
        lower = sorted_data[int(index)]
        upper = sorted_data[int(index) + 1]
        return lower + (upper - lower) * (index - int(index))

percentiles = [25, 50, 75, 90, 95]
print(f"\nPercentiles:")
for p in percentiles:
    value = percentile(measurements, p)
    print(f"  {p}th percentile: {value:.2f}")

# Find outliers using lambda (values more than 2 standard deviations from mean)
outliers = list(filter(lambda x: abs(x - mean) > 2 * std_dev, measurements))
print(f"\nOutliers (more than 2 std dev from mean): {outliers}")

# Calculate moving average using lambda
window_size = 3
if len(measurements) >= window_size:
    moving_avg = []
    for i in range(len(measurements) - window_size + 1):
        window = measurements[i:i + window_size]
        avg = sum(window) / len(window)
        moving_avg.append(avg)
    
    print(f"\nMoving average (window size {window_size}):")
    for i, avg in enumerate(moving_avg):
        print(f"  Position {i+1}: {avg:.2f}")

# Find the most common measurement (mode)
from collections import Counter
measurement_counts = Counter(measurements)
mode = measurement_counts.most_common(1)[0]
print(f"\nMost common measurement: {mode[0]} (appears {mode[1]} times)")

# Calculate coefficient of variation
cv = (std_dev / mean) * 100
print(f"Coefficient of variation: {cv:.2f}%")

# Find measurements that are above the median
median = percentile(measurements, 50)
above_median = list(filter(lambda x: x > median, measurements))
print(f"\nMedian: {median:.2f}")
print(f"Measurements above median: {above_median}")

# Calculate range and midrange
data_range = max_value - min_value
midrange = (max_value + min_value) / 2
print(f"\nRange: {data_range:.2f}")
print(f"Midrange: {midrange:.2f}")

# Find measurements in the top and bottom quartiles
q25 = percentile(measurements, 25)
q75 = percentile(measurements, 75)
bottom_quartile = list(filter(lambda x: x <= q25, measurements))
top_quartile = list(filter(lambda x: x >= q75, measurements))

print(f"\nQuartile analysis:")
print(f"  Q1 (25th percentile): {q25:.2f}")
print(f"  Q3 (75th percentile): {q75:.2f}")
print(f"  Bottom quartile: {bottom_quartile}")
print(f"  Top quartile: {top_quartile}")

print("\n" + "=" * 50)
print("Task 6 completed successfully!")
print("=" * 50)
