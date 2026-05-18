# **Introduction to NumPy and Matplotlib for Data Analysis and Visualization**

---

## **📌 Learning Objectives**
By the end of this workshop, participants will be able to:  
✅ Use **NumPy** for efficient numerical computations  
✅ Perform **basic and advanced array operations**  
✅ Load and manipulate **large datasets**  
✅ Generate **visualizations using Matplotlib**  
✅ Create **line plots, histograms, and heatmaps**  
✅ Customize plots for **scientific presentations**  

---

## **🔹 Workshop Outline**
### **1️⃣ NumPy Basics: Understanding Arrays and Performance**
- Why use NumPy instead of Python lists?
- Creating arrays (`np.array()`, `np.arange()`, `np.linspace()`)
- Reshaping and slicing arrays
- Performance comparison: Python lists vs. NumPy arrays  


#### **Why Use NumPy Instead of Python Lists?**
Python lists are **flexible** and **built-in**, but they are **slow** and **inefficient for numerical computations**. NumPy provides:
✅ **Speed**: Operations on NumPy arrays are **much faster** than Python lists.  
✅ **Memory Efficiency**: NumPy uses **fixed-type** arrays, while Python lists store mixed data types.  
✅ **Vectorization**: NumPy allows **element-wise operations** without loops.  
✅ **Advanced Features**: Supports **broadcasting, slicing, reshaping, and matrix operations**.

---

### **1️⃣ Creating Arrays in NumPy**
In NumPy, we create arrays using **`np.array()`**, **`np.arange()`**, and **`np.linspace()`**.

#### **📌 Example 1: `np.array()` (Creating from a List)**
```python
import numpy as np

# Creating a 1D array from a Python list
arr = np.array([1, 2, 3, 4, 5])
print(arr)  
# Output: [1 2 3 4 5]
```
🔹 **Key Benefit:** NumPy stores data **more efficiently** than a Python list.

---

#### **📌 Example 2: `np.arange()` (Creating Sequences)**
```python
arr = np.arange(0, 10, 2)  # Start at 0, go up to 10 (exclusive), step by 2
print(arr)
# Output: [ 0  2  4  6  8]
```
🔹 **Why Use `np.arange()`?**  
- **Cleaner than `range()`** because it directly creates an array.  
- **More efficient for numerical computations.**

---

#### **📌 Example 3: `np.linspace()` (Creating Evenly Spaced Values)**
```python
arr = np.linspace(0, 10, 5)  # Start at 0, end at 10, create 5 equally spaced numbers
print(arr)
# Output: [ 0.   2.5  5.   7.5 10. ]
```
🔹 **Why Use `np.linspace()`?**  
- Perfect for **plotting and numerical simulations** where we need **even spacing**.  

---

### **2️⃣ Reshaping and Slicing Arrays**
NumPy allows **reshaping** and **slicing** of arrays efficiently.

#### **📌 Example 4: Reshaping Arrays**
```python
arr = np.arange(1, 10)  # Creates an array [1, 2, 3, ..., 9]
reshaped = arr.reshape(3, 3)  # Converts to 3x3 matrix
print(reshaped)
```
🔹 **Why Reshape?**  
- Makes **matrix operations** easier.
- Enables **better visualization**.

**Output:**
```
[[1 2 3]
 [4 5 6]
 [7 8 9]]
```

---

#### **📌 Example 5: Slicing NumPy Arrays**
```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])  # Slice from index 1 to 3 (excludes 4)
# Output: [20 30 40]

print(arr[:3])  # First three elements
# Output: [10 20 30]

print(arr[-2:])  # Last two elements
# Output: [40 50]
```
🔹 **Why Slice in NumPy?**  
- Faster than slicing Python lists.
- Returns a **view (not a copy)**—modifying the slice **modifies the original array**.

---

### **3️⃣ Performance Comparison: Python Lists vs. NumPy Arrays**
NumPy is **significantly faster** than Python lists for numerical operations.

