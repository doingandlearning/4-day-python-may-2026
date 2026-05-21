# Packaging Your Python Script as an Executable

This guide walks you through turning a Python script into a standalone executable file
that a colleague can double-click and run — even if they do not have Python installed.

The tool used is **PyInstaller**, which bundles your script, the Python interpreter,
and all required libraries into a single file.

> **Alternative:** if your colleague already has Python, sharing a virtual environment
> and `requirements.txt` is often simpler. See [sharing_your_project.md](sharing_your_project.md).

---

## What you need before you start

- Your Python script working correctly on your own machine
- Python installed on your machine (the colleague receiving the file does not need it)
- A terminal / command prompt
- An internet connection to install PyInstaller

> **Important:** you must build the executable on the same type of operating system
> your colleague will run it on. To produce a `.exe` for Windows, build on Windows.
> To produce a `.app` for macOS, build on a Mac. You cannot cross-compile.

---

## Step 1: Open a terminal in your project folder

**Windows**

1. Open File Explorer and navigate to the folder containing your `.py` file.
2. Click the address bar at the top, type `cmd`, and press Enter.
   A Command Prompt window opens already pointing at your folder.

**macOS**

1. Open Finder and navigate to the folder containing your `.py` file.
2. Right-click the folder and choose **New Terminal at Folder**.
   If you do not see this option, open Terminal from Applications → Utilities,
   then type `cd ` (with a space), drag your folder into the Terminal window, and press Enter.

To confirm you are in the right place, type:

```text
Windows:   dir
macOS:     ls
```

You should see your `.py` file listed.

---

## Step 2: Install PyInstaller

Type the following and press Enter:

```text
pip install pyinstaller
```

Wait for it to finish. You should see a message ending in `Successfully installed pyinstaller-...`.

If you see `pip: command not found`, try `pip3` instead of `pip`.

---

## Step 3: Build the executable

Run the following command, replacing `your_script.py` with the actual name of your file:

```text
pyinstaller --onefile your_script.py
```

PyInstaller will print a lot of output. This is normal. Wait for it to finish —
it usually takes between 15 and 60 seconds.

> **If your script opens a window** (e.g. a tkinter app) and you do not want a
> black terminal/console window appearing behind it, add `--noconsole`:
>
> ```text
> pyinstaller --onefile --noconsole your_script.py
> ```
>
> On macOS, use `--windowed` instead:
>
> ```text
> pyinstaller --onefile --windowed your_script.py
> ```

---

## Step 4: Find your executable

When PyInstaller finishes, two new folders appear in your project folder:

```text
build/       ← temporary files, you can ignore this
dist/        ← your finished executable is here
```

Open the `dist` folder. You will find:

- **Windows:** `your_script.exe`
- **macOS:** `your_script` (a Unix executable) or `your_script.app`

This is the file to send to your colleague.

---

## Step 5: Test it before sending

Before sharing, double-click the executable yourself to confirm it runs correctly.

If it opens and closes immediately, there may be an error. To see what went wrong,
run it from the terminal instead:

**Windows**

```text
dist\your_script.exe
```

**macOS**

```text
./dist/your_script
```

Any error messages will appear in the terminal, which makes them much easier to diagnose.

---

## Sending the file to your colleague

**Windows:** send the single `.exe` file. Your colleague double-clicks it to run it.
Windows may show a "Windows protected your PC" warning the first time — they should
click **More info** then **Run anyway**.

**macOS:** send the file from the `dist` folder. Your colleague may see a message
saying the app is from an unidentified developer. To open it, they should:

1. Right-click (or Control-click) the file
2. Choose **Open**
3. Click **Open** again in the dialog that appears

They only need to do this once.

---

## Troubleshooting

### "Module not found" error when the executable runs

PyInstaller sometimes misses libraries that are imported indirectly.
Fix it by telling PyInstaller about the missing module explicitly:

```text
pyinstaller --onefile --hidden-import=the_missing_module your_script.py
```

Replace `the_missing_module` with the name shown in the error.
Common ones include `pandas`, `numpy`, `matplotlib`, and `tkinter`.

### The executable is very large

This is normal. PyInstaller bundles the entire Python interpreter and all libraries.
A script that uses pandas and matplotlib may produce an executable of 100–300 MB.
There is no easy fix for this — it is a known trade-off of the approach.

### The executable is slow to start the first time

Also normal for `--onefile` builds. When run, the executable unpacks itself into
a temporary folder before starting. This takes a few extra seconds on the first launch.
Subsequent runs are faster.

### It works on your machine but not your colleague's

The most common cause is that you built on a different operating system version.
For example, building on macOS 14 (Sonoma) and sending to someone on macOS 12 (Monterey)
can cause compatibility issues. If possible, build on an older OS version than your
colleague is running, or ask them to describe the exact error they see.

---

## Quick reference

| What you want | Command |
|---|---|
| Basic executable | `pyinstaller --onefile your_script.py` |
| No console window (Windows) | `pyinstaller --onefile --noconsole your_script.py` |
| No console window (macOS) | `pyinstaller --onefile --windowed your_script.py` |
| Fix a missing module | add `--hidden-import=module_name` |
| Custom icon (Windows) | add `--icon=icon.ico` |
| Custom icon (macOS) | add `--icon=icon.icns` |
