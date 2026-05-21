# Lab 13: Building a Desktop Interface with tkinter

This lab focuses on building a simple desktop application using tkinter's core widgets, layout system, and event handling.

You will practise:

- creating a root window and adding widgets
- laying out widgets with `grid()`
- binding button clicks to functions
- reading and updating widget values with `StringVar`

---

## Hints and Tips

- `ttk` widgets look better than plain `tk` widgets — import from `tkinter import ttk`.
- `grid(row=0, column=0)` places a widget; add `sticky="ew"` to make it stretch horizontally.
- A `StringVar` connects a variable to a widget — changing one updates the other automatically.
- Call `root.mainloop()` once at the end — it keeps the window open and handles events.
- Keep your callback functions short; they should update state or call a helper, not do heavy work.

---

## Task 1: A Window with a Label and a Button

Create `unit_converter.py`.

You will build a simple Celsius to Kelvin converter across the four tasks.

Start with a working window containing a title label and a button.

Rules:

1. Create a root window titled `"Unit Converter"` with a size of `400x200`.
2. Add a `ttk.Label` with the text `"Celsius to Kelvin Converter"`.
3. Add a `ttk.Button` with the text `"Convert"`. For now it does not need to do anything.
4. Use `grid()` to place both widgets. Put the label in row 0 and the button in row 1.
5. Call `root.mainloop()` to display the window.

<details>
<summary>Solution (Task 1)</summary>

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x200")

label = ttk.Label(root, text="Celsius to Kelvin Converter")
label.grid(row=0, column=0, padx=10, pady=10)

button = ttk.Button(root, text="Convert")
button.grid(row=1, column=0, padx=10, pady=5)

root.mainloop()
```

</details>

---

## Task 2: Add an Entry Field and Read the Input

Extend `unit_converter.py`.

Add an input field so the user can type a temperature, and a label to display the result.

Rules:

1. Create a `tk.StringVar` called `input_var` to hold the entry value.
2. Add a `ttk.Entry` widget bound to `input_var` and place it in row 1. Move the button to row 2.
3. Add a second `ttk.Label` below the button (row 3) to display the result. Bind it to a `tk.StringVar` called `result_var`.
4. Write a function `convert()` that:
   - reads the value from `input_var` using `.get()`
   - converts it to a float and adds `273.15`
   - writes the result to `result_var` using `.set()`
5. Connect `convert` to the button using the `command` parameter.

<details>
<summary>Solution (Task 2)</summary>

```python
import tkinter as tk
from tkinter import ttk

def convert():
    celsius = float(input_var.get())
    kelvin = celsius + 273.15
    result_var.set(f"{kelvin:.2f} K")

root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x200")

input_var = tk.StringVar()
result_var = tk.StringVar()

title_label = ttk.Label(root, text="Celsius to Kelvin Converter")
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

entry = ttk.Entry(root, textvariable=input_var, width=20)
entry.grid(row=1, column=0, padx=10, pady=5)

button = ttk.Button(root, text="Convert", command=convert)
button.grid(row=2, column=0, padx=10, pady=5)

result_label = ttk.Label(root, textvariable=result_var)
result_label.grid(row=3, column=0, padx=10, pady=5)

root.mainloop()
```

</details>

---

## Task 3: Add Input Validation and a Clear Button

Extend `unit_converter.py`.

Handle the case where the user types something that is not a number, and add a button to reset the form.

Rules:

1. Update `convert()` so that if `float()` fails because the input is not a valid number, `result_var` is set to `"Invalid input — enter a number"` instead of raising an error. Use an `if` check with `str.replace()` and `str.lstrip()` and `str.isdigit()` to validate, or check using a helper — do not use `try/except`.
2. Add a `ttk.Button` with the text `"Clear"` in row 2, column 1.
3. Write a function `clear()` that sets both `input_var` and `result_var` back to empty strings using `.set("")`.
4. Connect `clear` to the Clear button.

<details>
<summary>Solution (Task 3)</summary>

```python
import tkinter as tk
from tkinter import ttk

def is_valid_number(value):
    cleaned = value.strip().lstrip("-")
    return cleaned.replace(".", "", 1).isdigit() and len(cleaned) > 0

def convert():
    value = input_var.get()
    if not is_valid_number(value):
        result_var.set("Invalid input — enter a number")
        return
    kelvin = float(value) + 273.15
    result_var.set(f"{kelvin:.2f} K")

def clear():
    input_var.set("")
    result_var.set("")

root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x200")

input_var = tk.StringVar()
result_var = tk.StringVar()

title_label = ttk.Label(root, text="Celsius to Kelvin Converter")
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

entry = ttk.Entry(root, textvariable=input_var, width=20)
entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

convert_button = ttk.Button(root, text="Convert", command=convert)
convert_button.grid(row=2, column=0, padx=10, pady=5)

clear_button = ttk.Button(root, text="Clear", command=clear)
clear_button.grid(row=2, column=1, padx=10, pady=5)

result_label = ttk.Label(root, textvariable=result_var)
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
```

</details>

---

## Task 4 (Optional): Add a Conversion History

Extend `unit_converter.py`.

Add a scrollable list that records every successful conversion.

Rules:

1. Add a `tk.Listbox` widget with a `ttk.Scrollbar` attached to it. Place them in row 4, spanning both columns.
2. Connect the scrollbar to the listbox using the `yscrollcommand` and `xscrollcommand` parameters.
3. Update `convert()` so that after a successful conversion it inserts a new entry into the listbox in the format `"18.0 °C → 291.15 K"`.
4. Update `clear()` so that it also clears all entries from the listbox using `listbox.delete(0, tk.END)`.

<details>
<summary>Solution (Task 4 Optional)</summary>

```python
import tkinter as tk
from tkinter import ttk

def is_valid_number(value):
    cleaned = value.strip().lstrip("-")
    return cleaned.replace(".", "", 1).isdigit() and len(cleaned) > 0

def convert():
    value = input_var.get()
    if not is_valid_number(value):
        result_var.set("Invalid input — enter a number")
        return
    celsius = float(value)
    kelvin = celsius + 273.15
    result_var.set(f"{kelvin:.2f} K")
    history.insert(tk.END, f"{celsius} °C → {kelvin:.2f} K")

def clear():
    input_var.set("")
    result_var.set("")
    history.delete(0, tk.END)

root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x300")

input_var = tk.StringVar()
result_var = tk.StringVar()

title_label = ttk.Label(root, text="Celsius to Kelvin Converter")
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

entry = ttk.Entry(root, textvariable=input_var, width=20)
entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

convert_button = ttk.Button(root, text="Convert", command=convert)
convert_button.grid(row=2, column=0, padx=10, pady=5)

clear_button = ttk.Button(root, text="Clear", command=clear)
clear_button.grid(row=2, column=1, padx=10, pady=5)

result_label = ttk.Label(root, textvariable=result_var)
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL)
history = tk.Listbox(root, height=6, yscrollcommand=scrollbar.set)
scrollbar.config(command=history.yview)

history.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
scrollbar.grid(row=4, column=2, sticky="ns", pady=5)

root.mainloop()
```

</details>

---

## Reflection

- Why is `StringVar` more useful than reading the entry widget's value directly with a method call every time?
- What would happen if you called `root.mainloop()` before adding any widgets?
- Where in a larger tkinter application would you expect callbacks like `convert()` to grow complex, and how might you manage that?