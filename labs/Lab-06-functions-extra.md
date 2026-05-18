# Lab 6 Extra: Functions for Scientific Calculations

This lab focuses on defining reusable functions with parameters and return values for engineering and science workflows.

You will practise:

- writing functions that return computed values
- passing parameters to make functions flexible
- combining small functions into a short pipeline
- keeping `print` in the main flow, not inside every helper

---

## Hints and Tips

- Prefer `return` for results; call `print` only in your main script or test block.
- Give functions clear names: `celsius_to_fahrenheit`, not `convert1`.
- One function, one job—split conversion, filtering, and reporting.
- Test each function with a few known values before combining them.
- Use `3.14159` or `math.pi` consistently for circle and sphere formulas.

---

## Task 1: Temperature Conversions

Write these functions:

`celsius_to_fahrenheit(celsius)`

`celsius_to_kelvin(celsius)`

Rules:

1. `celsius_to_fahrenheit` returns \(F = (C \times 9/5) + 32\).
2. `celsius_to_kelvin` returns \(K = C + 273.15\).
3. In a short main block, print conversions for `0`, `25`, and `100` Celsius.

<details>
<summary>Solution (Task 1)</summary>

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def celsius_to_kelvin(celsius):
    return celsius + 273.15


for c in [0, 25, 100]:
    f = celsius_to_fahrenheit(c)
    k = celsius_to_kelvin(c)
    print(f"{c}°C -> {f:.1f}°F, {k:.1f} K")
```

</details>

---

## Task 2: Data Analysis Helpers

Write these functions:

`calculate_average(numbers)`

`find_maximum(numbers)`

`find_minimum(numbers)`

`count_above_threshold(numbers, threshold)`

Rules:

1. Each function takes a list of numbers and returns one result (no printing inside the functions).
2. `count_above_threshold` returns how many values are strictly greater than `threshold`.
3. Test with: `[23.5, 24.1, 22.8, 25.2, 23.9, 24.7, 22.1, 25.8]` and threshold `24.0`.

<details>
<summary>Solution (Task 2)</summary>

```python
def calculate_average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


def find_maximum(numbers):
    maximum = numbers[0]
    for n in numbers:
        if n > maximum:
            maximum = n
    return maximum


def find_minimum(numbers):
    minimum = numbers[0]
    for n in numbers:
        if n < minimum:
            minimum = n
    return minimum


def count_above_threshold(numbers, threshold):
    count = 0
    for n in numbers:
        if n > threshold:
            count += 1
    return count


data = [23.5, 24.1, 22.8, 25.2, 23.9, 24.7, 22.1, 25.8]
print("Average:", calculate_average(data))
print("Max:", find_maximum(data))
print("Min:", find_minimum(data))
print("Above 24.0:", count_above_threshold(data, 24.0))
```

</details>

---

## Task 3: Unit Conversions

Write these functions:

`meters_to_feet(meters)`

`kilograms_to_pounds(kg)`

Rules:

1. Use `1 meter = 3.28084 feet` and `1 kilogram = 2.20462 pounds`.
2. Return the converted value from each function.
3. Print sample conversions for `10` meters and `5` kilograms.

<details>
<summary>Solution (Task 3)</summary>

```python
def meters_to_feet(meters):
    return meters * 3.28084


def kilograms_to_pounds(kg):
    return kg * 2.20462


print(f"10 m = {meters_to_feet(10):.2f} ft")
print(f"5 kg = {kilograms_to_pounds(5):.2f} lb")
```

</details>

---

## Task 4 (Optional): Sensor Processing Pipeline

Build a small pipeline with these functions:

`filter_valid_readings(readings, min_val, max_val)`

`calculate_statistics(readings)`

`detect_anomalies(readings, threshold)`

Rules:

1. `filter_valid_readings` returns only values between `min_val` and `max_val` (inclusive).
2. `calculate_statistics` returns the mean of the list (assume it is not empty).
3. `detect_anomalies` returns a list of readings more than `threshold` away from the mean.
4. Use this sample data in main: `[22.1, 23.5, 45.0, 24.1, 23.8, 22.9]` with range `20`–`30` and threshold `2.0`.

<details>
<summary>Solution (Task 4 Optional)</summary>

```python
def filter_valid_readings(readings, min_val, max_val):
    valid = []
    for value in readings:
        if min_val <= value <= max_val:
            valid.append(value)
    return valid


def calculate_statistics(readings):
    total = 0
    for value in readings:
        total += value
    return total / len(readings)


def detect_anomalies(readings, threshold):
    mean = calculate_statistics(readings)
    anomalies = []
    for value in readings:
        if abs(value - mean) > threshold:
            anomalies.append(value)
    return anomalies


readings = [22.1, 23.5, 45.0, 24.1, 23.8, 22.9]
valid = filter_valid_readings(readings, 20, 30)
mean = calculate_statistics(valid)
anomalies = detect_anomalies(valid, 2.0)

print("Valid readings:", valid)
print("Mean:", f"{mean:.2f}")
print("Anomalies:", anomalies)
```

</details>

---

## Reflection

- Which function is easiest to reuse in another file?
- Where did parameters make your code cleaner than hard-coded values?
- Which task used return values most effectively compared to printing inside functions?
