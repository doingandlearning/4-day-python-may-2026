## tkinter session, mixed audience

---

## Files in this demo

| File | Purpose |
|------|---------|
| `monitor_scaffold.py` | Starting point — open this first |
| `monitor_full.py` | Finished app — the reveal |
| `sensor_data.csv` | Sample CSV with four "sensor" channels |

**Install requirement:** `pip install matplotlib` (tkinter ships with Python)

**Run from the demo folder:**

```bash
cd actual_code/tkinter-demo   # or wherever you copied the files
pip install matplotlib
python monitor_scaffold.py
```

---

## Arc of the session

### 1. Open the scaffold (5 min)

- Show `monitor_scaffold.py` — point out it's *nothing* yet: just a root window and a label
- Ask: "Who's used tkinter before?" — acknowledge both groups
- Say you're going to build something together that feels closer to what they actually do at work

Starting point (what students see):

```python
import tkinter as tk
from tkinter import ttk


def main():
    root = tk.Tk()
    root.title("CERN Instrument Monitor")
    root.geometry("900x600")

    label = ttk.Label(root, text="Ready to build the monitor...")
    label.pack(expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()
```

Key point to land early:

> tkinter's real trick is the **event loop** — `mainloop()` is blocking, which means you can't just use `time.sleep()` to update a plot. You need `after()` instead.

---

### 2. Build live (20–25 min) — suggested order

Work through these in order; don't rush to finish, stop and explain each pattern.

**Tip:** After Step 1 you're on a class-based app. Each later step adds methods or replaces `main()` — paste the blocks into `monitor_scaffold.py` in order.

---

#### Step 1 — Basic window + ttk style (~3 min)

**Say:** `ttk` widgets pick up a theme; `clam` is the most tweakable built-in theme. Plain `tk.Button` vs `ttk.Button` — themed vs native look.

**Replace** `main()` with a minimal app class (delete the old `label.pack` block):

```python
import tkinter as tk
from tkinter import ttk


class InstrumentMonitor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CERN Instrument Monitor")
        self.geometry("900x600")

        style = ttk.Style(self)
        style.theme_use("clam")  # 'clam' | 'alt' | 'default' — try them live

        ttk.Label(self, text="CERN Instrument Monitor — building…").pack(
            padx=20, pady=20
        )


if __name__ == "__main__":
    app = InstrumentMonitor()
    app.mainloop()
```

**Run** — window with themed label. Mention you'll ditch `pack()` for real layout next.

---

#### Step 2 — Layout with `grid()` (~5 min)

**Say:** `grid()` gives row/column alignment; `columnconfigure(..., weight=1)` lets columns stretch when the window resizes.

**Add** to `__init__` after the style lines (remove the `.pack()` label):

```python
        self._build_controls()

    def _build_controls(self):
        ctrl = ttk.Frame(self, padding=(10, 8))
        ctrl.grid(row=0, column=0, sticky="ew")
        self.columnconfigure(0, weight=1)

        ttk.Label(ctrl, text="Source:").grid(row=0, column=0, padx=(0, 4))
        ttk.Combobox(
            ctrl, values=["Simulated", "CSV File"], width=12, state="readonly"
        ).grid(row=0, column=1, padx=(0, 8))

        ttk.Button(ctrl, text="Browse CSV…", state="disabled").grid(
            row=0, column=2, padx=(0, 16)
        )

        ttk.Label(ctrl, text="Channel:").grid(row=0, column=3, padx=(0, 4))
        ttk.Combobox(
            ctrl,
            values=[
                "beam_current_mA",
                "temperature_C",
                "vacuum_pressure_mbar",
                "magnet_field_T",
            ],
            width=22,
            state="readonly",
        ).grid(row=0, column=4, padx=(0, 16))

        ttk.Label(ctrl, text="Interval (ms):").grid(row=0, column=5, padx=(0, 4))
        ttk.Spinbox(ctrl, from_=100, to=2000, increment=100, width=7).grid(
            row=0, column=6, padx=(0, 16)
        )

        ttk.Button(ctrl, text="▶  Start").grid(row=0, column=7, padx=(0, 4))
        ttk.Button(ctrl, text="■  Stop", state="disabled").grid(row=0, column=8)
```

**Run** — top bar only. Resize window; columns should stretch.

---

#### Step 3 — `StringVar` / `IntVar` (~3 min)

**Say:** These are tkinter's reactive variables — bind them to widgets and both sides stay in sync.

**Add** near the top of `__init__` (after `super().__init__()`):

```python
        self.source_var = tk.StringVar(value="Simulated")
        self.channel_var = tk.StringVar(value="beam_current_mA")
        self.interval_var = tk.IntVar(value=500)
        self.status_var = tk.StringVar(value="IDLE")
```

