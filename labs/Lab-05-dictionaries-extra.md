# Lab 5 Extra: Dictionaries and Data Lookup

This lab focuses on storing, updating, and querying scientific data with dictionaries.

You will practise:

- reading and updating key–value pairs
- looping over `.keys()`, `.values()`, and `.items()`
- using `.get()` and `in` for safe lookups
- building simple frequency counts with dictionaries

---

## Hints and Tips

- Use `.items()` when you need both key and value in a loop.
- Use `in` to test whether a key exists before relying on it.
- Use `.get(key, default)` when a key might be missing.
- To count occurrences, use a dict: if the key is new, set count to 1; otherwise add 1.
- Prefer ISO-style dates (`YYYY-MM-DD`) when you add date fields later in the course.

---

## Task 1: Sensor Readings

Start with this dictionary of sensor temperatures:

```python
sensor_readings = {
    "Sensor_A": 23.5,
    "Sensor_B": 24.1,
    "Sensor_C": 22.8,
    "Sensor_D": 25.2,
    "Sensor_E": 23.9,
}
```

Rules:

1. Print all sensor names and all readings.
2. Print the reading for `Sensor_A`.
3. Add `Sensor_F` with value `24.7` and update `Sensor_B` to `25.1`.
4. Remove `Sensor_C`.
5. Find the sensor with the highest and lowest reading.
6. Print sensors with readings above 24°C.

<details>
<summary>Solution (Task 1)</summary>

```python
sensor_readings = {
    "Sensor_A": 23.5,
    "Sensor_B": 24.1,
    "Sensor_C": 22.8,
    "Sensor_D": 25.2,
    "Sensor_E": 23.9,
}

print("Sensors:", list(sensor_readings.keys()))
print("Readings:", list(sensor_readings.values()))
print("Sensor_A:", sensor_readings["Sensor_A"])

sensor_readings["Sensor_F"] = 24.7
sensor_readings["Sensor_B"] = 25.1
del sensor_readings["Sensor_C"]

highest_sensor = None
highest_value = -999
lowest_sensor = None
lowest_value = 999

for sensor, value in sensor_readings.items():
    if value > highest_value:
        highest_value = value
        highest_sensor = sensor
    if value < lowest_value:
        lowest_value = value
        lowest_sensor = sensor

print(f"Highest: {highest_sensor} ({highest_value})")
print(f"Lowest: {lowest_sensor} ({lowest_value})")

print("Above 24°C:")
for sensor, value in sensor_readings.items():
    if value > 24:
        print(f"  {sensor}: {value}")
```

</details>

---

## Task 2: Laboratory Inventory

Start with an empty inventory dictionary. Keys are chemical names; values are quantities (strings are fine, e.g. `"500ml"`).

Rules:

1. Add hydrochloric acid (`500ml`), sodium chloride (`250g`), ethanol (`100ml`), and potassium hydroxide (`50g`).
2. Print the full inventory, then only keys, then only values.
3. Check whether `hydrochloric acid` and `sulfuric acid` are in the inventory.
4. Update hydrochloric acid to `750ml` and remove sodium chloride.
5. Print how many different chemicals are stored.

<details>
<summary>Solution (Task 2)</summary>

```python
inventory = {}

inventory["hydrochloric acid"] = "500ml"
inventory["sodium chloride"] = "250g"
inventory["ethanol"] = "100ml"
inventory["potassium hydroxide"] = "50g"

print(inventory)
print(list(inventory.keys()))
print(list(inventory.values()))

print("HCl in inventory:", "hydrochloric acid" in inventory)
print("H2SO4 in inventory:", "sulfuric acid" in inventory)

inventory["hydrochloric acid"] = "750ml"
del inventory["sodium chloride"]

print("Chemical count:", len(inventory))
```

</details>

---

## Task 3: Measurement Frequency Counter

Given repeated experimental measurements:

```python
measurements = [23.5, 24.1, 23.5, 25.2, 24.1, 23.5, 24.8, 25.2, 24.1]
```

Rules:

1. Build a dictionary that maps each value to how often it appears.
2. Print each value and its count.
3. Find the most common and least common measurement.
4. Print values that appear more than once.

<details>
<summary>Solution (Task 3)</summary>

```python
measurements = [23.5, 24.1, 23.5, 25.2, 24.1, 23.5, 24.8, 25.2, 24.1]

counts = {}
for value in measurements:
    if value in counts:
        counts[value] += 1
    else:
        counts[value] = 1

for value, count in counts.items():
    print(f"{value}: {count}")

most_common = None
most_count = 0
least_common = None
least_count = 999

for value, count in counts.items():
    if count > most_count:
        most_count = count
        most_common = value
    if count < least_count:
        least_count = count
        least_common = value

print(f"Most common: {most_common} ({most_count} times)")
print(f"Least common: {least_common} ({least_count} times)")

print("More than once:")
for value, count in counts.items():
    if count > 1:
        print(f"  {value}")
```

</details>

---

## Task 4 (Optional): Equipment Database

Work with nested dictionaries—each equipment ID maps to a small record:

```python
equipment = {
    "Microscope_001": {"type": "Optical", "location": "Lab_A", "status": "Active"},
    "Centrifuge_002": {"type": "Centrifuge", "location": "Lab_B", "status": "Maintenance"},
    "Spectrometer_003": {"type": "Analytical", "location": "Lab_A", "status": "Active"},
}
```

Rules:

1. Print every equipment name and `Microscope_001`'s location.
2. Add `Balance_004` in `Lab_C` with status `Active`.
3. Update `Spectrometer_003` status to `Calibration` and remove `Centrifuge_002`.
4. Print all equipment located in `Lab_A`.

<details>
<summary>Solution (Task 4 Optional)</summary>

```python
equipment = {
    "Microscope_001": {"type": "Optical", "location": "Lab_A", "status": "Active"},
    "Centrifuge_002": {"type": "Centrifuge", "location": "Lab_B", "status": "Maintenance"},
    "Spectrometer_003": {"type": "Analytical", "location": "Lab_A", "status": "Active"},
}

print(list(equipment.keys()))
print("Microscope location:", equipment["Microscope_001"]["location"])

equipment["Balance_004"] = {
    "type": "Weighing",
    "location": "Lab_C",
    "status": "Active",
}
equipment["Spectrometer_003"]["status"] = "Calibration"
del equipment["Centrifuge_002"]

print("Equipment in Lab_A:")
for name, record in equipment.items():
    if record["location"] == "Lab_A":
        print(f"  {name}: {record['type']}, {record['status']}")
```

</details>

---

## Reflection

- When is a dictionary a better choice than a list of tuples for sensor data?
- Which operation—lookup, update, or delete—did you use most often?
- How would you use `.get()` if a sensor ID might not exist in your data?