#### **📌 Example 6: Summing a Large List vs. NumPy Array**
```python
import time

size = 10**6  # 1 million elements

# Python List
py_list = list(range(size))
start = time.time()
sum(py_list)
print("Python list sum time:", time.time() - start)

# NumPy Array
np_arr = np.arange(size)
start = time.time()
np.sum(np_arr)
print("NumPy sum time:", time.time() - start)
```
**Expected Output (Varies by System, but NumPy is Much Faster)**
```
Python list sum time: 0.12 sec
NumPy sum time: 0.002 sec
```
🔹 **Why is NumPy Faster?**  
- NumPy uses **vectorized** operations in **compiled C code**.  
- Python lists **loop over each element in interpreted Python**, making them **slower**.

---

#### **📌 Example 7: Element-Wise Operations in NumPy**  
One of the **biggest advantages of NumPy** over Python lists is that it supports **element-wise operations** without requiring loops.

---

#### **Basic Element-Wise Operations**
```python
import numpy as np

# Create two NumPy arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

# Element-wise addition
print(arr1 + arr2)  
# Output: [11 22 33 44 55]

# Element-wise multiplication
print(arr1 * arr2)  
# Output: [ 10  40  90 160 250]

# Element-wise division
print(arr2 / arr1)  
# Output: [10. 10. 10. 10. 10.]

# Element-wise exponentiation
print(arr1 ** 2)  
# Output: [ 1  4  9 16 25]
```

🔹 **Why is this useful?**  
✅ No need for **loops**—operations are applied to **each element automatically**.  
✅ Much **faster** than using Python lists with loops.  

---

#### **Broadcasting: Operations with Scalars**
You can also perform operations **between an array and a single number** (scalar), and NumPy **broadcasts** the operation to all elements.

```python
arr = np.array([1, 2, 3, 4, 5])

print(arr + 10)  # Adds 10 to every element
# Output: [11 12 13 14 15]

print(arr * 2)  # Multiplies every element by 2
# Output: [ 2  4  6  8 10]

print(arr / 2)  # Divides every element by 2
# Output: [0.5 1.  1.5 2.  2.5]
```

🔹 **Why is this useful?**  
✅ **Quick transformations** (e.g., converting units).  
✅ **No need for loops**—the operation applies to **each element automatically**.

---

### **Comparison: NumPy vs. Python Lists**
Let’s compare **element-wise operations** in **Python lists vs. NumPy arrays**.

#### **📌 Example 8: Squaring Each Element in a List vs. NumPy**
#### **Using a Python List (Loop Required)**
```python
py_list = [1, 2, 3, 4, 5]
squared_list = [x ** 2 for x in py_list]  # Using list comprehension
print(squared_list)
# Output: [1, 4, 9, 16, 25]
```

#### **Using NumPy (Vectorized Operation)**
```python
arr = np.array([1, 2, 3, 4, 5])
squared_arr = arr ** 2  # No loop needed!
print(squared_arr)
# Output: [ 1  4  9 16 25]
```

🔹 **Key Takeaways**  
✅ **NumPy is faster**—no explicit loops.  
✅ **Code is shorter & cleaner**.  

---

### **🚀 Why Use Element-Wise Operations in NumPy?**
| Operation | Python Lists | NumPy Arrays |
|-----------|-------------|--------------|
| **Addition** | `for i in range(len(a)): result.append(a[i] + b[i])` | `a + b` |
| **Multiplication** | `for i in range(len(a)): result.append(a[i] * b[i])` | `a * b` |
| **Division** | `for i in range(len(a)): result.append(a[i] / b[i])` | `a / b` |
| **Exponentiation** | `for i in range(len(a)): result.append(a[i] ** 2)` | `a ** 2` |

---

