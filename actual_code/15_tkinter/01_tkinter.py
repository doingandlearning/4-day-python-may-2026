import tkinter as tk
from tkinter import ttk

class InstrumentMonitor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BEST INSTRUMENT MONITOR")
        self.geometry("900x600")

        style = ttk.Style()
        style.theme_use("clam")  # clam, basic, alt ... default

        self._build_controls()
        self.source_var = tk.StringVar(value="Simulated")
        self.channel_var = tk.StringVar(value="beam_current_mA")
        self.interval_var = tk.IntVar(value=500)
        self.status_var = tk.StringVar(value="IDLE")

    def _build_controls(self):
        ctrl = ttk.Frame(self, padding=(10, 8))
        ctrl.grid(row=0, column=0, sticky="ew")
        self.columnconfigure(0, weight=1)

        ttk.Label(ctrl, text="Source:").grid(row=0, column=0, padx=(0, 4))
        ttk.Combobox(
            ctrl, textvariable=self.source_var, values=["Simulated", "CSV File"], width=12, state="readonly"
        ).grid(row=0, column=1, padx=(0, 8))

        ttk.Button(ctrl, text="Browse CSV…", state="disabled").grid(
            row=0, column=2, padx=(0, 16)
        )

        ttk.Label(ctrl, text="Channel:").grid(row=0, column=3, padx=(0, 4))
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

        ttk.Label(ctrl, text="Interval (ms):").grid(row=0, column=5, padx=(0, 4))
        ttk.Spinbox(ctrl, textvariable=self.interval_var, from_=100, to=2000, increment=100, width=7).grid(
            row=0, column=6, padx=(0, 16)
        )

        ttk.Button(ctrl, text="▶  Start").grid(row=0, column=7, padx=(0, 4))
        ttk.Button(ctrl, text="■  Stop", state="disabled").grid(row=0, column=8)

        status = ttk.Frame(self, padding=(10, 4))
        status.grid(row=2, column=0, sticky="ew")

        ttk.Label(status, text="Status:").grid(row=0, column=0, padx=(0, 4))
        ttk.Label(status, textvariable=self.status_var).grid(row=0, column=1)

if __name__ == "__main__":
    app = InstrumentMonitor()
    app.mainloop()