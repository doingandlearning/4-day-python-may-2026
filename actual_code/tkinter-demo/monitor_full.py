"""
CERN Instrument Monitor — FULL VERSION
=======================================
A tkinter demo app built for a CERN data analysis / equipment testing audience.

Patterns demonstrated:
  - ttk theming (clam) and consistent widget styling
  - Frame-based layout with grid() geometry manager
  - Embedding a matplotlib FigureCanvasTkAgg in a tkinter frame
  - NavigationToolbar2Tk for free zoom/pan/save
  - after() for non-blocking periodic updates (the event loop trick)
  - StringVar / IntVar bound to widgets for reactive state
  - filedialog.askopenfilename() for CSV loading
  - Threshold alerting with dynamic label colour changes
  - Clean separation: data layer vs UI layer

Data sources:
  - Simulated: sine + noise, mimicking a beam current signal
  - CSV: loads timestamp + any numeric column from a file

To run:
    pip install matplotlib
    python monitor_full.py
"""

import csv
import math
import random
import tkinter as tk
from tkinter import filedialog, ttk

import matplotlib
matplotlib.use("TkAgg")  # Must be set before importing pyplot
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

WINDOW_TITLE  = "CERN Instrument Monitor"
WINDOW_SIZE   = "1050x680"
UPDATE_MS     = 500          # how often after() fires (milliseconds)
MAX_POINTS    = 80           # rolling window length
ALERT_COLOUR  = "#cc2200"
NORMAL_COLOUR = "#007700"
BG_DARK       = "#1e1e2e"
BG_MID        = "#2a2a3e"
FG_LIGHT      = "#cdd6f4"

CHANNELS = ["beam_current_mA", "temperature_C", "vacuum_pressure_mbar", "magnet_field_T"]

ALERT_THRESHOLDS = {
    "beam_current_mA":      (115.0, 128.0),
    "temperature_C":        (17.0,  21.0),
    "vacuum_pressure_mbar": (0.0,   2.0e-8),
    "magnet_field_T":       (8.32,  8.36),
}


# ---------------------------------------------------------------------------
# Data layer
# ---------------------------------------------------------------------------

class DataSource:
    """Abstract-ish base.  Subclasses implement next_value()."""

    def next_value(self) -> float:
        raise NotImplementedError


class SimulatedSource(DataSource):
    """Sine wave + gaussian noise — mimics a slowly drifting beam current."""

    def __init__(self, channel: str):
        self.channel = channel
        self._tick = 0
        # Reasonable centre values per channel
        self._centres = {
            "beam_current_mA":      122.0,
            "temperature_C":        19.0,
            "vacuum_pressure_mbar": 1.2e-8,
            "magnet_field_T":       8.336,
        }
        self._amplitudes = {
            "beam_current_mA":      3.5,
            "temperature_C":        0.8,
            "vacuum_pressure_mbar": 2e-9,
            "magnet_field_T":       0.008,
        }

    def next_value(self) -> float:
        centre    = self._centres.get(self.channel, 1.0)
        amplitude = self._amplitudes.get(self.channel, 0.1)
        noise     = random.gauss(0, amplitude * 0.15)
        value     = centre + amplitude * math.sin(self._tick * 0.25) + noise
        self._tick += 1
        return value