### **🚀 Summary: Why Use NumPy Over Python Lists?**
| Feature | Python List | NumPy Array |
|---------|------------|------------|
| **Speed** | ❌ Slow (loops in Python) | ✅ Fast (vectorized C code) |
| **Memory Efficiency** | ❌ Stores mixed types | ✅ Fixed-type, less memory |
| **Operations** | ❌ Requires loops | ✅ Element-wise operations |
| **Advanced Features** | ❌ No built-in reshaping, broadcasting | ✅ Supports reshaping, slicing, broadcasting |



---

## **📌 Working with Data Files in NumPy**
NumPy provides efficient ways to **read, write, and process data from files**, especially for large datasets. This guide covers:

✅ **Reading structured data** using `np.loadtxt()` and `np.genfromtxt()`  
✅ **Handling missing values** in NumPy arrays  
✅ **Boolean masking and filtering** for efficient data selection  

---

### **1️⃣ Reading Data from Files**
When working with large numerical datasets, plain text files (`.csv`, `.txt`) are common. NumPy provides:
- **`np.loadtxt()`**: Simple and fast for structured data.
- **`np.genfromtxt()`**: More flexible, handles missing values.
- **`np.savetxt()`**: Saves NumPy arrays to text files.

---

#### **📌 Example 1: Reading a CSV File with `np.loadtxt()`**
Use `np.loadtxt()` to read structured numerical data **without missing values**.

#### **🔹 Sample File (`data.csv`):**
```
10.5, 20.3, 30.1
15.2, 25.4, 35.6
```
#### **🔹 Reading Data into a NumPy Array**
```python
import numpy as np

# Load the file (comma-separated)
data = np.loadtxt("data.csv", delimiter=",")

print(data)
# Output:
# [[10.5 20.3 30.1]
#  [15.2 25.4 35.6]]
```
🔹 **Why Use `np.loadtxt()`?**  
✅ **Fastest method** for structured numerical data.  
✅ **Auto-converts data to NumPy arrays** (no need for loops).  
❌ **Does NOT support missing values**—use `np.genfromtxt()` for that.

---

#### **📌 Example 2: Handling Missing Values with `np.genfromtxt()`**
If your dataset **contains missing values**, `np.loadtxt()` **will fail**. Instead, use `np.genfromtxt()`.

##### **🔹 Sample File (`data_with_missing.csv`):**
```
10.5, 20.3, 30.1
15.2, , 35.6  # Missing value in the second column
```
#### **🔹 Reading with `np.genfromtxt()`**
```python
data = np.genfromtxt("data_with_missing.csv", delimiter=",", filling_values=-1)
print(data)
```
🔹 **Why Use `np.genfromtxt()`?**  
✅ **Handles missing values gracefully** (default = `NaN` or custom fill value).  
✅ **Supports heterogeneous data types (`dtype` argument)**.  
✅ **More flexible than `np.loadtxt()`**.

---

#### **📌 Example 3: Saving a NumPy Array to a File with `np.savetxt()`**
You can **export NumPy arrays** to text files using `np.savetxt()`.

```python
arr = np.array([[10.5, 20.3, 30.1], [15.2, 25.4, 35.6]])

# Save to CSV file
np.savetxt("output.csv", arr, delimiter=",", fmt="%.2f")

print("Data saved to output.csv")
```
🔹 **Why Use `np.savetxt()`?**  
✅ **Simple way to save NumPy arrays to files**.  
✅ **Customizable format (`fmt="%.2f"` for 2 decimal places)**.  

---

### **2️⃣ Handling Missing Data in NumPy**
NumPy represents missing values using `np.nan` (Not-a-Number).

### **📌 Example 4: Detecting and Replacing Missing Values**
```python
import numpy as np

data = np.array([10.5, np.nan, 20.3, np.nan, 30.1])

# Detect missing values
print(np.isnan(data))  
# Output: [False  True False  True False]

# Replace NaN with a default value (e.g., 0)
data[np.isnan(data)] = 0

print(data)
# Output: [10.5  0.  20.3  0.  30.1]
```
🔹 **Why Handle `np.nan`?**  
✅ **Prevents errors in computations** (e.g., mean, sum).  
✅ **Allows setting custom fill values for missing data**.

