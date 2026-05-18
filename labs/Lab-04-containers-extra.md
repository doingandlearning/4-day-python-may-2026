# Lab 4 Extra: Lists and Tuples

This lab focuses on practising list and tuple operations with loops and conditionals—no functions required.

You will practise:

- indexing and slicing containers
- iterating over lists and tuples
- updating lists with `append` and `remove`
- filtering data with `if` and `in`

---

## Hints and Tips

- Use a `for` loop to walk through a list or tuple.
- Access tuple fields by index: `name = pair[0]`, `grade = pair[1]`.
- Use `append()` to add at the end; use slicing like `items[:3]` for the first three items.
- Use `in` to test membership: `"bread" in shopping_list`.
- Use `len()` when you need a count; use `sum()` on a list of numbers when appropriate.

---

## Task 1: Student Grade Tracker

Work with a list of `(student_name, grade)` tuples:

```python
grades = [
    ("Alice", 85), ("Bob", 92), ("Charlie", 78),
    ("Diana", 96), ("Eve", 88), ("Frank", 73),
]
```

Rules:

1. Print every student name.
2. Print every grade.
3. Find and print the highest and lowest grade.
4. Calculate and print the average grade.
5. Print the names of students with a grade above 85.

<details>
<summary>Solution (Task 1)</summary>

```python
grades = [
    ("Alice", 85), ("Bob", 92), ("Charlie", 78),
    ("Diana", 96), ("Eve", 88), ("Frank", 73),
]

print("Names:")
for name, grade in grades:
    print(name)

print("\nGrades:")
for name, grade in grades:
    print(grade)

highest = grades[0][1]
lowest = grades[0][1]
for name, grade in grades:
    if grade > highest:
        highest = grade
    if grade < lowest:
        lowest = grade
print(f"\nHighest: {highest}")
print(f"Lowest: {lowest}")

total = 0
for name, grade in grades:
    total += grade
average = total / len(grades)
print(f"Average: {average:.1f}")

print("\nAbove 85:")
for name, grade in grades:
    if grade > 85:
        print(name)
```

</details>

---

## Task 2: Shopping List Manager

Start with this list:

```python
shopping_list = ["apples", "bananas", "milk", "bread", "eggs"]
```

Rules:

1. Print the full list.
2. Add `"cheese"` at the end and `"butter"` at index 2.
3. Remove `"milk"`.
4. Print the first 3 items and the last 2 items.
5. Check whether `"bread"` is in the list and print the result.
6. Print the length of the list.

<details>
<summary>Solution (Task 2)</summary>

```python
shopping_list = ["apples", "bananas", "milk", "bread", "eggs"]

print(shopping_list)

shopping_list.append("cheese")
shopping_list.insert(2, "butter")
shopping_list.remove("milk")

print("First 3:", shopping_list[:3])
print("Last 2:", shopping_list[-2:])
print("bread in list:", "bread" in shopping_list)
print("Length:", len(shopping_list))
```

</details>

---

## Task 3: Number Analysis

Work with this list:

```python
numbers = [15, 23, 8, 42, 17, 31, 6, 55, 29, 12]
```

Rules:

1. Count how many numbers are even and how many are odd.
2. Find and print the largest and smallest values.
3. Print all numbers greater than 20.
4. Print all numbers between 10 and 30 (inclusive).
5. Print the sum of all numbers.

<details>
<summary>Solution (Task 3)</summary>

```python
numbers = [15, 23, 8, 42, 17, 31, 6, 55, 29, 12]

even_count = 0
odd_count = 0
for n in numbers:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Even: {even_count}, Odd: {odd_count}")

largest = numbers[0]
smallest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n
print(f"Largest: {largest}, Smallest: {smallest}")

print("Greater than 20:")
for n in numbers:
    if n > 20:
        print(n)

print("Between 10 and 30:")
for n in numbers:
    if 10 <= n <= 30:
        print(n)

total = 0
for n in numbers:
    total += n
print(f"Sum: {total}")
```

</details>

---

## Task 4 (Optional): Daily Temperature Readings

Work with `(day, temperature)` tuples:

```python
temperatures = [
    ("Monday", 22), ("Tuesday", 25), ("Wednesday", 23),
    ("Thursday", 27), ("Friday", 24), ("Saturday", 26), ("Sunday", 21),
]
```

Rules:

1. Find and print the hottest and coldest day (by temperature).
2. Print days with temperature above 24.
3. Calculate and print the average temperature.

<details>
<summary>Solution (Task 4 Optional)</summary>

```python
temperatures = [
    ("Monday", 22), ("Tuesday", 25), ("Wednesday", 23),
    ("Thursday", 27), ("Friday", 24), ("Saturday", 26), ("Sunday", 21),
]

hottest_day = temperatures[0][0]
hottest_temp = temperatures[0][1]
coldest_day = temperatures[0][0]
coldest_temp = temperatures[0][1]

for day, temp in temperatures:
    if temp > hottest_temp:
        hottest_temp = temp
        hottest_day = day
    if temp < coldest_temp:
        coldest_temp = temp
        coldest_day = day

print(f"Hottest: {hottest_day} ({hottest_temp}°C)")
print(f"Coldest: {coldest_day} ({coldest_temp}°C)")

print("Above 24°C:")
for day, temp in temperatures:
    if temp > 24:
        print(f"  {day}: {temp}")

total = 0
for day, temp in temperatures:
    total += temp
average = total / len(temperatures)
print(f"Average: {average:.1f}°C")
```

</details>

---

## Reflection

- When did indexing (`pair[0]`) feel clearer than unpacking in a loop?
- Which task was easier with slicing instead of a loop?
- Where would a list of tuples be a good fit for sensor or experiment data?
