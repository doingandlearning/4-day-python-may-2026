# Lab 9: Error Handling in Data Processing

This lab focuses on making a measurement-processing function robust with `try`, `except`, `else`, `finally`, and a custom exception.

You will practise:

- catching specific exceptions without crashing
- skipping bad rows while processing valid data
- using `else` and `finally` for success and cleanup paths
- defining and raising a custom exception

---

## Hints and Tips

- Catch specific errors (`TypeError`, `ZeroDivisionError`) rather than a bare `except`.
- Validate data with `if` when you can (e.g. reject negative values before adding).
- Use `continue` inside a loop to skip one bad measurement and keep going.
- `finally` runs whether or not an error occurred—good for a “done” message.
- Return a summary string from the function; print it in main.

---

## Task 1: Catch Invalid Values

Start with this faulty function:

```python
def process_measurements(measurements):
    total = 0
    count = 0
    for experiment_id, value in measurements:
        total += value
        count += 1
    average = total / count
    return f"Processed {count} measurements. Average: {average:.2f}"
```

Rules:

1. Wrap the addition in `try` / `except TypeError`.
2. On `TypeError`, print which experiment had invalid data and continue the loop.
3. Only count and sum numeric values.

Test with:

```python
data_samples = [
    ("EXP001", 23.4),
    ("EXP002", "invalid"),
    ("EXP003", 18.7),
]
```

<details>
<summary>Solution (Task 1)</summary>

```python
def process_measurements(measurements):
    total = 0
    count = 0
    for experiment_id, value in measurements:
        try:
            total += value
            count += 1
        except TypeError:
            print(f"Error: Invalid value '{value}' in experiment {experiment_id}.")
    if count == 0:
        return "No valid measurements."
    average = total / count
    return f"Processed {count} measurements. Average: {average:.2f}"


data_samples = [
    ("EXP001", 23.4),
    ("EXP002", "invalid"),
    ("EXP003", 18.7),
]
print(process_measurements(data_samples))
```

</details>

---

## Task 2: Handle Empty Data and Use else / finally

Rules:

1. Catch `ZeroDivisionError` when there are no valid measurements.
2. Use `else` on the outer flow to print a success note only when at least one reading was processed.
3. Use `finally` to print `Processing complete.` every time the function runs.

<details>
<summary>Solution (Task 2)</summary>

```python
def process_measurements(measurements):
    total = 0
    count = 0
    try:
        for experiment_id, value in measurements:
            try:
                total += value
                count += 1
            except TypeError:
                print(
                    f"Error: Invalid value '{value}' in experiment {experiment_id}."
                )
        average = total / count
        result = f"Processed {count} measurements. Average: {average:.2f}"
    except ZeroDivisionError:
        result = "No valid measurements to average."
    else:
        if count > 0:
            print("All valid rows processed successfully.")
    finally:
        print("Processing complete.")
    return result


print(process_measurements([]))
print(process_measurements([("EXP001", 23.4), ("EXP002", "bad"), ("EXP003", 18.7)]))
```

</details>

---

## Task 3: Custom Exception for Negative Values

Define:

`InvalidMeasurementError`

Rules:

1. Subclass `Exception` (empty body is fine).
2. Before adding a value, if it is negative, raise `InvalidMeasurementError` with a clear message.
3. Catch it in the loop, print the error, and continue.
4. Test with a negative value in the sample list.

Example output pattern:

```text
Error: Invalid value 'invalid' in experiment EXP002.
Error: Negative measurement -5.0 in experiment EXP003.
Processed 2 valid measurements. Average: 21.05
Processing complete.
```

<details>
<summary>Solution (Task 3)</summary>

```python
class InvalidMeasurementError(Exception):
    pass


def process_measurements(measurements):
    total = 0
    count = 0
    try:
        for experiment_id, value in measurements:
            try:
                if isinstance(value, (int, float)) and value < 0:
                    raise InvalidMeasurementError(
                        f"Negative measurement {value} in experiment {experiment_id}."
                    )
                total += value
                count += 1
            except TypeError:
                print(
                    f"Error: Invalid value '{value}' in experiment {experiment_id}."
                )
            except InvalidMeasurementError as err:
                print(f"Error: {err}")
        average = total / count
        result = f"Processed {count} valid measurements. Average: {average:.2f}"
    except ZeroDivisionError:
        result = "No valid measurements to average."
    finally:
        print("Processing complete.")
    return result


data_samples = [
    ("EXP001", 23.4),
    ("EXP002", "invalid"),
    ("EXP003", -5.0),
    ("EXP004", 18.7),
]
print(process_measurements(data_samples))
```

</details>

---

## Task 4 (Optional): Validate Before try

Rewrite the inner loop so negative values are rejected with an `if` check **before** `raise InvalidMeasurementError`, and non-numeric values are rejected with `if not isinstance(value, (int, float))` before addition.

Rules:

1. Keep the same behaviour as Task 3.
2. Prefer explicit checks over relying only on `TypeError` from `+=`.

<details>
<summary>Solution (Task 4 Optional)</summary>

```python
class InvalidMeasurementError(Exception):
    pass


def process_measurements(measurements):
    total = 0
    count = 0
    for experiment_id, value in measurements:
        if not isinstance(value, (int, float)):
            print(f"Error: Invalid value '{value}' in experiment {experiment_id}.")
            continue
        if value < 0:
            print(f"Error: Negative measurement {value} in experiment {experiment_id}.")
            continue
        total += value
        count += 1

    if count == 0:
        print("Processing complete.")
        return "No valid measurements to average."

    average = total / count
    print("Processing complete.")
    return f"Processed {count} valid measurements. Average: {average:.2f}"


data_samples = [
    ("EXP001", 23.4),
    ("EXP002", "invalid"),
    ("EXP003", -5.0),
    ("EXP004", 18.7),
]
print(process_measurements(data_samples))
```

</details>

---

## Reflection

- When is an `if` check clearer than waiting for a `TypeError`?
- Why process valid rows instead of stopping at the first bad value?
- What other measurement rule might deserve its own custom exception?
