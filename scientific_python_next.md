# Scientific Python — What to Learn Next

This course covered core Python including files, classes, testing, threads, and processes.
If your work involves **numeric data, plots, or CSV files**, the natural next step is the scientific Python stack.

---

## Start in this repository

You already have material here — use it before hunting for new tutorials:

| Material | Location |
|----------|----------|
| Guided lab (NumPy + pandas) | [labs/Appx-Numpy-and-Matplotlib/guided_lab.md](labs/Appx-Numpy-and-Matplotlib/guided_lab.md) |
| Lab scripts | [labs/Appx-Numpy-and-Matplotlib/](labs/Appx-Numpy-and-Matplotlib/) |
| Sample solutions | [labs-solutions/Appx1-Numpy/](labs-solutions/Appx1-Numpy/) |
| Slides | [slides/Apx-1-Numpy-and-Matplotlib.md](slides/Apx-1-Numpy-and-Matplotlib.md) |

Install once in your project venv:

```text
pip install numpy pandas matplotlib
```

---

## The three layers (mental model)

| Tool | Think of it as | When to reach for it |
|------|------------------|----------------------|
| **NumPy** | Fast arrays and math on numbers | Grids of measurements, linear algebra, vectorised formulas |
| **pandas** | Tables with named columns (like a spreadsheet) | CSV logs, filters, group-by, missing data |
| **matplotlib** | Plots and figures | Quick charts, publication-style plots |

**Rule of thumb:** CSV or labelled columns → pandas. Pure numeric grids and formulas → NumPy. Either can feed matplotlib.

---

## Jupyter notebooks (optional)

Notebooks let you run code in **cells** and keep results, plots, and notes in one file.

- Install: `pip install jupyterlab` (or `notebook`)
- Run: `jupyter lab` in your project folder
- Good for: exploration, teaching, one-off analysis
- Less ideal for: production pipelines, large reusable libraries

For scripts you run repeatedly from the command line, stay with `.py` files and pytest (as in Lab 11).

---

## Small projects to try

1. **Load your own CSV** — instrument log, survey export, open data; use `pd.read_csv`, `head()`, `describe()`.
2. **Filter and plot** — subset rows (e.g. channel or run ID), plot one column vs another with matplotlib.
3. **Replace a loop with NumPy** — take a calculation you wrote with a `for` loop over numbers and express it with array operations.
4. **Combine with course skills** — read config from a JSON file (modules lab), write summary stats to a new CSV (files lab), add a pytest for a pure function that processes a small array.

---

## Performance note

NumPy and pandas release the **GIL** during heavy C-level work, so they can be fast without you writing threads.
Do not thread plain Python loops over large data — vectorise or use NumPy instead. See [threads_vs_processes.md](threads_vs_processes.md).

---

## Further reading

| Resource | Notes |
|----------|--------|
| [Scientific Python](https://scientific-python.org/) | Ecosystem overview and learning links |
| _Python for Data Analysis_ (Wes McKinney) | pandas-focused; often on O’Reilly or library |
| [whats-next.md](whats-next.md) | Broader learning paths and practice sites |
| [python_quick_reference.md](python_quick_reference.md) | Official docs and debugging |

---

## Sharing scientific code

Colleagues with Python: [sharing_your_project.md](sharing_your_project.md) with `numpy`, `pandas`, `matplotlib` in `requirements.txt`.

Colleagues without Python: [packaging_your_project.md](packaging_your_project.md) — expect large executables if you bundle the full stack.
