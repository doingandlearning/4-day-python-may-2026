# Advanced Data Visualization Lab: Heatmaps and 3D Surface Plots - SOLUTION
# In this lab, you'll practice creating and customizing heatmaps and 3D surface plots

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# -------------------------------------------------------------
# Part 1: Creating Basic Heatmaps
# -------------------------------------------------------------

# EXERCISE 1: Create a basic heatmap with a 10x10 random matrix
# Use the viridis colormap and add a colorbar
plt.figure(figsize=(8, 6))
data = np.random.rand(10, 10)
plt.imshow(data, cmap="viridis", interpolation="nearest")
plt.colorbar(label="Intensity")
plt.title("Basic Heatmap with Random Data")
plt.savefig("ex1_basic_heatmap.png")
plt.close()
print("Exercise 1 completed: Basic heatmap created")

# EXERCISE 2: Create a heatmap with a custom colormap
# Use the 'hot' colormap and set interpolation to 'bicubic'
plt.figure(figsize=(8, 6))
data = np.random.rand(10, 10)
plt.imshow(data, cmap="hot", interpolation="bicubic")
plt.colorbar(label="Intensity")
plt.title("Heatmap with Hot Colormap and Bicubic Interpolation")
plt.savefig("ex2_custom_colormap_heatmap.png")
plt.close()
print("Exercise 2 completed: Custom colormap heatmap created")

# -------------------------------------------------------------
# Part 2: Creating Custom Labeled Heatmaps
# -------------------------------------------------------------

# EXERCISE 3: Create a correlation matrix heatmap
# 1. Generate a 5x5 correlation matrix (hint: use np.corrcoef with random data)
# 2. Create a heatmap with the 'coolwarm' colormap
# 3. Add custom labels for both axes: 'A', 'B', 'C', 'D', 'E'
plt.figure(figsize=(8, 6))
# Generate random data for 5 variables
random_data = np.random.randn(100, 5)
# Calculate correlation matrix
corr_matrix = np.corrcoef(random_data.T)
# Create heatmap
plt.imshow(corr_matrix, cmap="coolwarm", interpolation="nearest", vmin=-1, vmax=1)
plt.colorbar(label="Correlation Coefficient")
# Add custom labels
labels = ['A', 'B', 'C', 'D', 'E']
plt.xticks(ticks=np.arange(5), labels=labels)
plt.yticks(ticks=np.arange(5), labels=labels)
# Add title
plt.title("Correlation Matrix Heatmap")
plt.savefig("ex3_correlation_heatmap.png")
plt.close()
print("Exercise 3 completed: Correlation matrix heatmap created")

# EXERCISE 4: Create a heatmap with annotations
# 1. Generate a 6x6 matrix with random integers between 0 and 100
# 2. Create a heatmap and add text annotations showing the value in each cell
plt.figure(figsize=(10, 8))
# Generate random integer data
data = np.random.randint(0, 100, size=(6, 6))
# Create heatmap
im = plt.imshow(data, cmap="YlGnBu")
plt.colorbar(label="Value")
# Add text annotations
for i in range(6):
    for j in range(6):
        plt.text(j, i, f"{data[i, j]}", ha="center", va="center", 
                 color="black" if data[i, j] > 50 else "white")
# Add title
plt.title("Heatmap with Value Annotations")
plt.savefig("ex4_annotated_heatmap.png")
plt.close()
print("Exercise 4 completed: Annotated heatmap created")

# -------------------------------------------------------------
# Part 3: Basic 3D Surface Plots
# -------------------------------------------------------------

# EXERCISE 5: Create a basic 3D surface plot
# 1. Generate X and Y values from -5 to 5 with np.linspace and np.meshgrid
# 2. Calculate Z as sin(sqrt(X^2 + Y^2))
# 3. Create a 3D surface plot with the 'viridis' colormap
# Create a grid of X, Y values
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
# Calculate Z values
Z = np.sin(np.sqrt(X**2 + Y**2))
# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
# Plot the surface
surf = ax.plot_surface(X, Y, Z, cmap="viridis")
# Add color bar and labels
fig.colorbar(surf, label="Z Value")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Value")
plt.title("Basic 3D Surface Plot")
plt.savefig("ex5_basic_3d_surface.png")
plt.close()
print("Exercise 5 completed: Basic 3D surface plot created")

