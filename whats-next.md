# What's Next?

Most learners hit a plateau after an introductory course—not because Python gets harder, but because the **next steps feel fuzzy**. Below is a curated map of resources, challenges, and project ideas suited to scientists, engineers, and programmers. Mix structured study with bite-size practice and small automation wins to keep momentum high.

For course-specific follow-ups (sharing code, NumPy lab, AI prompts), start with [POST_COURSE.md](POST_COURSE.md).

---

## Structured Learning & Reference

### Real Python

Free tutorials and paid learning paths cover everything from f-strings to async I/O, with quizzes to check retention — [realpython.com](https://realpython.com/)

### Python Morsels

Weekly graded challenges (novice → advanced) plus screencasts; ideal for habit building without overwhelm — [pythonmorsels.com](https://www.pythonmorsels.com/exercises/)

### O'Reilly Learning Platform

If you have access (many organisations do), use it for interactive Python labs and books such as _Learning Python_, _Fluent Python_, and _Python for Data Analysis_ (Wes McKinney).

### Recommended Books

| Goal | Title | Why it helps |
|------|-------|--------------|
| Solid fundamentals | _Learning Python_ (Mark Lutz) | Deep coverage of core language |
| Practical wins | _Automate the Boring Stuff with Python_ (Al Sweigart) | Project-based automation — [free online](https://automatetheboringstuff.com/) |
| Data and tables | _Python for Data Analysis_ (Wes McKinney) | pandas and workflow for tabular data |

---

## Practice & Daily Challenges

| Format | Platform | Why try it? |
|--------|----------|-------------|
| Seasonal puzzles | [Advent of Code](https://adventofcode.com/) | One problem per day; great for pair programming |
| Guided exercises | [Exercism Python track](https://exercism.org/tracks/python) | 140+ exercises with optional mentor feedback |
| Idiomatic katas | [PyBites](https://codechalleng.es/) | Real-world, bite-sized challenges |
| Data micro-courses | [Kaggle Learn](https://www.kaggle.com/learn) | Interactive, low setup |
| Long habit | 100 Days of Python (various providers) | Build something daily for ~3 months |

Mix one evergreen track (e.g. Exercism) with a seasonal burst (Advent of Code).

---

## Projects & Applied Learning

Ideas that fit a scientific or engineering context:

1. **Lab automation** — bulk-rename run folders, parse log files, summarise CSV outputs from instruments ([Automate the Boring Stuff](https://automatetheboringstuff.com/) is a good pattern book).
2. **Data snack-size**
   - Load open data or your own CSV → clean with pandas → plot with matplotlib (continue [scientific_python_next.md](scientific_python_next.md)).
   - Simple ETL: CSV → filter → SQLite or a summary report.
3. **Reproducible analysis** — turn a one-off script into a small package with `requirements.txt` and pytest ([sharing_your_project.md](sharing_your_project.md), Lab 11).
4. **Monitoring or dashboards** — CLI or optional [tkinter lab](labs/z-Lab-Tkinter.md) for a simple GUI; Streamlit if you want a web UI with little frontend code.
5. **Open data APIs** — CERN Open Data Portal, INSPIRE-HEP, or other public APIs; build a small fetch-and-filter script.
6. **Kaggle mini-comp** — Titanic or House Prices to practise pandas and baselines — [kaggle.com/learn](https://www.kaggle.com/learn)

---

## Community & Support

| Community | Value |
|-----------|--------|
| [Python Discord](https://www.pythondiscord.com/) | Live help, code jams |
| [r/learnpython](https://www.reddit.com/r/learnpython/) | Peer Q&A |
| Real Python / PyBites communities | Topic-specific chat |
| Colleagues at your experiment or project | Best context for your stack and policies |

Join one or two communities so you have humans in the loop when docs are not enough.

---

## Suggested Paths

| Profile | Next 4 weeks | After 4 weeks |
|---------|--------------|---------------|
| **Scientist / engineer, new to Python** | [scientific_python_next.md](scientific_python_next.md) + Automate chapters 1–6 | One real automation on your own data |
| **Junior developer** | Python Morsels weekly + Exercism | Advent of Code or PyBites streak |
| **Experienced programmer** | _Fluent Python_ (selected chapters) + [python_quick_reference.md](python_quick_reference.md) | Small internal tool with tests; optional PyPI module |

---

## Final tip

Treat learning as **cycling gears**: alternate focused reading (low gear) with real-world friction (high gear). Use [learning_prompts.md](learning_prompts.md) when AI helps you learn; use [POST_COURSE.md](POST_COURSE.md) to find everything from this repo.
