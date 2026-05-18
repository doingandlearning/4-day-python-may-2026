# Lab 06 Extra - Task 3: Data Analysis Functions
# Practice with functions for analyzing experimental data

print("=" * 50)
print("Task 3: Data Analysis Functions")
print("=" * 50)

def calculate_average(numbers):
    """Calculate the average of a list of numbers"""
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    average = total / len(numbers)
    return average

def find_maximum(numbers):
    """Find the maximum value in a list of numbers"""
    if len(numbers) == 0:
        return None
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

def find_minimum(numbers):
    """Find the minimum value in a list of numbers"""
    if len(numbers) == 0:
        return None
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum

def calculate_range(numbers):
    """Calculate the range (max - min) of a list of numbers"""
    if len(numbers) == 0:
        return 0
    maximum = find_maximum(numbers)
    minimum = find_minimum(numbers)
    range_value = maximum - minimum
    return range_value

def count_above_threshold(numbers, threshold):
    """Count values above a threshold"""
    count = 0
    for num in numbers:
        if num > threshold:
            count += 1
    return count

# Test with sample data
sample_data = [23.5, 24.1, 22.8, 25.2, 23.9, 24.7, 22.1, 25.8]
print("Sample data:", sample_data)

# Test all functions
average = calculate_average(sample_data)
maximum = find_maximum(sample_data)
minimum = find_minimum(sample_data)
range_value = calculate_range(sample_data)

print(f"\nData analysis results:")
print(f"Average: {average:.2f}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
print(f"Range: {range_value}")

# Test threshold counting
thresholds = [23.0, 24.0, 25.0]
print(f"\nValues above different thresholds:")
for threshold in thresholds:
    count = count_above_threshold(sample_data, threshold)
    print(f"  Above {threshold}: {count} values")

# Additional test cases
print("\nAdditional test cases:")

# Test with different datasets
test_datasets = [
    [1, 2, 3, 4, 5],
    [10, 20, 30],
    [5, 5, 5, 5],
    [100, 50, 25, 12.5],
    []
]

for i, dataset in enumerate(test_datasets):
    print(f"\nDataset {i+1}: {dataset}")
    if len(dataset) > 0:
        avg = calculate_average(dataset)
        max_val = find_maximum(dataset)
        min_val = find_minimum(dataset)
        range_val = calculate_range(dataset)
        print(f"  Average: {avg:.2f}")
        print(f"  Max: {max_val}")
        print(f"  Min: {min_val}")
        print(f"  Range: {range_val}")
    else:
        print("  Empty dataset")

# Test threshold counting with different thresholds
print(f"\nThreshold analysis for sample data:")
for threshold in range(20, 27):
    count = count_above_threshold(sample_data, threshold)
    print(f"  Above {threshold}: {count} values")

print("\n" + "=" * 50)
print("Task 3 completed successfully!")
print("=" * 50)
