# Lab 10: Python Modules and Imports

This lab focuses on splitting code into a module and a main script, and exploring import styles.

You will practise:

- creating a module with functions and a class
- importing with `import`, `from ... import`, and aliases
- using `if __name__ == "__main__"`
- calling built-in modules (`math`, `random`)

---

## Hints and Tips

- Code in a module runs on `import` unless you guard it with `if __name__ == "__main__"`.
- `from mymodule import greet` lets you call `greet()` without the module prefix.
- `dir(module)` lists names defined in that module.
- Keep reusable logic in the module; keep interactive demos in `main.py`.
- Run `python mymodule.py` to test the module alone; run `python main.py` for the full lab.

---

## Task 1: Create and Import Your Module

Create `mymodule.py`:

```python
"""Sample module for the lab."""


def greet(name):
  return f"Hello, {name}!"


class Scientist:
    def __init__(self, name, field):
        self.name = name
        self.field = field

    def __str__(self):
        return f"{self.name} works in {self.field}."
```

In `main.py`:

Rules:

1. `import mymodule` and print `mymodule.greet("Alice")`.
2. Create `mymodule.Scientist("Alice", "Biology")` and print it.
3. Print `mymodule.__name__` and `mymodule.__doc__`.

<details>
<summary>Solution (Task 1)</summary>

`mymodule.py`:

```python
"""Sample module for the lab."""


def greet(name):
    return f"Hello, {name}!"


class Scientist:
    def __init__(self, name, field):
        self.name = name
        self.field = field

    def __str__(self):
        return f"{self.name} works in {self.field}."
```

`main.py`:

```python
import mymodule

print(mymodule.greet("Alice"))
scientist = mymodule.Scientist("Alice", "Biology")
print(scientist)
print("Module name:", mymodule.__name__)
print("Module doc:", mymodule.__doc__)
```

</details>

---

## Task 2: Import Styles

In `main.py`, add:

Rules:

1. `from mymodule import greet` and print `greet("Bob")`.
2. `from mymodule import Scientist as Sci` and print `Sci("Dr. Eve", "Physics")`.
3. `import mymodule as mod` and print `mod.greet("Charlie")`.
4. Print `dir(mymodule)` (or `dir(mod)`) once.

<details>
<summary>Solution (Task 2)</summary>

```python
import mymodule
from mymodule import greet
from mymodule import Scientist as Sci
import mymodule as mod

print(mymodule.greet("Alice"))
print(Sci("Dr. Eve", "Physics"))
print(greet("Bob"))
print(mod.greet("Charlie"))
print(dir(mymodule))
```

</details>

---

## Task 3: Built-in Modules

In `main.py`:

Rules:

1. Import `math` and print the square root of `25`.
2. Import `random` and print one random integer from 1 to 100 inclusive.

<details>
<summary>Solution (Task 3)</summary>

```python
import math
import random

print("Square root of 25:", math.sqrt(25))
print("Random 1-100:", random.randint(1, 100))
```

</details>

---

## Task 4: The __main__ Guard

Update `mymodule.py`:

Rules:

1. Add a `main()` function that prints `This runs only when mymodule.py is executed directly.`
2. Add:

```python
if __name__ == "__main__":
    main()
```

3. Confirm: `python mymodule.py` prints the message; `python main.py` does not.

<details>
<summary>Solution (Task 4)</summary>

`mymodule.py`:

```python
"""Sample module for the lab."""


def greet(name):
    return f"Hello, {name}!"


class Scientist:
    def __init__(self, name, field):
        self.name = name
        self.field = field

    def __str__(self):
        return f"{self.name} works in {self.field}."


def main():
    print("This runs only when mymodule.py is executed directly.")


if __name__ == "__main__":
    main()
```

</details>

---

## Reflection

- What is the difference between running a file and importing it?
- When would you use `from module import name` instead of `import module`?
- Where should interactive `input()` and `print()` live—in the module or in `main.py`?
