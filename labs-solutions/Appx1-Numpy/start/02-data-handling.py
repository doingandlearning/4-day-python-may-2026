# NumPy Data Handling Lab
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
# YOUR CODE HERE:



# EXERCISE 2: Try to read the file with missing values using np.loadtxt()
# What happens? Comment on the error
# YOUR CODE HERE:



# EXERCISE 3: Now read the file with missing values using np.genfromtxt()
# YOUR CODE HERE:



# -------------------------------------------------
# Part 3: Working with Missing Values
# -------------------------------------------------

# EXERCISE 4: Detect which values in the data are missing
# YOUR CODE HERE:



# EXERCISE 5: Calculate the mean of each column, ignoring missing values
# Hint: np.nanmean()
# YOUR CODE HERE:



# EXERCISE 6: Replace missing values with the mean of their respective columns
# YOUR CODE HERE:



# -------------------------------------------------
# Part 4: Boolean Masking and Filtering
# -------------------------------------------------

# Let's use the data we read from the complete file
data = np.loadtxt("complete_data.csv", delimiter=",")

# EXERCISE 7: Find all values in the data that are greater than 30
# YOUR CODE HERE:



# EXERCISE 8: Find the positions (indices) where values are between 20 and 40
# YOUR CODE HERE:



# EXERCISE 9: Create a filter to select rows where the sum of the row is greater than 100
# YOUR CODE HERE:



# -------------------------------------------------
# Part 5: Practical Application
# -------------------------------------------------

# EXERCISE 10: Temperature Analysis
# The dataset represents temperature readings (in Celsius) for 5 days across 4 different locations
# Column 1: Location A, Column 2: Location B, Column 3: Location C, Column 4: Location D

# 1. Calculate the average temperature for each location
# YOUR CODE HERE:



# 2. Find the day (row) with the highest average temperature across all locations
# YOUR CODE HERE:



# 3. Identify locations (columns) where the temperature exceeded 35°C at least once
# YOUR CODE HERE:



# 4. Create a boolean mask for readings between 20°C and 30°C (moderate temperatures)
# YOUR CODE HERE:



# 5. Save a new CSV file with only the moderate temperature readings
#    (other values should be replaced with 0)
# YOUR CODE HERE:



# BONUS: Create a visualization of the temperature data 
# Hint: Use matplotlib.pyplot to create a line plot showing temperatures by location
# YOUR CODE HERE: