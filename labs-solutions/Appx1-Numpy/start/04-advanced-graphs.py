# Advanced Data Visualization Lab: Heatmaps and 3D Surface Plots
# In this lab, you'll practice creating and customizing heatmaps and 3D surface plots

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# -------------------------------------------------------------
# Part 1: Creating Basic Heatmaps
# -------------------------------------------------------------

# EXERCISE 1: Create a basic heatmap with a 10x10 random matrix
# Use the viridis colormap and add a colorbar
# YOUR CODE HERE:


# EXERCISE 2: Create a heatmap with a custom colormap
# Use the 'hot' colormap and set interpolation to 'bicubic'
# YOUR CODE HERE:


# -------------------------------------------------------------
# Part 2: Creating Custom Labeled Heatmaps
# -------------------------------------------------------------

# EXERCISE 3: Create a correlation matrix heatmap
# 1. Generate a 5x5 correlation matrix (hint: use np.corrcoef with random data)
# 2. Create a heatmap with the 'coolwarm' colormap
# 3. Add custom labels for both axes: 'A', 'B', 'C', 'D', 'E'
# YOUR CODE HERE:


# EXERCISE 4: Create a heatmap with annotations
# 1. Generate a 6x6 matrix with random integers between 0 and 100
# 2. Create a heatmap and add text annotations showing the value in each cell
# YOUR CODE HERE:


# -------------------------------------------------------------
# Part 3: Basic 3D Surface Plots
# -------------------------------------------------------------

# EXERCISE 5: Create a basic 3D surface plot
# 1. Generate X and Y values from -5 to 5 with np.linspace and np.meshgrid
# 2. Calculate Z as sin(sqrt(X^2 + Y^2))
# 3. Create a 3D surface plot with the 'viridis' colormap
# YOUR CODE HERE:


# EXERCISE 6: Create a 3D surface plot with a different function
# 1. Use the same X and Y values as in Exercise 5
# 2. Calculate Z as X^2 - Y^2 (a hyperbolic paraboloid)
# 3. Create a 3D surface plot with a different colormap of your choice
# YOUR CODE HERE:


# -------------------------------------------------------------
# Part 4: Customizing 3D Surface Plots
# -------------------------------------------------------------

# EXERCISE 7: Create a customized 3D surface plot
# 1. Generate X and Y values from -3 to 3
# 2. Calculate Z as cos(X) * sin(Y)
# 3. Create a 3D surface plot with:
#    - Custom colormap
#    - Edge colors
#    - Axis labels
#    - Title
# YOUR CODE HERE:


# -------------------------------------------------------------
# Part 5: Applied Visualization
# -------------------------------------------------------------

# EXERCISE 8: Temperature Map
# Create a heatmap representing temperature data across a region
# 1. Generate a 10x10 grid with values between 10 and 30 (representing °C)
# 2. Add a temperature gradient at the top: cooler at the top, warmer at the bottom
# 3. Create a heatmap with a suitable colormap for temperature
# 4. Add a descriptive title and colorbar with the label "Temperature (°C)"
# YOUR CODE HERE:


# EXERCISE 9: 3D Terrain Visualization
# Create a 3D surface plot representing a terrain map
# 1. Generate a 50x50 grid
# 2. Create a terrain-like surface with multiple peaks and valleys
#    Hint: Use combinations of sin/cos functions or random noise
# 3. Use a terrain-appropriate colormap (like 'terrain' or 'gist_earth')
# 4. Add proper labels and a title
# YOUR CODE HERE:


# -------------------------------------------------------------
# Part 6: Combining Plots
# -------------------------------------------------------------

# EXERCISE 10: Create a figure with both a heatmap and its 3D representation
# 1. Create a 2x1 subplot layout
# 2. In the first subplot, create a heatmap of a function of your choice
# 3. In the second subplot, create a 3D surface plot of the same function
# 4. Add a single colorbar that applies to both plots
# 5. Add a main title for the entire figure
# YOUR CODE HERE:


# Save your visualizations
plt.savefig('visualization_lab_results.png')
print("Congratulations! You've completed the Advanced Data Visualization Lab!")