# Lab 05 Extra - Task 3: Data Point Frequency Counter
# Practice with dictionaries to count measurement frequencies

print("=" * 50)
print("Task 3: Data Point Frequency Counter")
print("=" * 50)

# Sample experimental measurements
measurements = [23.5, 24.1, 23.5, 25.2, 24.1, 23.5, 24.8, 25.2, 24.1]

print("Original measurements:")
for i, measurement in enumerate(measurements):
    print(f"Measurement {i+1}: {measurement}")

# Create a dictionary to count measurement frequencies
frequency_count = {}

# Count how many times each measurement appears
for measurement in measurements:
    if measurement in frequency_count:
        frequency_count[measurement] += 1
    else:
        frequency_count[measurement] = 1

# Print the frequency of each measurement value
print("\nFrequency of each measurement value:")
for measurement, count in frequency_count.items():
    print(f"- {measurement}: appears {count} time(s)")

# Find the most common measurement
most_common_count = max(frequency_count.values())
most_common_measurements = []
for measurement, count in frequency_count.items():
    if count == most_common_count:
        most_common_measurements.append(measurement)

print(f"\nMost common measurement(s): {most_common_measurements} (appears {most_common_count} times)")

# Find the least common measurement
least_common_count = min(frequency_count.values())
least_common_measurements = []
for measurement, count in frequency_count.items():
    if count == least_common_count:
        least_common_measurements.append(measurement)

print(f"Least common measurement(s): {least_common_measurements} (appears {least_common_count} time)")

# Print measurements that appear more than once
print("\nMeasurements that appear more than once:")
for measurement, count in frequency_count.items():
    if count > 1:
        print(f"- {measurement}: appears {count} times")

# Print measurements that appear exactly once
print("\nMeasurements that appear exactly once:")
for measurement, count in frequency_count.items():
    if count == 1:
        print(f"- {measurement}: appears {count} time")

print("\n" + "=" * 50)
print("Task 3 completed successfully!")
print("=" * 50)
