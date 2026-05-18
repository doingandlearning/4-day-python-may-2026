# Lab 15: Reading Temperature Data from CSV

This lab focuses on loading temperature readings from a CSV file into class instances.

You will practise:

- defining a small class for one reading
- reading CSV rows with the `csv` module
- validating rows before creating objects
- prompting for a filename with a sensible default

---

## Hints and Tips

- Use `with open(filename, newline="")` when reading CSV files.
- `csv.reader` yields each row as a list of strings—convert numbers with `float()`.
- Skip bad rows with `continue` after printing a short message.
- Use `input().strip()`; if the result is empty, default to `"data.csv"`.
- Write output to a new file if you export results—do not overwrite raw data.

---

## Task 1: TemperatureReading Class

Create `loader.py` and define:

`TemperatureReading`

Rules:

1. `__init__(self, temp, date, location, scale="Celsius")` stores all fields.
2. `__str__` returns a readable line, e.g. `22.5°C on 2025-05-01 at Geneva`.
3. Create one instance in code and print it to verify.

<details>
<summary>Solution (Task 1)</summary>

```python
class TemperatureReading:
    def __init__(self, temp, date, location, scale="Celsius"):
        self.temp = temp
        self.date = date
        self.location = location
        self.scale = scale

    def __str__(self):
        return f"{self.temp}°{self.scale[0]} on {self.date} at {self.location}"


sample = TemperatureReading(22.5, "2025-05-01", "Geneva")
print(sample)
```

</details>

---

## Task 2: Create data.csv

Create `data.csv` in the same folder with at least seven rows.

Format (four columns per row):

```text
temp,scale,date,location
22.5,Celsius,2025-05-01,Geneva
21.0,Celsius,2025-05-02,Geneva
```

Rules:

1. Use ISO-style dates (`YYYY-MM-DD`).
2. Include at least one row you will treat as malformed in Task 3 (e.g. missing a column) to test skipping.

<details>
<summary>Solution (Task 2)</summary>

Example `data.csv`:

```text
22.5,Celsius,2025-05-01,Geneva
21.0,Celsius,2025-05-02,Geneva
19.5,Celsius,2025-05-03,Geneva
24.0,Celsius,2025-05-04,Geneva
18.0,Celsius,2025-05-05,Geneva
23.5,Celsius,2025-05-06,Geneva
20.0,Celsius,2025-05-07,Geneva
badrow
```

</details>

---

## Task 3: load_data Function

In `loader.py`, write:

`load_data(filename)`

Rules:

1. Open the file with `with open(...)` and `csv.reader`.
2. Expect four columns: temperature, scale, date, location.
3. Convert temperature to `float`; skip rows with wrong column count or invalid temperature.
4. Print `Skipping malformed row: ...` for skipped rows.
5. Return a list of `TemperatureReading` objects.

<details>
<summary>Solution (Task 3)</summary>

```python
import csv


class TemperatureReading:
    def __init__(self, temp, date, location, scale="Celsius"):
        self.temp = temp
        self.date = date
        self.location = location
        self.scale = scale

    def __str__(self):
        return f"{self.temp} {self.scale} on {self.date} at {self.location}"


def load_data(filename):
    readings = []
    with open(filename, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) != 4:
                print(f"Skipping malformed row: {row}")
                continue
            temp_str, scale, date, location = row
            try:
                temp = float(temp_str)
            except ValueError:
                print(f"Skipping malformed row: {row}")
                continue
            readings.append(TemperatureReading(temp, date, location, scale))
    return readings
```

</details>

---

## Task 4: Main Script with User Input

Add a main block to `loader.py`.

Rules:

1. Prompt: `Enter CSV filename (default data.csv): `.
2. If the user enters nothing, use `data.csv`.
3. Call `load_data`, print how many readings loaded, then print each reading.

Example output:

```text
Loaded 7 temperature readings
22.5 Celsius on 2025-05-01 at Geneva
...
```

<details>
<summary>Solution (Task 4)</summary>

```python
import csv


class TemperatureReading:
    def __init__(self, temp, date, location, scale="Celsius"):
        self.temp = temp
        self.date = date
        self.location = location
        self.scale = scale

    def __str__(self):
        return f"{self.temp} {self.scale} on {self.date} at {self.location}"


def load_data(filename):
    readings = []
    with open(filename, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) != 4:
                print(f"Skipping malformed row: {row}")
                continue
            temp_str, scale, date, location = row
            try:
                temp = float(temp_str)
            except ValueError:
                print(f"Skipping malformed row: {row}")
                continue
            readings.append(TemperatureReading(temp, date, location, scale))
    return readings


filename = input("Enter CSV filename (default data.csv): ").strip()
if filename == "":
    filename = "data.csv"

temperatures = load_data(filename)
print(f"Loaded {len(temperatures)} temperature readings")
for reading in temperatures:
    print(reading)
```

</details>

---

## Task 5 (Optional): Filter Warm Readings

Rules:

1. After loading, print only readings above `20.0`°C (Celsius rows only).
2. Print the count of warm readings.

<details>
<summary>Solution (Task 5 Optional)</summary>

```python
warm = []
for reading in temperatures:
    if reading.scale == "Celsius" and reading.temp > 20.0:
        warm.append(reading)

print(f"Warm readings: {len(warm)}")
for reading in warm:
    print(reading)
```

</details>

---

## Reflection

- Why is it safer to skip bad rows than to stop the whole program?
- What would break if a row used `DD/MM/YYYY` instead of ISO dates?
- Where would you add code to write filtered readings to a new CSV file?
