# NumPy Data Handling Lab - SOLUTION
# In this lab, you'll practice working with data files, handling missing values, and filtering data in NumPy

import numpy as np
import os
import matplotlib.pyplot as plt

# -------------------------------------------------
# Part 1: Creating Sample Data Files
# -------------------------------------------------

# Let's first create some sample data files to work with
def create_sample_files():
    # Complete dataset (no missing values)
    complete_data = np.array([
        [10.5, 20.3, 30.1, 40.5],
        [15.2, 25.4, 35.6, 45.7],
        [12.8, 22.9, 32.7, 42.3],
        [18.1, 28.6, 38.9, 48.2],
        [14.7, 24.5, 34.8, 44.6]
    ])
    
    # Dataset with missing values
    missing_data = np.copy(complete_data)
    missing_data[1, 2] = np.nan  # Row 1, Col 2
    missing_data[3, 1] = np.nan  # Row 3, Col 1
    missing_data[4, 3] = np.nan  # Row 4, Col 3
    
    # Save the data to CSV files
    np.savetxt("complete_data.csv", complete_data, delimiter=",", fmt="%.1f")
    np.savetxt("missing_data.csv", missing_data, delimiter=",", fmt="%.1f")
    
    print("Sample data files created: complete_data.csv and missing_data.csv")

# Create the sample files if they don't exist
if not os.path.exists("complete_data.csv"):
    create_sample_files()

# -------------------------------------------------
# Part 2: Reading Data Files
# -------------------------------------------------

# EXERCISE 1: Read the complete data file using np.loadtxt()
complete_data = np.loadtxt("complete_data.csv", delimiter=",")
print("Complete data loaded successfully:")
print(complete_data)

# EXERCISE 2: Try to read the file with missing values using np.loadtxt()
# What happens? Comment on the error
try:
    problematic_data = np.loadtxt("missing_data.csv", delimiter=",")
    print("Data loaded successfully (unexpected!)")
except ValueError as e:
    print("Error loading data with np.loadtxt():")
    print(e)
    print("np.loadtxt() cannot handle missing values - it will raise an error when it encounters NaN values.")

# EXERCISE 3: Now read the file with missing values using np.genfromtxt()
missing_data = np.genfromtxt("missing_data.csv", delimiter=",")
print("\nMissing data loaded with genfromtxt:")
print(missing_data)

# -------------------------------------------------
# Part 3: Working with Missing Values
# -------------------------------------------------

# EXERCISE 4: Detect which values in the data are missing
missing_mask = np.isnan(missing_data)
print("\nMissing value mask (True indicates missing):")
print(missing_mask)
print(f"Number of missing values: {np.sum(missing_mask)}")

# EXERCISE 5: Calculate the mean of each column, ignoring missing values
column_means = np.nanmean(missing_data, axis=0)
print("\nColumn means (ignoring NaN values):")
print(column_means)

# EXERCISE 6: Replace missing values with the mean of their respective columns
# Create a copy to work with
filled_data = np.copy(missing_data)

# Replace NaN values with column means
for col in range(missing_data.shape[1]):
    col_mean = np.nanmean(missing_data[:, col])
    # Create a mask for NaN values in this column
    mask = np.isnan(filled_data[:, col])
    # Replace NaN with the column mean
    filled_data[mask, col] = col_mean

print("\nData with missing values filled by column means:")
print(filled_data)

# -------------------------------------------------
# Part 4: Boolean Masking and Filtering
# -------------------------------------------------

# Let's use the data we read from the complete file
data = np.loadtxt("complete_data.csv", delimiter=",")

# EXERCISE 7: Find all values in the data that are greater than 30
high_values_mask = data > 30
high_values = data[high_values_mask]
print("\nValues greater than 30:")
print(high_values)

# EXERCISE 8: Find the positions (indices) where values are between 20 and 40
between_mask = (data >= 20) & (data <= 40)
positions = np.where(between_mask)
values_between = data[between_mask]

print("\nPositions (row, col) where values are between 20 and 40:")
print(list(zip(positions[0], positions[1])))
print("The values at these positions:")
print(values_between)

# EXERCISE 9: Create a filter to select rows where the sum of the row is greater than 100
row_sums = np.sum(data, axis=1)
high_sum_rows_mask = row_sums > 100
high_sum_rows = data[high_sum_rows_mask]

print("\nRows where sum exceeds 100:")
print(high_sum_rows)
print("Their sums:")
print(np.sum(high_sum_rows, axis=1))

# -------------------------------------------------
# Part 5: Practical Application
# -------------------------------------------------

# EXERCISE 10: Temperature Analysis
# The dataset represents temperature readings (in Celsius) for 5 days across 4 different locations
# Column 1: Location A, Column 2: Location B, Column 3: Location C, Column 4: Location D

# 1. Calculate the average temperature for each location
location_avgs = np.mean(data, axis=0)
print("\nAverage temperature by location:")
for i, avg in enumerate(['A', 'B', 'C', 'D']):
    print(f"Location {avg}: {location_avgs[i]:.1f}°C")

# 2. Find the day (row) with the highest average temperature across all locations
day_avgs = np.mean(data, axis=1)
hottest_day_idx = np.argmax(day_avgs)
print(f"\nDay {hottest_day_idx + 1} had the highest average temperature: {day_avgs[hottest_day_idx]:.1f}°C")

# 3. Identify locations (columns) where the temperature exceeded 35°C at least once
hot_days_by_location = np.any(data > 35, axis=0)
hot_locations = ['A', 'B', 'C', 'D']
print("\nLocations where temperature exceeded 35°C at least once:")
for i, is_hot in enumerate(hot_days_by_location):
    if is_hot:
        print(f"Location {hot_locations[i]}")

# 4. Create a boolean mask for readings between 20°C and 30°C (moderate temperatures)
moderate_temp_mask = (data >= 20) & (data <= 30)
print("\nModerate temperature readings (20-30°C):")
print(moderate_temp_mask)

# 5. Save a new CSV file with only the moderate temperature readings
#    (other values should be replaced with 0)
moderate_temps = np.where(moderate_temp_mask, data, 0)
np.savetxt("moderate_temps.csv", moderate_temps, delimiter=",", fmt="%.1f")
print("\nModerate temperatures saved to moderate_temps.csv")
print("Data where only moderate temperatures are preserved (others set to 0):")
print(moderate_temps)