---

### **3️⃣ Boolean Masking and Filtering**
Boolean masking is a **powerful way to filter** data based on conditions.

### **📌 Example 5: Filtering Values Based on Conditions**
```python
import numpy as np

data = np.array([10, 15, 20, 25, 30])

# Create a mask for values greater than 15
mask = data > 15

print(mask)
# Output: [False False  True  True  True]

# Use the mask to filter the array
filtered_data = data[mask]
print(filtered_data)
# Output: [20 25 30]
```
🔹 **Why Use Boolean Masking?**  
✅ **Avoids loops**, making filtering much faster.  
✅ **Easily extracts subsets of data**.

---

#### **📌 Example 6: Combining Multiple Conditions**
```python
data = np.array([10, 15, 20, 25, 30])

# Select values between 15 and 30
filtered_data = data[(data >= 15) & (data <= 30)]
print(filtered_data)
# Output: [15 20 25 30]
```
🔹 **Why Use `&` and `|` Instead of `and`/`or`?**  
❌ `and` / `or` **won't work** on NumPy arrays.  
✅ **Use `&` (AND) and `|` (OR) for element-wise operations.**

---

### **🚀 Summary**
| **Feature** | **Method** | **Key Benefit** |
|------------|------------|----------------|
| **Read Data** | `np.loadtxt()` | Fast, structured numerical data |
| **Read with Missing Data** | `np.genfromtxt()` | Handles NaN, flexible |
| **Save Data** | `np.savetxt()` | Easy way to save NumPy arrays |
| **Detect Missing Values** | `np.isnan()` | Identifies NaN values |
| **Replace Missing Values** | `data[np.isnan(data)] = value` | Allows setting default values |
| **Filter Data** | `data[data > value]` | Fast boolean filtering |


---

## **📌 Data Visualization with Matplotlib**
Matplotlib is **the most widely used** Python library for plotting and visualizing data. This section covers:

✅ **Basic plotting types:** `plot()`, `scatter()`, `hist()`  
✅ **Customizing plots:** Titles, labels, grids, colors, markers  
✅ **Saving plots for reports**  

---

### **1️⃣ Basic Plotting in Matplotlib**
Matplotlib provides several types of plots. Let's start with **line plots, scatter plots, and histograms**.

---

#### **📌 Example 1: Line Plot (`plt.plot()`)**
A **line plot** is used to visualize continuous data.

```python
import numpy as np
import matplotlib.pyplot as plt

# Generate 100 evenly spaced values between 0 and 10
x = np.linspace(0, 10, 100)
y = np.sin(x)  # Apply sine function

# Create a line plot
plt.plot(x, y, label="Sine Wave", color="blue", linestyle="--", linewidth=2)

# Add labels and title
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Sine Wave Plot")

# Add legend and grid
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
```

🔹 **Why Use `plt.plot()`?**  
✅ Best for **time series** and **continuous data**.  
✅ Supports **line styles, colors, and markers**.  
✅ Easy to **add grid, legend, and labels**.

---

#### **📌 Example 2: Scatter Plot (`plt.scatter()`)**
A **scatter plot** is useful for visualizing relationships between two variables.

```python
# Generate random data
np.random.seed(42)
x = np.random.rand(50) * 10  # X values between 0 and 10
y = np.random.rand(50) * 100  # Y values between 0 and 100

# Create a scatter plot
plt.scatter(x, y, color="red", marker="o", alpha=0.7, label="Data Points")

# Add labels and title
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Scatter Plot Example")

# Show legend
plt.legend()

# Show plot
plt.show()
```

🔹 **Why Use `plt.scatter()`?**  
✅ Best for **showing relationships** in **large datasets**.  
✅ Supports **custom colors, markers, and transparency (`alpha`)**.  

---

#### **📌 Example 3: Histogram (`plt.hist()`)**
A **histogram** shows the distribution of data.

