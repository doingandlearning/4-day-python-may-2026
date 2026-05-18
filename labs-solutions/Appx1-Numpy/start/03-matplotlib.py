# Matplotlib Data Visualization Lab
# In this lab, you'll practice creating and customizing different types of plots using Matplotlib

import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# Part 1: Basic Plotting with Matplotlib
# -------------------------------------------------

# EXERCISE 1: Create a simple line plot of a sine wave
# 1. Generate x values from 0 to 2π with 100 points
# 2. Calculate y = sin(x)
# 3. Create a line plot of the sine wave
# 4. Add appropriate labels, title, and grid
# YOUR CODE HERE:



# EXERCISE 2: Create a scatter plot
# 1. Generate 50 random x values between 0 and 10
# 2. Generate y values based on the formula y = x^2 + some random noise
# 3. Create a scatter plot
# 4. Add a title, labels, and legend
# YOUR CODE HERE:



# EXERCISE 3: Create a histogram
# 1. Generate 1000 random values from a normal distribution with mean=70, std=15
# 2. Create a histogram with 20 bins
# 3. Add appropriate title and labels
# YOUR CODE HERE:



# -------------------------------------------------
# Part 2: Customizing Plots
# -------------------------------------------------

# EXERCISE 4: Create a customized line plot comparing sine and cosine
# 1. Generate x values from 0 to 2π with 100 points
# 2. Plot both sine and cosine on the same graph with different colors and line styles
# 3. Add markers to both lines
# 4. Add a legend, grid, and appropriate labels
# YOUR CODE HERE:



# EXERCISE 5: Create a scatter plot with customized markers
# 1. Generate random x and y data for two different groups
# 2. Plot group 1 with red circle markers and group 2 with blue triangle markers
# 3. Make the markers semi-transparent (alpha = 0.5)
# 4. Add a legend to distinguish the groups
# YOUR CODE HERE:



# -------------------------------------------------
# Part 3: Multiple Subplots
# -------------------------------------------------

# EXERCISE 6: Create a 2x2 grid of subplots with different plot types
# 1. Create a figure with a 2x2 grid of subplots
# 2. In the top-left: Plot a sine wave
# 3. In the top-right: Create a scatter plot
# 4. In the bottom-left: Plot a cosine wave
# 5. In the bottom-right: Create a histogram
# 6. Add appropriate titles to each subplot
# YOUR CODE HERE:



# -------------------------------------------------
# Part 4: Saving Plots
# -------------------------------------------------

# EXERCISE 7: Create and save a high-quality plot
# 1. Create a plot of your choice (line, scatter, or histogram)
# 2. Add appropriate labels, title, and customizations
# 3. Save the plot as a high-resolution PNG file
# YOUR CODE HERE:



# -------------------------------------------------
# Part 5: Real-world Application
# -------------------------------------------------

# EXERCISE 8: Data Analysis and Visualization Project
# We'll analyze a simulated dataset of student exam scores

# Generate sample data
np.random.seed(42)  # For reproducibility
midterm_scores = np.random.normal(70, 15, 100)  # Mean 70, std 15, 100 students
final_scores = midterm_scores + np.random.normal(5, 10, 100)  # Generally improved but with variation
final_scores = np.clip(final_scores, 0, 100)  # Ensure scores stay between 0 and 100

# YOUR TASKS:
# 1. Create a scatter plot of midterm vs. final scores with an appropriate title and labels
# 2. Create histograms of both midterm and final scores (use a 2x1 subplot)
# 3. Calculate and visualize the improvement from midterm to final (you might use a histogram or line plot)
# 4. BONUS: Add a diagonal line to the scatter plot representing "no change" in scores 
#           (i.e., where midterm score equals final score)
# YOUR CODE HERE:


# BONUS CHALLENGE: Create a custom visualization that effectively shows the distribution 
# of both scores along with their relationship
# Hint: Consider combining multiple plot types or using specialized plots like hexbin, contour, etc.
# YOUR CODE HERE: