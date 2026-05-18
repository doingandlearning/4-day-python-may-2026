# Lab 8: Classes for Sensor Readings

This lab focuses on modelling environmental sensor data with a Python class.

You will practise:

- defining a class with `__init__` and instance attributes
- overriding `__str__` for readable output
- writing methods that use `self`
- working with a list of class instances

---

## Hints and Tips

- The first parameter of instance methods is always `self`.
- `__str__` should return a string; use `print(reading)` to display it.
- Methods like `adjust_reading` change `self.value` in place.
- Assigning `r2 = r1` makes two names point at the same object—changing one affects the other.
- Use a list of objects when you have many readings to filter or adjust.

---

## Task 1: Define SensorReading

Write a class:

`SensorReading`

Rules:

1. `__init__(self, sensor_id, timestamp, value, units)` stores all four attributes.
2. Create one reading: `TEMP_001`, `"2025-03-11 14:30:00"`, `22.5`, `"°C"`.
3. Print `reading.value` and `reading.units`.

<details>
<summary>Solution (Task 1)</summary>

```python
class SensorReading:
    def __init__(self, sensor_id, timestamp, value, units):
        self.sensor_id = sensor_id
        self.timestamp = timestamp
        self.value = value
        self.units = units


reading = SensorReading("TEMP_001", "2025-03-11 14:30:00", 22.5, "°C")
print(reading.value, reading.units)
```

</details>

---

## Task 2: Display and Threshold Check

Extend `SensorReading` with:

`__str__(self)`

`is_above_threshold(self, threshold)`

Rules:

1. `__str__` returns: `Sensor TEMP_001 at 2025-03-11 14:30:00: 22.5 °C` (use the instance’s fields).
2. `is_above_threshold` returns `True` when `value > threshold`, otherwise `False`.
3. Test with a CO₂ reading at `450.0` ppm and threshold `400`.

<details>
<summary>Solution (Task 2)</summary>

```python
class SensorReading:
    def __init__(self, sensor_id, timestamp, value, units):
        self.sensor_id = sensor_id
        self.timestamp = timestamp
        self.value = value
        self.units = units

    def __str__(self):
        return (
            f"Sensor {self.sensor_id} at {self.timestamp}: "
            f"{self.value} {self.units}"
        )

    def is_above_threshold(self, threshold):
        return self.value > threshold


r1 = SensorReading("TEMP_001", "2025-03-11 14:30:00", 22.5, "°C")
r2 = SensorReading("CO2_002", "2025-03-11 14:31:00", 450.0, "ppm")

print(r1)
print(r2.is_above_threshold(400))
```

</details>

---

## Task 3: Adjust Readings and Assignment

Add:

`adjust_reading(self, correction)`

Rules:

1. Add `correction` to `value` (use a negative correction to subtract).
2. Call `adjust_reading(-2.5)` on a 22.5°C reading and print the object.
3. Demonstrate assignment: create `r1`, set `r2 = r1`, change `r2.value`, print both—explain why they match.

<details>
<summary>Solution (Task 3)</summary>

```python
class SensorReading:
    def __init__(self, sensor_id, timestamp, value, units):
        self.sensor_id = sensor_id
        self.timestamp = timestamp
        self.value = value
        self.units = units

    def __str__(self):
        return (
            f"Sensor {self.sensor_id} at {self.timestamp}: "
            f"{self.value} {self.units}"
        )

    def adjust_reading(self, correction):
        self.value += correction


r1 = SensorReading("TEMP_001", "2025-03-11 14:30:00", 22.5, "°C")
r1.adjust_reading(-2.5)
print(r1)

r1 = SensorReading("TEMP_001", "2025-03-11 14:30:00", 22.5, "°C")
r2 = r1
r2.value = 25.0
print("r1:", r1)
print("r2:", r2)
```

</details>

---

## Task 4: Process Multiple Readings

Create a list of at least three `SensorReading` objects (mix of temperature and other units).

Rules:

1. Print every reading in a loop.
2. Print only readings above a threshold you choose.
3. Adjust every reading by the same correction (e.g. `-0.5`) and print the updated list.

<details>
<summary>Solution (Task 4)</summary>

```python
class SensorReading:
    def __init__(self, sensor_id, timestamp, value, units):
        self.sensor_id = sensor_id
        self.timestamp = timestamp
        self.value = value
        self.units = units

    def __str__(self):
        return (
            f"Sensor {self.sensor_id} at {self.timestamp}: "
            f"{self.value} {self.units}"
        )

    def is_above_threshold(self, threshold):
        return self.value > threshold

    def adjust_reading(self, correction):
        self.value += correction


readings = [
    SensorReading("TEMP_001", "2025-03-11 14:30:00", 22.5, "°C"),
    SensorReading("TEMP_002", "2025-03-11 14:31:00", 18.0, "°C"),
    SensorReading("CO2_001", "2025-03-11 14:32:00", 420.0, "ppm"),
]

print("All readings:")
for reading in readings:
    print(reading)

print("\nAbove 20:")
for reading in readings:
    if reading.is_above_threshold(20):
        print(reading)

for reading in readings:
    reading.adjust_reading(-0.5)

print("\nAfter calibration:")
for reading in readings:
    print(reading)
```

</details>

---

## Reflection

- What is the difference between a class and a single dictionary for one reading?
- Why does changing `r2.value` also change `r1` when `r2 = r1`?
- Which method would you add next if you needed to convert units inside the class?