```python
# Generate random normally distributed data
data = np.random.normal(loc=50, scale=15, size=1000)

# Create a histogram
plt.hist(data, bins=30, color="green", alpha=0.7, edgecolor="black")

# Add labels and title
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Data")

# Show the plot
plt.show()
```

🔹 **Why Use `plt.hist()`?**  
✅ Best for **analyzing distributions**.  
✅ Customizable **bins, colors, transparency**.  
✅ Essential for **data exploration**.

---

### **2️⃣ Customizing Plots**
A good plot **is clear, readable, and informative**. Matplotlib allows:
- **Adding titles and labels**
- **Customizing colors, markers, and line styles**
- **Adding legends and grids**

---

#### **📌 Example 4: Customizing a Line Plot**
```python
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="Sine Wave", color="blue", linestyle="--", linewidth=2, marker="o")
plt.plot(x, y2, label="Cosine Wave", color="red", linestyle="-", linewidth=2, marker="x")

# Customization
plt.xlabel("Time (s)", fontsize=12, color="darkgreen")
plt.ylabel("Amplitude", fontsize=12, color="darkred")
plt.title("Customized Sine & Cosine Waves", fontsize=14, fontweight="bold")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

# Show the plot
plt.show()
```

🔹 **Key Customizations:**  
✅ **Line styles (`--`, `-`, `:`) & markers (`o`, `x`)**  
✅ **Custom colors & font sizes**  
✅ **Grid styling**  

---

#### **📌 Example 5: Multiple Subplots (`plt.subplot()`)**
Sometimes, we need **multiple plots in one figure**.

```python
fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # 2x2 grid

# Line plot
axs[0, 0].plot(x, y1, color="blue")
axs[0, 0].set_title("Sine Wave")

# Scatter plot
axs[0, 1].scatter(x, y1, color="red")
axs[0, 1].set_title("Scatter Plot")

# Histogram
axs[1, 0].hist(data, bins=20, color="green", edgecolor="black")
axs[1, 0].set_title("Histogram")

# Cosine wave
axs[1, 1].plot(x, y2, color="purple")
axs[1, 1].set_title("Cosine Wave")

# Adjust layout
plt.tight_layout()
plt.show()
```

🔹 **Why Use Subplots?**  
✅ Best for **comparing multiple datasets**.  
✅ Keeps related plots **in a single figure**.  
✅ Easy to **adjust layout and size**.

---

### **3️⃣ Saving Plots for Reports**
Use `plt.savefig()` to **export plots as images** for reports and presentations.

```python
plt.plot(x, y1, label="Sine Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Sine Wave Plot")
plt.legend()

# Save the figure
plt.savefig("sine_wave.png", dpi=300, bbox_inches="tight")

# Show the plot
plt.show()
```

🔹 **Why Use `plt.savefig()`?**  
✅ Saves plots in **high-quality PNG, PDF, SVG, EPS** formats.  
✅ **`dpi=300`** ensures **high resolution**.  
✅ **`bbox_inches="tight"`** prevents **extra white space**.

---

### **🚀 Summary**
| **Feature** | **Method** | **Best For** |
|------------|------------|--------------|
| **Line Plot** | `plt.plot()` | Time series, trends |
| **Scatter Plot** | `plt.scatter()` | Relationships, correlations |
| **Histogram** | `plt.hist()` | Data distribution |
| **Customize Plots** | Titles, labels, grid, colors | Better readability |
| **Multiple Plots** | `plt.subplot()` | Side-by-side comparisons |
| **Save Plots** | `plt.savefig()` | Reports, presentations |


---

## **Advanced Visualization: Heatmaps and 3D Plots**

For **scientific and engineering applications**, **heatmaps** and **3D surface plots** help **visualize multi-dimensional data**.

---

### **1️⃣ Creating Heatmaps with `imshow()`**
A **heatmap** is a **color-coded matrix** used to visualize the **intensity of values** in a 2D dataset.

