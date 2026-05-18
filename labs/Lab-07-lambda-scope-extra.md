# Lab 7 Extra: Lambda Functions, Comprehensions, and Scope

This lab focuses on sorting with `lambda`, filtering and transforming data with list comprehensions (often clearer than `filter`/`map`), and understanding local versus global variables.

You will practise:

- sorting with a custom `key` using `lambda`
- filtering and extracting fields with list comprehensions
- comparing comprehensions with `filter()` and `map()` when useful
- reading global variables inside functions
- using the `global` keyword when a function must update a counter

---

## Hints and Tips

- `sorted(data, key=lambda x: x[1])` sorts by the second field of each tuple—comprehensions do not replace this pattern.
- Extract readings from OK sensors: `[row[1] for row in sensor_data if row[2] == "OK"]`.
- Lambdas work best for short `key=` functions; use a named function if the logic grows.
- You can read globals inside a function without `global`; you need `global` only to assign to them.
- Local variables inside a function are not visible outside it.

---

## Task 1: Sorting Experiment Data

Use this data: `(experiment_id, temperature, pressure, result)`.

```python
experiments = [
    ("EXP_001", 25.3, 101.2, 0.85),
    ("EXP_002", 30.1, 98.7, 0.92),
    ("EXP_003", 22.8, 103.1, 0.78),
    ("EXP_004", 28.5, 99.8, 0.88),
    ("EXP_005", 26.7, 102.3, 0.91),
]
```

Rules:

1. Sort by temperature ascending and print the list.
2. Sort by result descending and print the list.
3. Sort by experiment ID alphabetically and print the list.
4. Use `key=lambda ...` in each `sorted()` call (or a named function if you prefer).

<details>
<summary>Solution (Task 1)</summary>

```python
experiments = [
    ("EXP_001", 25.3, 101.2, 0.85),
    ("EXP_002", 30.1, 98.7, 0.92),
    ("EXP_003", 22.8, 103.1, 0.78),
    ("EXP_004", 28.5, 99.8, 0.88),
    ("EXP_005", 26.7, 102.3, 0.91),
]

by_temp = sorted(experiments, key=lambda row: row[1])
print("By temperature:", by_temp)

by_result = sorted(experiments, key=lambda row: row[3], reverse=True)
print("By result:", by_result)

by_id = sorted(experiments, key=lambda row: row[0])
print("By ID:", by_id)
```

</details>

---

## Task 2: Scope with Physical Constants

Use global constants:

```python
PI = 3.14159
GRAVITY = 9.81
```

Write:

`calculate_circle_area(radius)`

`calculate_pendulum_period(length)`

Rules:

1. `calculate_circle_area` uses `PI` and returns \(\pi r^2\).
2. `calculate_pendulum_period` uses `GRAVITY` for \(T = 2\pi\sqrt{L/g}\) and returns the period.
3. Print results for radius `5` and length `1.0`.

<details>
<summary>Solution (Task 2)</summary>

```python
PI = 3.14159
GRAVITY = 9.81


def calculate_circle_area(radius):
    return PI * radius * radius


def calculate_pendulum_period(length):
    return 2 * PI * (length / GRAVITY) ** 0.5


print("Area:", calculate_circle_area(5))
print("Period:", calculate_pendulum_period(1.0))
```

</details>

---

## Task 3: Extract Readings from OK Sensors

```python
sensor_data = [
    ("SENSOR_A", 23.5, "OK"),
    ("SENSOR_B", 25.1, "WARNING"),
    ("SENSOR_C", 22.8, "OK"),
    ("SENSOR_D", 26.3, "ERROR"),
    ("SENSOR_E", 24.7, "OK"),
]
```

Each tuple is `(sensor_id, reading, status)`.

Rules:

1. Build a list of reading values for sensors with status `"OK"` using a **list comprehension**.
2. Print that list.
3. Optionally reproduce the same result with `filter()` and `map()` to compare readability.

<details>
<summary>Solution (Task 3)</summary>

```python
sensor_data = [
    ("SENSOR_A", 23.5, "OK"),
    ("SENSOR_B", 25.1, "WARNING"),
    ("SENSOR_C", 22.8, "OK"),
    ("SENSOR_D", 26.3, "ERROR"),
    ("SENSOR_E", 24.7, "OK"),
]

ok_readings = [row[1] for row in sensor_data if row[2] == "OK"]
print(ok_readings)

# Equivalent with filter/map
ok_rows = list(filter(lambda row: row[2] == "OK", sensor_data))
ok_readings_map = list(map(lambda row: row[1], ok_rows))
print(ok_readings_map)
```

</details>

---

## Task 4 (Optional): Experiment Counter and Material Sort

Part A — global counter:

```python
experiment_count = 0
```

Write `run_experiment()` that increments `experiment_count` and returns the new count. Call it three times and print the count each time.

Part B — sort materials by strength-to-weight ratio:

```python
materials = [
    ("Steel", 7850, 400),
    ("Aluminum", 2700, 200),
    ("Titanium", 4500, 900),
]
```

Each tuple is `(name, density, strength)`. Sort by `strength / density` descending with `sorted(..., key=lambda ...)`.

Part C — list only material names with strength above 300:

Rules:

1. Use a comprehension: `[name for name, density, strength in materials if strength > 300]`.

<details>
<summary>Solution (Task 4 Optional)</summary>

```python
experiment_count = 0


def run_experiment():
    global experiment_count
    experiment_count += 1
    return experiment_count


for _ in range(3):
    print("Experiment #", run_experiment())

materials = [
    ("Steel", 7850, 400),
    ("Aluminum", 2700, 200),
    ("Titanium", 4500, 900),
]

ranked = sorted(materials, key=lambda m: m[2] / m[1], reverse=True)
print("By strength/weight:", ranked)

strong_names = [name for name, density, strength in materials if strength > 300]
print("Strength > 300:", strong_names)
```

</details>

---

## Reflection

- When did a lambda in `sorted(..., key=...)` feel clearer than a separate function?
- How did the Task 3 comprehension compare to `filter()` plus `map()` for readability?
- What happened when you tried to change a global variable without the `global` keyword?
