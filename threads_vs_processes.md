# Threads vs Processes in Python

A short reminder from the course (Labs 16–17). Keep this handy when you want code to run **in parallel**.

---

## The GIL in one sentence

CPython has a **Global Interpreter Lock (GIL)**: only one thread runs Python bytecode at a time in a single process.

So **multiple threads do not speed up CPU-heavy pure Python loops** — they take turns on one core.

---

## Decision table

| Workload | Use | Why |
|----------|-----|-----|
| CPU-bound pure Python (loops, math in Python) | `multiprocessing` | Separate processes, separate interpreters, true parallelism |
| CPU-bound NumPy/pandas/matplotlib (large arrays) | Often **no extra threads** — libraries already use C/Fortran and may release the GIL | Vectorise first; profile before adding concurrency |
| Waiting on disk, network, sensors, APIs | `threading` | Threads block on I/O; other threads can run |
| Many independent batch jobs | `multiprocessing.Pool` | Reuse worker processes |

---

## What you saw in the course

**Threads** (`threading.Thread`): good when work **waits** (I/O). Little gain when every thread is busy computing in Python.

**Processes** (`multiprocessing.Process`, `Pool`): separate memory, higher startup cost, but **parallel CPU** for Python-heavy work.

The weather-station and batch-analysis labs show threads helping with **overlapping waits**, and processes helping with **parallel CPU work**.

---

## Common mistakes

1. **Threading a NumPy-heavy pipeline** — usually unnecessary; optimise the array code first.
2. **Sharing mutable data between processes without care** — use queues, pipes, or pass data at startup; do not assume shared global lists “just work.”
3. **Threads + processes everywhere** — start sequential; add concurrency only when you have measured a bottleneck.
4. **No synchronization** — if threads share mutable state, use locks (see [labs/security/](labs/security/) for exercises).

---

## When in doubt

1. Make it **correct** sequentially.
2. **Measure** where time goes (`time.perf_counter()`, logging, or a profiler).
3. If CPU-bound in Python → **processes**; if I/O-bound → **threads**.

For deeper practice: [labs/security/README.md](labs/security/README.md).