**Wire** the comboboxes and spinbox (replace the bare `ttk.Combobox(...)` calls):

```python
        ttk.Combobox(
            ctrl,
            textvariable=self.source_var,
            values=["Simulated", "CSV File"],
            width=12,
            state="readonly",
        ).grid(row=0, column=1, padx=(0, 8))

        # ... channel combobox:
        ttk.Combobox(
            ctrl,
            textvariable=self.channel_var,
            values=[
                "beam_current_mA",
                "temperature_C",
                "vacuum_pressure_mbar",
                "magnet_field_T",
            ],
            width=22,
            state="readonly",
        ).grid(row=0, column=4, padx=(0, 16))

        ttk.Spinbox(
            ctrl,
            from_=100,
            to=2000,
            increment=100,
            textvariable=self.interval_var,
            width=7,
        ).grid(row=0, column=6, padx=(0, 16))
```

**Add** a status row under the controls (still in `_build_controls` or a new `_build_status`):

```python
        status = ttk.Frame(self, padding=(10, 4))
        status.grid(row=2, column=0, sticky="ew")

        ttk.Label(status, text="Status:").grid(row=0, column=0, padx=(0, 4))
        ttk.Label(status, textvariable=self.status_var).grid(row=0, column=1)
```

**Live demo trick** — in the Python REPL *or* a temporary button:

```python
# Prove the binding: change the var, label updates without touching the label
self.status_var.set("NOMINAL")
```

---

#### Step 4 — Embed matplotlib (~5 min)

**Say:** `matplotlib.use("TkAgg")` must run **before** `import pyplot`. The canvas is just another widget you `pack`/`grid` like anything else.

**Add imports** at the top of the file:

```python
import matplotlib

matplotlib.use("TkAgg")  # MUST be before pyplot
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk,
)
```

**Add** to `__init__` after controls:

```python
        self._build_plot()

    def _build_plot(self):
        plot_frame = ttk.Frame(self)
        plot_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=6)
        self.rowconfigure(1, weight=1)

        self._fig, self._ax = plt.subplots(figsize=(9, 4))
        self._line, = self._ax.plot([], [], linewidth=1.8)
        self._ax.set_xlabel("Sample")
        self._ax.set_ylabel(self.channel_var.get())

        self._canvas = FigureCanvasTkAgg(self._fig, master=plot_frame)
        self._canvas.draw()
        self._canvas.get_tk_widget().pack(fill="both", expand=True)

        toolbar_frame = ttk.Frame(plot_frame)
        toolbar_frame.pack(fill="x")
        NavigationToolbar2Tk(self._canvas, toolbar_frame)
```

**Run** — empty plot with zoom/pan toolbar. Let someone try the toolbar.

---

#### Step 5 — The `after()` loop (~5 min)

**Say:** A `while` loop with `time.sleep()` inside `mainloop()` freezes the UI — the event loop never gets to process redraws or clicks.

**Wrong way** (show, then comment out — do not leave running):

```python
import time

def _bad_update_loop(self):
    while self.running:
        time.sleep(0.5)   # blocks the entire UI thread
        self._tick()
```

**Right way** — add state and handlers to the class:

```python
        # in __init__:
        self.running = False
        self._after_id = None
        self._xdata: list[float] = []
        self._ydata: list[float] = []
```

Wire Start/Stop (keep references to buttons if you need to toggle state):

```python
        self.start_btn = ttk.Button(ctrl, text="▶  Start", command=self._start)
        self.start_btn.grid(row=0, column=7, padx=(0, 4))

        self.stop_btn = ttk.Button(
            ctrl, text="■  Stop", command=self._stop, state="disabled"
        )
        self.stop_btn.grid(row=0, column=8)
```

**Minimal tick** (fake data until Step 6):

```python
    def _start(self):
        if self.running:
            return
        self.running = True
        self.start_btn.configure(state="disabled")
        self.stop_btn.configure(state="normal")
        self.status_var.set("RUNNING")
        self._schedule_update()

    def _stop(self):
        self.running = False
        if self._after_id:
            self.after_cancel(self._after_id)
            self._after_id = None
        self.start_btn.configure(state="normal")
        self.stop_btn.configure(state="disabled")
        self.status_var.set("STOPPED")

    def _schedule_update(self):
        interval = max(100, self.interval_var.get())
        self._after_id = self.after(interval, self._tick)

    def _tick(self):
        if not self.running:
            return

        import random
        value = 120.0 + random.uniform(-2, 2)  # placeholder until Step 6

        n = len(self._xdata)
        self._xdata.append(n)
        self._ydata.append(value)
        if len(self._xdata) > 80:
            self._xdata.pop(0)
            self._ydata.pop(0)

        self._line.set_data(range(len(self._ydata)), self._ydata)
        self._ax.relim()
        self._ax.autoscale_view()
        self._canvas.draw_idle()  # cheaper than draw()

        self._schedule_update()  # schedule next tick — non-blocking chain
```

