# Sharing Your Python Project with Colleagues

Use this guide when your colleague **already has Python** (or can install it).
It is usually simpler and easier to maintain than building a standalone executable.

For colleagues **without** Python, see [packaging_your_project.md](packaging_your_project.md) (PyInstaller).

---

## Which approach?

| Situation | Best approach |
|-----------|----------------|
| Colleague has Python (or IT can install it) | This guide — `venv` + `requirements.txt` |
| Colleague cannot install Python | [packaging_your_project.md](packaging_your_project.md) — PyInstaller |
| You will update the script often | This guide — they pull changes and reinstall deps if needed |
| One-off handoff, no updates | Either works; PyInstaller is a single file |

---

## What you send

At minimum:

- Your `.py` files (or a small project folder)
- A `requirements.txt` listing third-party packages
- Short instructions (copy from the template below)

Optional but helpful:

- A `README` with how to run the main script
- Sample input data (small, non-sensitive files only)

---

## Step 1: Create a virtual environment (on your machine)

In your project folder:

```text
python -m venv .venv
```

Activate it:

**Windows (Command Prompt)**

```text
.venv\Scripts\activate
```

**macOS / Linux**

```text
source .venv/bin/activate
```

Your prompt should show `(.venv)`. Install your dependencies inside this environment.

---

## Step 2: Record dependencies in requirements.txt

With the venv activated:

```text
pip install numpy pandas
pip freeze > requirements.txt
```

Edit `requirements.txt` if needed — remove packages you did not actually use.
For a minimal script with no third-party libs, `requirements.txt` can be empty or omitted.

---

## Step 3: Test a clean install

Simulate what your colleague will do:

1. Deactivate: `deactivate`
2. Create a fresh venv: `python -m venv test_venv`
3. Activate `test_venv`
4. Run: `pip install -r requirements.txt`
5. Run your script: `python your_script.py`

If that works, your handoff instructions are trustworthy.

---

## Step 4: Instructions for your colleague

Include something like this in email or a `README`:

```text
1. Install Python 3.10+ if you do not have it (python.org or your IT package manager).
2. Open a terminal in the project folder.
3. Create a virtual environment:
     python -m venv .venv
4. Activate it:
     Windows:  .venv\Scripts\activate
     macOS:    source .venv/bin/activate
5. Install dependencies:
     pip install -r requirements.txt
6. Run the script:
     python your_script.py
```

Replace `your_script.py` with your entry point.

---

## Common problems

### `pip` not found

Try `python -m pip install -r requirements.txt` instead of `pip install`.

### Wrong Python version

Note the Python version you used (e.g. 3.11) in the README. Mixed 3.9 / 3.12 can break some packages.

### Script runs for you but not for them

- Confirm they activated the venv before `pip install` and before `python your_script.py`
- Check file paths — use paths relative to the script or document where data files must live
- On Windows vs macOS, path separators differ; prefer `pathlib.Path` in code

### Large scientific stack

`numpy`, `pandas`, and `matplotlib` take time to download. That is normal; they only install once per venv.

---

## Security note

Do not put passwords, API keys, or internal URLs in `requirements.txt` or committed files.
Use environment variables or a local config file that is **not** shared (add it to `.gitignore` if using git).