#### **📌 Example 1: Generating a Basic Heatmap**
```python
import numpy as np
import matplotlib.pyplot as plt

# Generate a 10x10 matrix with random values
data = np.random.rand(10, 10)  

# Create heatmap
plt.imshow(data, cmap="viridis", interpolation="nearest")

# Add color bar (indicates intensity levels)
plt.colorbar(label="Intensity")

# Add title
plt.title("Heatmap of Random Data")

# Show the plot
plt.show()
```

🔹 **Key Concepts**:
- **`cmap="viridis"`**: Defines the **colormap** (other options: `"hot"`, `"cool"`, `"jet"`).
- **`interpolation="nearest"`**: Ensures that each value in the matrix is clearly shown (without smoothing).
- **`plt.colorbar()`**: Adds a **color legend** to explain intensity levels.

---

#### **📌 Example 2: Heatmap with Custom Labels and Grid**
```python
# Generate random 6x6 data
data = np.random.rand(6, 6)

# Define row and column labels
row_labels = ["A", "B", "C", "D", "E", "F"]
col_labels = ["W", "X", "Y", "Z", "V", "U"]

# Create heatmap
plt.imshow(data, cmap="coolwarm", interpolation="nearest")

# Add color bar
plt.colorbar(label="Measurement Intensity")

# Customize tick labels
plt.xticks(ticks=np.arange(6), labels=col_labels)
plt.yticks(ticks=np.arange(6), labels=row_labels)

# Add title
plt.title("Labeled Heatmap")

plt.show()
```

🔹 **Why Use Custom Labels?**  
✅ Helps **interpret data better** when working with categorical axes.  
✅ Useful for **confusion matrices, correlation matrices**, and **spatial data visualization**.  

---

### **2️⃣ Creating 3D Surface Plots**
A **3D surface plot** helps visualize relationships between **three continuous variables**.

---

#### **📌 Example 3: Basic 3D Surface Plot**
```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a grid of X, Y values
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)  # Create 2D grid

# Define a function for Z values
Z = np.sin(np.sqrt(X**2 + Y**2))  

# Create a 3D figure
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection="3d")

# Plot the surface
surf = ax.plot_surface(X, Y, Z, cmap="viridis")

# Add color bar and title
fig.colorbar(surf)
plt.title("3D Surface Plot")

# Show the plot
plt.show()
```

🔹 **Key Concepts**:
- **`np.meshgrid(X, Y)`**: Creates a **grid** for 3D plotting.
- **`plot_surface(X, Y, Z, cmap="viridis")`**: Renders the **3D shape**.
- **Color bar** represents **function intensity (Z-values).**

---

#### **📌 Example 4: Customizing a 3D Surface Plot**
```python
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection="3d")

# Create a different function
Z = np.cos(X) * np.sin(Y)

# Customize the surface plot
surf = ax.plot_surface(X, Y, Z, cmap="coolwarm", edgecolor="black", linewidth=0.5)

# Labels
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Value")
plt.title("Customized 3D Surface Plot")

# Add color bar
fig.colorbar(surf)

plt.show()
```

🔹 **Customizations**:
✅ **Change colormap**: `"coolwarm"`, `"plasma"`, `"inferno"`.  
✅ **Add edge colors** for better visibility.  
✅ **Label axes for clarity**.  

---

### **🚀 Summary: When to Use Heatmaps vs. 3D Plots**
| **Visualization** | **Best Use Cases** | **Matplotlib Function** |
|------------------|------------------|------------------|
| **Heatmap (`imshow`)** | Matrices, correlation data, intensity maps | `plt.imshow()` |
| **3D Surface Plot** | Function visualization, terrain maps | `ax.plot_surface()` |

---


### **🔹 Additional Resources**
- **NumPy Documentation**: [https://numpy.org/doc/stable/](https://numpy.org/doc/stable/)  
- **Matplotlib Documentation**: [https://matplotlib.org/stable/](https://matplotlib.org/stable/)  
- **SciPy and Pandas for Next Steps**  