**Run** — plot should roll. Click Stop; UI stays responsive.

---

#### Step 6 — Data sources (~5 min)

**Say:** Separate *data* from *UI* — same pattern as instrument drivers vs dashboard.

**Add imports:**

```python
import csv
import math
import random
from tkinter import filedialog
```

**Add classes** above `InstrumentMonitor`:

```python
class DataSource:
    def next_value(self) -> float:
        raise NotImplementedError


class SimulatedSource(DataSource):
    def __init__(self, channel: str):
        self.channel = channel
        self._tick = 0
        self._centres = {
            "beam_current_mA": 122.0,
            "temperature_C": 19.0,
            "vacuum_pressure_mbar": 1.2e-8,
            "magnet_field_T": 8.336,
        }
        self._amplitudes = {
            "beam_current_mA": 3.5,
            "temperature_C": 0.8,
            "vacuum_pressure_mbar": 2e-9,
            "magnet_field_T": 0.008,
        }

    def next_value(self) -> float:
        centre = self._centres.get(self.channel, 1.0)
        amp = self._amplitudes.get(self.channel, 0.1)
        noise = random.gauss(0, amp * 0.15)
        value = centre + amp * math.sin(self._tick * 0.25) + noise
        self._tick += 1
        return value


class CsvSource(DataSource):
    def __init__(self, filepath: str, channel: str):
        self._rows: list[float] = []
        self._index = 0
        with open(filepath, newline="") as f:
            for row in csv.DictReader(f):
                if channel in row:
                    try:
                        self._rows.append(float(row[channel]))
                    except ValueError:
                        pass

    def next_value(self) -> float:
        if not self._rows:
            return 0.0
        value = self._rows[self._index % len(self._rows)]
        self._index += 1
        return value
```

**In `__init__`:**

```python
        self._source: DataSource | None = None
        self._csv_path: str | None = None
```

**Enable Browse** when source is CSV:

```python
        self.csv_btn = ttk.Button(
            ctrl, text="Browse CSV…", command=self._browse_csv, state="disabled"
        )
        # bind source combobox:
        src_combo.bind("<<ComboboxSelected>>", self._on_source_change)

    def _on_source_change(self, _event=None):
        is_csv = self.source_var.get() == "CSV File"
        self.csv_btn.configure(state="normal" if is_csv else "disabled")
        self._stop()

    def _browse_csv(self):
        path = filedialog.askopenfilename(
            title="Select sensor CSV",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
        )
        if path:
            self._csv_path = path
            self._source = None
```

**Update `_start`** to pick a source:

```python
    def _start(self):
        if self.running:
            return
        channel = self.channel_var.get()
        if self.source_var.get() == "CSV File":
            if not self._csv_path:
                self.status_var.set("No CSV loaded")
                return
            self._source = CsvSource(self._csv_path, channel)
        else:
            self._source = SimulatedSource(channel)

        self.running = True
        # ... rest unchanged
```

**Update `_tick`** — replace the random placeholder:

```python
        value = self._source.next_value()
```

**Demo:** `sensor_data.csv` in the same folder — pick a channel, Browse, Start.

---

#### Step 7 — Threshold alerting (~3 min)

**Say:** Same idea as a monitoring dashboard — reference lines + status colour.

**Add** constants near the top:

```python
ALERT_THRESHOLDS = {
    "beam_current_mA": (115.0, 128.0),
    "temperature_C": (17.0, 21.0),
    "vacuum_pressure_mbar": (0.0, 2.0e-8),
    "magnet_field_T": (8.32, 8.36),
}
ALERT_COLOUR = "#cc2200"
NORMAL_COLOUR = "#007700"
```

**After creating the plot line** in `_build_plot`:

```python
        self._thresh_lines = [
            self._ax.axhline(0, color="red", linestyle="--", alpha=0.6),
            self._ax.axhline(0, color="red", linestyle="--", alpha=0.6),
        ]
        self._update_thresholds()
```

**Keep a reference** to the status label so you can change colour:

```python
        self._alert_label = ttk.Label(status, textvariable=self.status_var)
        self._alert_label.grid(row=0, column=1)
```

