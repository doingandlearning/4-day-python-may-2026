import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# Part 1: Basic Plotting with Matplotlib
# -------------------------------------------------

# EXERCISE 1: Create a simple line plot of a sine wave
x = np.linspace(0, 2 * np.pi, 100)  # Generate x values
y = np.sin(x)  # Compute sine values

plt.figure(figsize=(8, 5))
plt.plot(x, y, label="Sine Wave", color="blue", linestyle="-")
plt.xlabel("X values (radians)")
plt.ylabel("Sine of X")
plt.title("Sine Wave Plot")
plt.legend()
plt.grid(True)
plt.show()


# EXERCISE 2: Create a scatter plot
x = np.random.uniform(0, 10, 50)  # Random x values between 0 and 10
y = x**2 + np.random.normal(0, 5, 50)  # Quadratic relationship with noise

plt.figure(figsize=(8, 5))
plt.scatter(x, y, color="red", alpha=0.7, label="Data Points")
plt.xlabel("X values")
plt.ylabel("Y = X^2 + noise")
plt.title("Scatter Plot of Quadratic Function")
plt.legend()
plt.grid(True)
plt.show()


# EXERCISE 3: Create a histogram
data = np.random.normal(70, 15, 1000)  # Generate normally distributed data

plt.figure(figsize=(8, 5))
plt.hist(data, bins=20, color="green", alpha=0.7, edgecolor="black")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.title("Histogram of Normally Distributed Scores")
plt.grid(True)
plt.show()

# -------------------------------------------------
# Part 2: Customizing Plots
# -------------------------------------------------

# EXERCISE 4: Compare sine and cosine with customizations
x = np.linspace(0, 2 * np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y_sin, label="Sine Wave", color="blue", linestyle="--", marker="o")
plt.plot(x, y_cos, label="Cosine Wave", color="red", linestyle="-.", marker="s")
plt.xlabel("X values (radians)")
plt.ylabel("Function Value")
plt.title("Comparison of Sine and Cosine")
plt.legend()
plt.grid(True)
plt.show()


# EXERCISE 5: Scatter plot with customized markers
x1 = np.random.uniform(0, 10, 30)
y1 = np.random.uniform(0, 10, 30)

x2 = np.random.uniform(0, 10, 30)
y2 = np.random.uniform(0, 10, 30)

plt.figure(figsize=(8, 5))
plt.scatter(x1, y1, color="red", marker="o", alpha=0.5, label="Group 1")
plt.scatter(x2, y2, color="blue", marker="^", alpha=0.5, label="Group 2")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot with Different Markers")
plt.legend()
plt.grid(True)
plt.show()

# -------------------------------------------------
# Part 3: Multiple Subplots
# -------------------------------------------------

# EXERCISE 6: 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Sine wave (Top-left)
axs[0, 0].plot(x, np.sin(x), color="blue")
axs[0, 0].set_title("Sine Wave")

# Scatter plot (Top-right)
axs[0, 1].scatter(x, y_sin, color="red", alpha=0.6)
axs[0, 1].set_title("Scatter Plot")

# Cosine wave (Bottom-left)
axs[1, 0].plot(x, np.cos(x), color="green")
axs[1, 0].set_title("Cosine Wave")

# Histogram (Bottom-right)
axs[1, 1].hist(data, bins=20, color="purple", edgecolor="black")
axs[1, 1].set_title("Histogram")

plt.tight_layout()
plt.show()

# -------------------------------------------------
# Part 4: Saving Plots
# -------------------------------------------------

# EXERCISE 7: Save a high-quality plot
plt.figure(figsize=(8, 5))
plt.plot(x, np.sin(x), label="Sine Wave", color="blue", linestyle="-")
plt.xlabel("X values")
plt.ylabel("Sine of X")
plt.title("Sine Wave Plot for Saving")
plt.legend()
plt.grid(True)

# Save the figure
plt.savefig("sine_wave_plot.png", dpi=300, bbox_inches="tight")
plt.show()

# -------------------------------------------------
# Part 5: Real-world Application
# -------------------------------------------------

# EXERCISE 8: Student Exam Scores Analysis
np.random.seed(42)  # Ensure reproducibility
midterm_scores = np.random.normal(70, 15, 100)
final_scores = midterm_scores + np.random.normal(5, 10, 100)
final_scores = np.clip(final_scores, 0, 100)  # Ensure scores stay in range

# Scatter plot of midterm vs. final scores
plt.figure(figsize=(8, 5))
plt.scatter(midterm_scores, final_scores, color="blue", alpha=0.6, label="Student Scores")
plt.plot([0, 100], [0, 100], linestyle="--", color="red", label="No Improvement Line")
plt.xlabel("Midterm Score")
plt.ylabel("Final Score")
plt.title("Midterm vs. Final Scores")
plt.legend()
plt.grid(True)
plt.show()

# Histograms of midterm and final scores (2x1 subplot)
fig, axs = plt.subplots(2, 1, figsize=(8, 10))

axs[0].hist(midterm_scores, bins=20, color="green", alpha=0.7, edgecolor="black")
axs[0].set_title("Histogram of Midterm Scores")

axs[1].hist(final_scores, bins=20, color="purple", alpha=0.7, edgecolor="black")
axs[1].set_title("Histogram of Final Scores")

plt.tight_layout()
plt.show()

# Improvement Visualization
improvement = final_scores - midterm_scores

plt.figure(figsize=(8, 5))
plt.hist(improvement, bins=15, color="orange", alpha=0.7, edgecolor="black")
plt.xlabel("Score Improvement")
plt.ylabel("Number of Students")
plt.title("Distribution of Score Improvements")
plt.grid(True)
plt.show()

# BONUS CHALLENGE: Custom Visualization
plt.figure(figsize=(8, 5))
plt.hexbin(midterm_scores, final_scores, gridsize=25, cmap="coolwarm")
plt.colorbar(label="Density")
plt.xlabel("Midterm Score")
plt.ylabel("Final Score")
plt.title("Hexbin Plot of Midterm vs. Final Scores")
plt.grid(True)
plt.show()
