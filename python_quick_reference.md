# Python Quick Reference — Where Answers Live

A one-page map for finding answers after the course. You already know how to program; this is about **Python’s ecosystem**.

---

## In the interpreter or a script

```python
help(len)           # documentation for a function
help("str")         # documentation for a type/module name
dir(some_object)    # names available on an object
```

In many editors, hover over a name or use “Go to definition” for the same effect.

---

## Official documentation

| Resource | URL | Use for |
|----------|-----|---------|
| Python 3 docs (tutorial + library) | https://docs.python.org/3/ | Language and standard library |
| Built-in functions | https://docs.python.org/3/library/functions.html | `len`, `range`, `open`, … |
| Standard library index | https://docs.python.org/3/library/index.html | `csv`, `json`, `pathlib`, `threading`, … |
| Language reference | https://docs.python.org/3/reference/ | Precise rules (semantics, syntax) |
| PEP index | https://peps.python.org/ | Design decisions and new features |

Start with the **tutorial** if you want narrative explanations; use the **library reference** when you know the module name.

---

## Third-party libraries

Install with `pip install package_name`, then read **that package’s** docs (linked from PyPI: https://pypi.org/).

Common in scientific work:

| Library | Docs |
|---------|------|
| NumPy | https://numpy.org/doc/ |
| pandas | https://pandas.pydata.org/docs/ |
| matplotlib | https://matplotlib.org/stable/ |
| pytest | https://docs.pytest.org/ |

---

## Reading a traceback

Read from the **bottom** upward:

1. **Last line** — the exception type and message (e.g. `TypeError: ...`)
2. **Lines above** — which file and line raised it
3. **Higher frames** — who called whom

The error is usually in **your** code (paths without `site-packages`), not inside the standard library.

Use [learning_prompts.md](learning_prompts.md) Prompt 6 to ask AI to explain an error **without** asking for the fix.

---

## Debugging without rewriting everything

| Technique | How |
|-----------|-----|
| Print key values | `print(f"x={x!r}")` — `!r` shows repr, helpful for types |
| Breakpoint | Add `breakpoint()` and run from a terminal; use `n`, `s`, `c`, `q` in pdb |
| Run from terminal | See full traceback; IDEs sometimes hide detail |
| Logging | `import logging` — better than print for scripts that run often |

See also [using_ai_after_the_course.md](using_ai_after_the_course.md) and Prompt 4 in [learning_prompts.md](learning_prompts.md).

---

## Searching the web

Good queries include the **exception type**, **library name**, and **Python version**:

- `python 3 ValueError int() base 10`
- `pandas read_csv encoding error`

Prefer recent results; check the answer matches Python 3, not Python 2.

Stack Overflow is useful for **specific errors**; official docs are better for **how a module is supposed to work**.

---

## Standard library modules worth knowing

Many were introduced in the course; this maps names to problems:

| Module | Typical use |
|--------|-------------|
| `pathlib` | Paths and files in a portable way |
| `csv` | Read/write CSV without pandas |
| `json` | Config and API payloads |
| `datetime` | Dates and times |
| `collections` | `defaultdict`, `Counter`, … |
| `itertools` | Combinations, chaining iterables |
| `copy` | Shallow and deep copy |
| `re` | Regular expressions |
| `threading` / `multiprocessing` | Concurrency — see [threads_vs_processes.md](threads_vs_processes.md) |
| `unittest` / third-party `pytest` | Automated tests — Lab 11 |

---

## When you are stuck

1. Read the traceback bottom-up.
2. Check the official docs for the function or module involved.
3. Try a minimal example in the REPL (`python` in a terminal).
4. Use a [learning_prompts.md](learning_prompts.md) template — explain, don’t “fix my homework.”
5. Ask a colleague or community (see [whats-next.md](whats-next.md)).
