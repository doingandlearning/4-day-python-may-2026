# Lab 7: Transforming Lists with map, filter, and Comprehensions

This lab focuses on converting and filtering temperature and number lists. You can use `map()` and `filter()`, or list comprehensions—comprehensions are often the more readable choice for these patterns.

You will practise:

- converting every item in a list (map or comprehension)
- keeping items that match a condition (filter or comprehension)
- combining filter and convert in one or two steps
- choosing between a named function, a lambda, and a comprehension

---

## Hints and Tips

- Celsius to Fahrenheit: `F = (C * 9/5) + 32`.
- Convert all values: `[celsius_to_fahrenheit(c) for c in temperatures]`.
- Keep some values: `[c for c in temperatures if c >= 18]`.
- Filter and convert together: `[celsius_to_fahrenheit(c) for c in temperatures if c > 14]`.
- `map()` and `filter()` return iterators—use `list(...)` if you need a full list to print.
- A number is even when `n % 2 == 0`.

---

## Task 1: Convert Temperatures

Use:

```python
temperatures = [12.5, 18.1, 15.6, 17.8, 20.1, 22.6, 18.9]
```

Write:

`celsius_to_fahrenheit(celsius)`

Rules:

1. Implement conversion in a named function that returns the value.
2. Build the Fahrenheit list with a **list comprehension** and print it.
3. Also try `map()` with your named function (or a lambda) and print that list—they should match.

Example output:

```text
[54.5, 64.58, 60.08, 64.04, 68.18, 72.68, 66.02]
```

<details>
<summary>Solution (Task 1)</summary>

```python
temperatures = [12.5, 18.1, 15.6, 17.8, 20.1, 22.6, 18.9]


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


fahrenheit_comp = [celsius_to_fahrenheit(c) for c in temperatures]
fahrenheit_map = list(map(celsius_to_fahrenheit, temperatures))

print(fahrenheit_comp)
print(fahrenheit_map)
```

</details>

---

## Task 2: Filter Warm Temperatures

Using the same `temperatures` list, keep only values **18°C or above**.

Rules:

1. Build the result with a list comprehension and print it.
2. Repeat with `filter()` (lambda or named function is fine) and print—the lists should match.

Expected:

```text
[18.1, 20.1, 22.6, 18.9]
```

<details>
<summary>Solution (Task 2)</summary>

```python
temperatures = [12.5, 18.1, 15.6, 17.8, 20.1, 22.6, 18.9]

warm_comp = [c for c in temperatures if c >= 18]
warm_filter = list(filter(lambda c: c >= 18, temperatures))

print(warm_comp)
print(warm_filter)
```

</details>

---

## Task 3: Filter Then Convert

From `temperatures`, keep values **above 14°C** and convert them to Fahrenheit.

Rules:

1. Prefer a **single comprehension** that filters and converts in one expression.
2. Optionally show the two-step version (filter, then map or second comprehension) for comparison.
3. Print the final list.

Expected:

```text
[60.08, 64.04, 68.18, 72.68, 66.02]
```

<details>
<summary>Solution (Task 3)</summary>

```python
temperatures = [12.5, 18.1, 15.6, 17.8, 20.1, 22.6, 18.9]


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# One readable comprehension
fahrenheit = [
    celsius_to_fahrenheit(c)
    for c in temperatures
    if c > 14
]
print(fahrenheit)

# Two-step alternative (equivalent)
warm_enough = [c for c in temperatures if c > 14]
fahrenheit_two_step = [celsius_to_fahrenheit(c) for c in warm_enough]
print(fahrenheit_two_step)
```

</details>

---

## Task 4: Filter Even Numbers

Use:

```python
data = [1, 3, 5, 2, 7, 4, 10]
```

Write:

`is_even(n)`

Rules:

1. Implement `is_even` as a named function returning `True` or `False`.
2. Build the even list with a comprehension: `[n for n in data if ...]`.
3. Build the same list with `filter(is_even, data)` and confirm they match.

Expected:

```text
[2, 4, 10]
```

<details>
<summary>Solution (Task 4)</summary>

```python
data = [1, 3, 5, 2, 7, 4, 10]


def is_even(n):
    return n % 2 == 0


evens_comp = [n for n in data if is_even(n)]
evens_filter = list(filter(is_even, data))

print(evens_comp)
print(evens_filter)
```

</details>

---

## Reflection

- Which version of Task 3 did you find easiest to read—the one-step comprehension or the two-step version?
- When might you still reach for `map()` or `filter()` instead of a comprehension?
- Which step would you change first if the threshold temperature changed?