# EXERCISE 6: Create a 3D surface plot with a different function
# 1. Use the same X and Y values as in Exercise 5
# 2. Calculate Z as X^2 - Y^2 (a hyperbolic paraboloid)
# 3. Create a 3D surface plot with a different colormap of your choice
# Reuse X and Y from previous exercise
# Calculate Z values for hyperbolic paraboloid
Z = X**2 - Y**2
# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
# Plot the surface with a different colormap
surf = ax.plot_surface(X, Y, Z, cmap="plasma")
# Add color bar and labels
fig.colorbar(surf, label="Z Value")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Value")
plt.title("Hyperbolic Paraboloid Surface Plot")
plt.savefig("ex6_hyperbolic_paraboloid.png")
plt.close()
print("Exercise 6 completed: Hyperbolic paraboloid surface plot created")

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
# Create a grid of X, Y values in the range [-3, 3]
X = np.linspace(-3, 3, 50)
Y = np.linspace(-3, 3, 50)
X, Y = np.meshgrid(X, Y)
# Calculate Z values
Z = np.cos(X) * np.sin(Y)
# Create 3D plot
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection="3d")
# Plot the surface with custom settings
surf = ax.plot_surface(X, Y, Z, cmap="coolwarm", edgecolor="black", linewidth=0.5, alpha=0.8)
# Add color bar and labels
fig.colorbar(surf, label="Z Value")
ax.set_xlabel("X Axis", fontsize=12)
ax.set_ylabel("Y Axis", fontsize=12)
ax.set_zlabel("Z Value", fontsize=12)
ax.set_title("Customized 3D Surface Plot: cos(X) * sin(Y)", fontsize=14)
# Adjust view angle
ax.view_init(elev=30, azim=45)
plt.savefig("ex7_customized_3d_surface.png")
plt.close()
print("Exercise 7 completed: Customized 3D surface plot created")

# -------------------------------------------------------------
# Part 5: Applied Visualization
# -------------------------------------------------------------

# EXERCISE 8: Temperature Map
# Create a heatmap representing temperature data across a region
# 1. Generate a 10x10 grid with values between 10 and 30 (representing °C)
# 2. Add a temperature gradient at the top: cooler at the top, warmer at the bottom
# 3. Create a heatmap with a suitable colormap for temperature
# 4. Add a descriptive title and colorbar with the label "Temperature (°C)"
plt.figure(figsize=(10, 8))
# Generate base temperature data
base_temp = np.random.uniform(10, 20, (10, 10))
# Add a temperature gradient (cooler at top, warmer at bottom)
gradient = np.linspace(0, 10, 10).reshape(10, 1)
temp_data = base_temp + gradient
# Create heatmap with a temperature-appropriate colormap
plt.imshow(temp_data, cmap="RdYlBu_r", interpolation="bicubic")
plt.colorbar(label="Temperature (°C)")
# Add title and labels
plt.title("Regional Temperature Map", fontsize=14)
plt.xlabel("Longitude", fontsize=12)
plt.ylabel("Latitude", fontsize=12)
# Add grid lines
plt.grid(False)
plt.savefig("ex8_temperature_map.png")
plt.close()
print("Exercise 8 completed: Temperature map created")

# EXERCISE 9: 3D Terrain Visualization
# Create a 3D surface plot representing a terrain map
# 1. Generate a 50x50 grid
# 2. Create a terrain-like surface with multiple peaks and valleys
#    Hint: Use combinations of sin/cos functions or random noise
# 3. Use a terrain-appropriate colormap (like 'terrain' or 'gist_earth')
# 4. Add proper labels and a title
# Create a grid for the terrain
X = np.linspace(-3, 3, 50)
Y = np.linspace(-3, 3, 50)
X, Y = np.meshgrid(X, Y)
# Create terrain-like surface with multiple features
Z = (2 * np.sin(X) * np.cos(Y) + 
     np.sin(2*X) * np.cos(0.5*Y) + 
     0.5 * np.sin(X*Y) + 
     np.random.normal(0, 0.1, X.shape))  # Add some random noise
# Create 3D plot
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection="3d")
# Plot the surface with terrain colormap
surf = ax.plot_surface(X, Y, Z, cmap="terrain", edgecolor=None, linewidth=0, 
                      antialiased=True, shade=True)
# Add color bar and labels
fig.colorbar(surf, label="Elevation (m)")
ax