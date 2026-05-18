# Lab 11: Testing with pytest

This lab focuses on writing unit tests for a small weather data module using `pytest`.

You will practise:

- writing function-based tests with `pytest`
- testing normal results and error cases
- using `@pytest.mark.parametrize` for multiple inputs
- skipping tests for features not yet implemented

---

## Hints and Tips

- Name test files `test_<module>.py` and test functions `test_<behaviour>`.
- Use `assert` for expectations: `assert celsius_to_fahrenheit(0) == 32`.
- Test exceptions with `pytest.raises(ValueError)`.
- Parametrize when the same logic applies to many input/output pairs.
- Run tests from the lab folder: `pytest test_weather.py -v`.

---

## Task 1: Create the Module Under Test

Create `weather.py` with:

`celsius_to_fahrenheit(celsius)`

`average_temperature(temperatures)`

`detect_anomalies(temperatures, threshold)`

Rules:

1. Fahrenheit conversion uses `(celsius * 9/5) + 32`.
2. `average_temperature` raises `ValueError` if the list is empty.
3. `detect_anomalies` returns temperatures where `abs(temp) > threshold`.

<details>
<summary>Solution (Task 1)</summary>

```python
"""Weather data processing module."""


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def average_temperature(temperatures):
    if not temperatures:
        raise ValueError("Temperature list cannot be empty")
    return sum(temperatures) / len(temperatures)


def detect_anomalies(temperatures, threshold):
    return [temp for temp in temperatures if abs(temp) > threshold]
```

</details>

---

## Task 2: Basic Tests

Create `test_weather.py` with tests for:

Rules:

1. `test_celsius_to_fahrenheit` — assert `0` → `32` and `100` → `212`.
2. `test_average_temperature` — assert average of `[20, 22, 24]` is `22`.
3. `test_average_temperature_empty_list` — use `pytest.raises(ValueError)`.

<details>
<summary>Solution (Task 2)</summary>

```python
import pytest
from weather import celsius_to_fahrenheit, average_temperature


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212


def test_average_temperature():
    assert average_temperature([20, 22, 24]) == 22


def test_average_temperature_empty_list():
    with pytest.raises(ValueError):
        average_temperature([])
```

</details>

---

## Task 3: Parameterized Conversion Tests

Add a parametrized test for `celsius_to_fahrenheit`.

Rules:

1. Use `@pytest.mark.parametrize` with at least three `(celsius, expected)` pairs.
2. One pair should be negative Celsius.

<details>
<summary>Solution (Task 3)</summary>

```python
import pytest
from weather import celsius_to_fahrenheit


@pytest.mark.parametrize(
    "celsius, expected",
    [
        (0, 32),
        (100, 212),
        (-40, -40),
        (25, 77),
    ],
)
def test_celsius_to_fahrenheit_param(celsius, expected):
    assert celsius_to_fahrenheit(celsius) == expected
```

</details>

---

## Task 4: Anomalies and Skipped Tests

Rules:

1. Add `test_detect_anomalies` — for threshold `20`, `[15, 25, -30, 18]` should return `[25, -30]`.
2. Add `test_future_feature` decorated with `@pytest.mark.skip(reason="Not implemented yet")`.

<details>
<summary>Solution (Task 4)</summary>

```python
import pytest
from weather import detect_anomalies


def test_detect_anomalies():
    result = detect_anomalies([15, 25, -30, 18], 20)
    assert result == [25, -30]


@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    assert False
```

</details>

---

## Reflection

- Why test the empty-list case separately from the happy path?
- What is the advantage of parametrized tests over many nearly identical functions?
- When would you skip a test instead of deleting it?