```python
    def _update_thresholds(self):
        ch = self.channel_var.get()
        lo, hi = ALERT_THRESHOLDS.get(ch, (None, None))
        if lo is not None:
            self._thresh_lines[0].set_ydata([lo, lo])
            self._thresh_lines[1].set_ydata([hi, hi])
            for line in self._thresh_lines:
                line.set_visible(True)
        else:
            for line in self._thresh_lines:
                line.set_visible(False)

    def _check_threshold(self, value: float):
        ch = self.channel_var.get()
        lo, hi = ALERT_THRESHOLDS.get(ch, (None, None))
        if lo is None:
            return
        if value < lo or value > hi:
            self.status_var.set("⚠  OUT OF RANGE")
            self._alert_label.configure(foreground=ALERT_COLOUR)
        else:
            self.status_var.set("✓  NOMINAL")
            self._alert_label.configure(foreground=NORMAL_COLOUR)
```

**Call** `self._check_threshold(value)` at the end of `_tick`.

**Run** — switch to `beam_current_mA`, simulated source; watch lines and status flip.

---

### 3. Reveal the full version (5 min)

- Open `monitor_full.py` side by side
- Point out what you *didn't* build live: dark theme (`_apply_styles`), rolling status fields (`_value_var`, `_count_var`), channel-change handler clearing buffers
- Invite questions: "What would you add? What channel would you actually want to monitor here?"

**Quick diff highlights** (full version only):

```python
# Dark theme — style.configure on custom "Dark.TFrame" / "Dark.TLabel"
def _apply_styles(self, style: ttk.Style):
    style.configure("Dark.TFrame", background=BG_DARK)
    # ...

# Channel change clears buffers and redraws thresholds
def _on_channel_change(self, _event=None):
    self._stop()
    self._xdata.clear()
    self._ydata.clear()
    # ...
```

---

## Patterns cheat-sheet (for questions)

| Pattern | Where in the code | Why it matters |
|---------|------------------|---------------|
| `ttk.Style` + `theme_use` | `__init__` / `_apply_styles()` | Consistent look; separates style from structure |
| `grid()` geometry manager | `_build_controls()`, `_build_plot()` | Predictable alignment; better than pack for multi-column layouts |
| `StringVar` / `IntVar` | `source_var`, `channel_var`, etc. | Two-way binding between widget and Python variable |
| `FigureCanvasTkAgg` | `_build_plot()` | Embeds any matplotlib figure as a tkinter widget |
| `NavigationToolbar2Tk` | After canvas setup | Free interactive toolbar — zoom, pan, save to PNG |
| `after(ms, callback)` | `_schedule_update()` | Non-blocking periodic updates — the only safe way to animate |
| `draw_idle()` | `_tick()` | Cheaper than `draw()` — only redraws dirty regions |
| `filedialog.askopenfilename` | `_browse_csv()` | Native OS file picker, one line |
| `axhline()` | `_update_thresholds()` | Horizontal reference lines on the plot |

---

## Likely questions

**"Why not just use a web dashboard?"**
Fair question. tkinter is great when you want a self-contained desktop tool with no server, no browser, no dependencies beyond Python. For a shared monitoring dashboard, yes — web makes more sense. For a quick local analysis tool or a lab instrument interface, tkinter wins on simplicity.

**"Can you use pandas instead of the csv module?"**
Absolutely:

```python
import pandas as pd
df = pd.read_csv(filepath)
values = df[channel].astype(float).tolist()
```

**"Is tkinter good enough for production tools?"**
Many real scientific instrument GUIs are tkinter. ROOT (the CERN analysis framework) has its own GUI layer, but plenty of lab tooling is plain Python + tkinter. It's not pretty by default, but it works.

**"What about threading for heavy data processing?"**
All UI updates must happen on the main thread. Worker thread + `queue.Queue` + drain on the main thread via `after()`:

```python
import queue
import threading

self._queue: queue.Queue = queue.Queue()

def _worker():
    result = heavy_computation()
    self._queue.put(result)

threading.Thread(target=_worker, daemon=True).start()

def _poll_queue(self):
    try:
        while True:
            value = self._queue.get_nowait()
            self._handle_value(value)
    except queue.Empty:
        pass
    self.after(100, self._poll_queue)
```

---

## Timing guide

| Segment | Time |
|---------|------|
| Scaffold walkthrough + context | 5 min |
| Live build (Steps 1–5) | 15 min |
| Live build (Steps 6–7) | 10 min |
| Reveal full version + questions | 10 min |
| **Total** | **~40 min** |

---

## Emergency shortcuts

If you're running short on time, skip to a working app:

```bash
python monitor_full.py
```

If matplotlib import fails on macOS/Linux headless SSH, remind them: needs a display (or X forwarding). For the room, local laptop is fine.

If the plot stays frozen after Step 5, check: (1) `_schedule_update()` called at end of `_tick`, (2) not using `time.sleep`, (3) `draw_idle()` not blocking elsewhere.