class CsvSource(DataSource):
    """Streams rows from a CSV file, looping when exhausted."""

    def __init__(self, filepath: str, channel: str):
        self.channel = channel
        self._rows: list[float] = []
        self._index = 0
        self._load(filepath)

    def _load(self, filepath: str):
        with open(filepath, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if self.channel in row:
                    try:
                        self._rows.append(float(row[self.channel]))
                    except ValueError:
                        pass

    def next_value(self) -> float:
        if not self._rows:
            return 0.0
        value = self._rows[self._index % len(self._rows)]
        self._index += 1
        return value


# ---------------------------------------------------------------------------
# Main application
# ---------------------------------------------------------------------------

class InstrumentMonitor(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title(WINDOW_TITLE)
        self.geometry(WINDOW_SIZE)
        self.configure(bg=BG_DARK)

        # Apply ttk theme — 'clam' is the most customisable built-in
        style = ttk.Style(self)
        style.theme_use("clam")
        self._apply_styles(style)

        # Reactive state variables (StringVar / IntVar bind to widgets)
        self.source_var   = tk.StringVar(value="Simulated")
        self.channel_var  = tk.StringVar(value=CHANNELS[0])
        self.interval_var = tk.IntVar(value=UPDATE_MS)
        self.running      = False
        self._after_id    = None

        # Data
        self._source: DataSource | None = None
        self._xdata: list[float] = []
        self._ydata: list[float] = []
        self._csv_path: str | None = None

        self._build_ui()

    # ------------------------------------------------------------------
    # UI construction
    # ------------------------------------------------------------------

    def _build_ui(self):
        # ── top control bar ──────────────────────────────────────────
        ctrl = ttk.Frame(self, style="Dark.TFrame", padding=(10, 8))
        ctrl.grid(row=0, column=0, sticky="ew")
        self.columnconfigure(0, weight=1)

        ttk.Label(ctrl, text="Source:", style="Dark.TLabel").grid(row=0, column=0, padx=(0, 4))
        src_combo = ttk.Combobox(
            ctrl, textvariable=self.source_var,
            values=["Simulated", "CSV File"], width=12, state="readonly"
        )
        src_combo.grid(row=0, column=1, padx=(0, 8))
        src_combo.bind("<<ComboboxSelected>>", self._on_source_change)

        self.csv_btn = ttk.Button(ctrl, text="Browse CSV…", command=self._browse_csv, state="disabled")
        self.csv_btn.grid(row=0, column=2, padx=(0, 16))

        ttk.Label(ctrl, text="Channel:", style="Dark.TLabel").grid(row=0, column=3, padx=(0, 4))
        ch_combo = ttk.Combobox(
            ctrl, textvariable=self.channel_var,
            values=CHANNELS, width=22, state="readonly"
        )
        ch_combo.grid(row=0, column=4, padx=(0, 16))
        ch_combo.bind("<<ComboboxSelected>>", self._on_channel_change)

        ttk.Label(ctrl, text="Interval (ms):", style="Dark.TLabel").grid(row=0, column=5, padx=(0, 4))
        ttk.Spinbox(
            ctrl, from_=100, to=2000, increment=100,
            textvariable=self.interval_var, width=7
        ).grid(row=0, column=6, padx=(0, 16))

        self.start_btn = ttk.Button(ctrl, text="▶  Start", command=self._start, style="Accent.TButton")
        self.start_btn.grid(row=0, column=7, padx=(0, 4))

        self.stop_btn = ttk.Button(ctrl, text="■  Stop", command=self._stop, state="disabled")
        self.stop_btn.grid(row=0, column=8, padx=(0, 0))

        # ── plot area ─────────────────────────────────────────────────
        plot_frame = ttk.Frame(self, style="Dark.TFrame")
        plot_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=(6, 4))
        self.rowconfigure(1, weight=1)

        self._fig, self._ax = plt.subplots(figsize=(10, 4.5))
        self._fig.patch.set_facecolor(BG_DARK)
        self._ax.set_facecolor(BG_MID)
        self._ax.tick_params(colors=FG_LIGHT)
        for spine in self._ax.spines.values():
            spine.set_edgecolor("#44475a")
        self._line, = self._ax.plot([], [], color="#89b4fa", linewidth=1.8, label=self.channel_var.get())
        self._ax.set_xlabel("Sample", color=FG_LIGHT)
        self._ax.set_ylabel(self.channel_var.get(), color=FG_LIGHT)
        self._ax.legend(facecolor=BG_MID, labelcolor=FG_LIGHT)

        # Threshold lines (drawn once, updated on channel change)
        self._thresh_lines = [
            self._ax.axhline(0, color="#f38ba8", linewidth=1, linestyle="--", alpha=0.6),
            self._ax.axhline(0, color="#f38ba8", linewidth=1, linestyle="--", alpha=0.6),
        ]
        self._update_thresholds()

        self._canvas = FigureCanvasTkAgg(self._fig, master=plot_frame)
        self._canvas.draw()
        self._canvas.get_tk_widget().pack(fill="both", expand=True)

        # matplotlib toolbar (zoom, pan, save — free!) 
        toolbar_frame = ttk.Frame(plot_frame, style="Dark.TFrame")
        toolbar_frame.pack(fill="x")
        NavigationToolbar2Tk(self._canvas, toolbar_frame)

        # ── status bar ────────────────────────────────────────────────
        status = ttk.Frame(self, style="Dark.TFrame", padding=(10, 4))
        status.grid(row=2, column=0, sticky="ew")

        ttk.Label(status, text="Last value:", style="Dark.TLabel").grid(row=0, column=0, padx=(0, 4))
        self._value_var = tk.StringVar(value="—")
        ttk.Label(status, textvariable=self._value_var, width=18, style="Dark.TLabel").grid(row=0, column=1, padx=(0, 20))

        ttk.Label(status, text="Samples:", style="Dark.TLabel").grid(row=0, column=2, padx=(0, 4))
        self._count_var = tk.StringVar(value="0")
        ttk.Label(status, textvariable=self._count_var, width=8, style="Dark.TLabel").grid(row=0, column=3, padx=(0, 20))

        ttk.Label(status, text="Status:", style="Dark.TLabel").grid(row=0, column=4, padx=(0, 4))
        self._alert_var = tk.StringVar(value="IDLE")
        self._alert_label = ttk.Label(status, textvariable=self._alert_var, style="Dark.TLabel")
        self._alert_label.grid(row=0, column=5)

    # ------------------------------------------------------------------
    # Styling
    # ------------------------------------------------------------------

    def _apply_styles(self, style: ttk.Style):
        style.configure("Dark.TFrame",  background=BG_DARK)
        style.configure("Dark.TLabel",  background=BG_DARK, foreground=FG_LIGHT)
        style.configure("TCombobox",    fieldbackground=BG_MID, background=BG_MID, foreground=FG_LIGHT)
        style.configure("TSpinbox",     fieldbackground=BG_MID, background=BG_MID, foreground=FG_LIGHT)
        style.configure("TButton",      background=BG_MID, foreground=FG_LIGHT)
        style.configure("Accent.TButton", background="#313244", foreground="#89b4fa")
        style.map("Accent.TButton", background=[("active", "#45475a")])

    # ------------------------------------------------------------------
    # Event handlers
    # ------------------------------------------------------------------

    def _on_source_change(self, _event=None):
        is_csv = self.source_var.get() == "CSV File"
        self.csv_btn.configure(state="normal" if is_csv else "disabled")
        self._stop()
        self._source = None

    def _on_channel_change(self, _event=None):
        self._stop()
        self._xdata.clear()
        self._ydata.clear()
        self._source = None
        ch = self.channel_var.get()
        self._ax.set_ylabel(ch, color=FG_LIGHT)
        self._line.set_label(ch)
        self._ax.legend(facecolor=BG_MID, labelcolor=FG_LIGHT)
        self._update_thresholds()
        self._canvas.draw()

    def _browse_csv(self):
        path = filedialog.askopenfilename(
            title="Select sensor CSV",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        if path:
            self._csv_path = path
            self._source = None  # force re-init on next start

    # ------------------------------------------------------------------
    # Start / stop
    # ------------------------------------------------------------------

    def _start(self):
        if self.running:
            return
        channel = self.channel_var.get()
        if self.source_var.get() == "CSV File":
            if not self._csv_path:
                self._alert_var.set("No CSV loaded")
                return
            self._source = CsvSource(self._csv_path, channel)
        else:
            self._source = SimulatedSource(channel)

        self.running = True
        self.start_btn.configure(state="disabled")
        self.stop_btn.configure(state="normal")
        self._schedule_update()

    def _stop(self):
        self.running = False
        if self._after_id:
            self.after_cancel(self._after_id)
            self._after_id = None
        self.start_btn.configure(state="normal")
        self.stop_btn.configure(state="disabled")
        self._alert_var.set("STOPPED")
        self._alert_label.configure(foreground=FG_LIGHT)

    # ------------------------------------------------------------------
    # Periodic update via after()
    # ------------------------------------------------------------------

    def _schedule_update(self):
        """Register the next tick without blocking the event loop."""
        interval = max(100, self.interval_var.get())
        self._after_id = self.after(interval, self._tick)

    def _tick(self):
        if not self.running:
            return
        value = self._source.next_value()

        # Rolling window
        sample_n = len(self._xdata)
        self._xdata.append(sample_n)
        self._ydata.append(value)
        if len(self._xdata) > MAX_POINTS:
            self._xdata.pop(0)
            self._ydata.pop(0)

        # Update plot data
        self._line.set_data(range(len(self._ydata)), self._ydata)
        self._ax.relim()
        self._ax.autoscale_view()
        self._canvas.draw_idle()  # draw_idle is cheaper than draw()

        # Update status bar
        self._value_var.set(f"{value:.4g}  ({self.channel_var.get().split('_')[-1]})")
        self._count_var.set(str(sample_n + 1))
        self._check_threshold(value)

        self._schedule_update()

    # ------------------------------------------------------------------
    # Thresholds & alerting
    # ------------------------------------------------------------------

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
            self._alert_var.set("⚠  OUT OF RANGE")
            self._alert_label.configure(foreground=ALERT_COLOUR)
        else:
            self._alert_var.set("✓  NOMINAL")
            self._alert_label.configure(foreground=NORMAL_COLOUR)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    app = InstrumentMonitor()
    app.mainloop()
