# Lab 06 Extra - Task 6: Statistical Analysis Functions
# Practice with functions for basic statistical analysis

print("=" * 50)
print("Task 6: Statistical Analysis Functions")
print("=" * 50)

import math

def calculate_mean(numbers):
    """Calculate the mean of a list of numbers"""
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    mean = total / len(numbers)
    return mean

def calculate_median(numbers):
    """Calculate the median of a list of numbers"""
    if len(numbers) == 0:
        return 0
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    if n % 2 == 0:
        # Even number of elements
        median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        # Odd number of elements
        median = sorted_numbers[n//2]
    
    return median

def calculate_variance(numbers):
    """Calculate the variance of a list of numbers"""
    if len(numbers) <= 1:
        return 0
    
    mean = calculate_mean(numbers)
    squared_differences = [(x - mean) ** 2 for x in numbers]
    variance = sum(squared_differences) / (len(numbers) - 1)
    return variance

def calculate_standard_deviation(numbers):
    """Calculate the standard deviation of a list of numbers"""
    variance = calculate_variance(numbers)
    std_dev = math.sqrt(variance)
    return std_dev

def find_outliers(numbers, threshold):
    """Find values more than threshold standard deviations from mean"""
    if len(numbers) <= 1:
        return []
    
    mean = calculate_mean(numbers)
    std_dev = calculate_standard_deviation(numbers)
    
    outliers = []
    for num in numbers:
        z_score = abs(num - mean) / std_dev
        if z_score > threshold:
            outliers.append(num)
    
    return outliers

def calculate_mode(numbers):
    """Calculate the mode (most frequent value) of a list of numbers"""
    if len(numbers) == 0:
        return None
    
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    
    max_frequency = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_frequency]
    
    return modes

# Test with sample data
sample_data = [12.3, 15.7, 18.2, 14.1, 16.8, 13.9, 17.4, 15.2, 19.1, 14.6]
print("Sample data:", sample_data)

# Calculate all statistics
mean = calculate_mean(sample_data)
median = calculate_median(sample_data)
variance = calculate_variance(sample_data)
std_dev = calculate_standard_deviation(sample_data)
mode = calculate_mode(sample_data)

print(f"\nStatistical analysis results:")
print(f"Mean: {mean:.2f}")
print(f"Median: {median:.2f}")
print(f"Variance: {variance:.2f}")
print(f"Standard deviation: {std_dev:.2f}")
print(f"Mode: {mode}")

# Test outlier detection
thresholds = [1.0, 1.5, 2.0]
print(f"\nOutlier detection (values more than X standard deviations from mean):")
for threshold in thresholds:
    outliers = find_outliers(sample_data, threshold)
    print(f"  Threshold {threshold}: {outliers}")

# Additional test cases
print("\nAdditional test cases:")

# Test with different datasets
test_datasets = [
    [1, 2, 3, 4, 5],
    [10, 20, 30, 40, 50],
    [5, 5, 5, 5, 5],
    [1, 1, 2, 2, 3, 3, 4, 4],
    [100, 50, 25, 12.5, 6.25],
    [1, 2, 3, 4, 5, 100]  # Contains an outlier
]

for i, dataset in enumerate(test_datasets):
    print(f"\nDataset {i+1}: {dataset}")
    if len(dataset) > 0:
        mean_val = calculate_mean(dataset)
        median_val = calculate_median(dataset)
        std_val = calculate_standard_deviation(dataset)
        mode_val = calculate_mode(dataset)
        outliers_2std = find_outliers(dataset, 2.0)
        
        print(f"  Mean: {mean_val:.2f}")
        print(f"  Median: {median_val:.2f}")
        print(f"  Std Dev: {std_val:.2f}")
        print(f"  Mode: {mode_val}")
        print(f"  Outliers (2σ): {outliers_2std}")

# Practical example: Temperature measurements
print(f"\nPractical example - Temperature measurements:")
temp_readings = [22.1, 22.3, 22.0, 22.2, 22.1, 22.4, 22.0, 22.2, 22.1, 22.3, 25.0]  # 25.0 is an outlier
print(f"Temperature readings: {temp_readings}")

temp_mean = calculate_mean(temp_readings)
temp_std = calculate_standard_deviation(temp_readings)
temp_outliers = find_outliers(temp_readings, 2.0)

print(f"Temperature statistics:")
print(f"  Mean: {temp_mean:.2f}°C")
print(f"  Standard deviation: {temp_std:.2f}°C")
print(f"  Outliers: {temp_outliers}")

# Quality control example
print(f"\nQuality control example:")
measurements = [10.1, 10.0, 9.9, 10.2, 10.0, 9.8, 10.1, 10.0, 9.9, 10.2, 8.5]  # 8.5 is defective
print(f"Measurements: {measurements}")

qc_mean = calculate_mean(measurements)
qc_std = calculate_standard_deviation(measurements)
qc_outliers = find_outliers(measurements, 2.0)

print(f"Quality control analysis:")
print(f"  Target: 10.0")
print(f"  Mean: {qc_mean:.2f}")
print(f"  Standard deviation: {qc_std:.2f}")
print(f"  Defective items (outliers): {qc_outliers}")

print("\n" + "=" * 50)
print("Task 6 completed successfully!")
print("=" * 50)
