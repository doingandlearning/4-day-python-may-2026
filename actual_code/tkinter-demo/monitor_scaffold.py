"""
CERN Instrument Monitor — SCAFFOLD VERSION
==========================================
This is the starting point for the live-coding demo.
Students see this first; the full version is revealed afterwards.

Patterns to introduce:
  - tk.Tk() and mainloop()
  - ttk widgets and theming
  - Frame-based layout with grid
  - Embedding matplotlib in tkinter
  - after() for periodic callbacks (the event loop trick)
  - StringVar / IntVar for reactive UI state
  - filedialog for file picking

To run:
    pip install matplotlib
    python monitor_scaffold.py
"""

import tkinter as tk
from tkinter import ttk


def main():
    root = tk.Tk()
    root.title("CERN Instrument Monitor")
    root.geometry("900x600")

    # --- YOUR CODE GOES HERE ---
    # Hint: think about three regions:
    #   1. A top control bar (data source, channel selector, start/stop)
    #   2. A central plot area (matplotlib figure embedded here)
    #   3. A bottom status bar (last value, timestamp, alert indicator)

    label = ttk.Label(root, text="Ready to build the monitor...")
    label.pack(expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()
