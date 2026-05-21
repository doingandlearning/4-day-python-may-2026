# Lab Appx: Exploring Data with NumPy and pandas

This lab focuses on loading, inspecting, and summarising tabular data using NumPy and pandas.

You will practise:

- creating and operating on NumPy arrays
- loading a CSV file into a pandas DataFrame
- inspecting and filtering data
- computing summary statistics

---

## Hints and Tips

- Import conventions: `import numpy as np` and `import pandas as pd`.
- `df.head()` shows the first five rows — use it to sanity-check a load.
- Access a column with `df["column_name"]`; filter rows with a boolean expression.
- NumPy operates element-wise by default: `array * 2` doubles every value.
- Run `pip install numpy pandas` if either library is not already installed.

---

## Task 1: NumPy Arrays

Create a file `array_basics.py`.

Use NumPy to work with a short sequence of temperature readings.

Rules:

1. Create a NumPy array called `readings` containing: `[12.4, 15.1, 9.8, 22.3, 18.6, 11.0]`.
2. Print the mean, minimum, and maximum of the array.
3. Create a second array `above_mean` containing only the values greater than the mean.
4. Print `above_mean`.

<details>
<summary>Solution (Task 1)</summary>

```python
import numpy as np

readings = np.array([12.4, 15.1, 9.8, 22.3, 18.6, 11.0])

print("Mean:   ", readings.mean())
print("Min:    ", readings.min())
print("Max:    ", readings.max())

above_mean = readings[readings > readings.mean()]
print("Above mean:", above_mean)
```

</details>

---

## Task 2: Array Operations

Add to `array_basics.py`.

NumPy arrays support arithmetic directly — no loops needed.

Rules:

1. Convert `readings` from Celsius to Kelvin by adding `273.15` to the whole array. Store the result in `readings_kelvin`.
2. Round `readings_kelvin` to two decimal places using `np.round`.
3. Print `readings_kelvin`.

<details>
<summary>Solution (Task 2)</summary>

```python
import numpy as np

readings = np.array([12.4, 15.1, 9.8, 22.3, 18.6, 11.0])

readings_kelvin = readings + 273.15
readings_kelvin = np.round(readings_kelvin, 2)

print("Kelvin:", readings_kelvin)
```

</details>

---

## Task 3: Loading and Inspecting a DataFrame

Create a file `sensor_analysis.py`.

Save the following data as `sensor_readings.csv` in the same folder:

```text
timestamp,sensor_id,temperature_c,pressure_hpa
2024-01-15,A1,18.2,1013.1
2024-01-15,A2,19.4,1012.8
2024-01-15,B1,17.8,1014.2
2024-01-16,A1,20.1,1011.5
2024-01-16,A2,21.3,1010.9
2024-01-16,B1,19.7,1013.6
2024-01-17,A1,16.5,1015.0
2024-01-17,A2,17.2,1014.7
2024-01-17,B1,15.9,1016.1
```

Rules:

1. Load `sensor_readings.csv` into a DataFrame called `df`.
2. Print the first five rows using `df.head()`.
3. Print the column names and the shape of the DataFrame.
4. Print summary statistics using `df.describe()`.

<details>
<summary>Solution (Task 3)</summary>

```python
import pandas as pd

df = pd.read_csv("sensor_readings.csv")

print(df.head())
print()
print("Columns:", df.columns.tolist())
print("Shape:  ", df.shape)
print()
print(df.describe())
```

</details>

---

## Task 4: Filtering and Grouping

Continue in `sensor_analysis.py`.

Rules:

1. Filter the DataFrame to rows where `temperature_c` is above `19.0`. Store the result in `warm_readings` and print it.
2. Group the full DataFrame by `sensor_id` and compute the mean `temperature_c` for each sensor. Print the result.

<details>
<summary>Solution (Task 4)</summary>

```python
import pandas as pd

df = pd.read_csv("sensor_readings.csv")

warm_readings = df[df["temperature_c"] > 19.0]
print("Warm readings:")
print(warm_readings)
print()

mean_by_sensor = df.groupby("sensor_id")["temperature_c"].mean()
print("Mean temperature by sensor:")
print(mean_by_sensor)
```

</details>

---

## Task 5 (Optional): Adding a Derived Column

Continue in `sensor_analysis.py`.

Rules:

1. Add a new column `temperature_k` to `df` containing each temperature converted to Kelvin (add `273.15`).
2. Save the updated DataFrame to a new file called `sensor_readings_kelvin.csv` using `df.to_csv`. Set `index=False` so the row numbers are not written to the file.
3. Print a confirmation message with the number of rows saved.

<details>
<summary>Solution (Task 5 Optional)</summary>

```python
import pandas as pd

df = pd.read_csv("sensor_readings.csv")

df["temperature_k"] = df["temperature_c"] + 273.15

df.to_csv("sensor_readings_kelvin.csv", index=False)

print(f"Saved {len(df)} rows to sensor_readings_kelvin.csv")
```

</details>

---

## Reflection

- What is the advantage of using NumPy array operations instead of a `for` loop for the Kelvin conversion?
- Why does `df.describe()` only show numeric columns, and when is that useful?
- When would you use `groupby` instead of manually filtering and averaging each group?