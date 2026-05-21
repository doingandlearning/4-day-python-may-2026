# 1. Single-process version

Start simple.

This establishes:

* functions
* timing
* sequential CPU-bound work

```python
import time

def analyse_batch(batch_id, readings):
    print(f"Batch {batch_id}: starting")
    total = sum(x ** 2 for x in readings)
    print(f"Batch {batch_id}: result = {total}")
    return total

batches = {
    "alpha": range(1, 500_000),
    "beta":  range(1, 500_000),
    "gamma": range(1, 500_000),
}

start = time.perf_counter()

for batch_id, readings in batches.items():
    analyse_batch(batch_id, readings)

elapsed = time.perf_counter() - start
print(f"All done in {elapsed:.2f}s")
```

## What students observe

The batches run one after another:

```text
Batch alpha: starting
Batch alpha: result = ...
Batch beta: starting
Batch beta: result = ...
Batch gamma: starting
Batch gamma: result = ...
All done in ~1.8s
```

Nothing overlaps. Total time is the sum of all three.

---

# 2. Naïve threads (and why they don't help here)

Show threads first — and show that they barely improve things.

This is the GIL teaching moment.

```python
import time
from threading import Thread

def analyse_batch(batch_id, readings):
    print(f"Batch {batch_id}: starting")
    total = sum(x ** 2 for x in readings)
    print(f"Batch {batch_id}: result = {total}")

batches = {
    "alpha": range(1, 500_000),
    "beta":  range(1, 500_000),
    "gamma": range(1, 500_000),
}

start = time.perf_counter()

threads = [
    Thread(target=analyse_batch, args=(batch_id, readings))
    for batch_id, readings in batches.items()
]

for t in threads:
    t.start()

for t in threads:
    t.join()

elapsed = time.perf_counter() - start
print(f"All done in {elapsed:.2f}s")
```

## What students observe

The time barely improves — possibly gets worse:

```text
All done in ~1.9s
```

## The teaching point

Threads share the same interpreter.
For CPU-bound work, the GIL means only one thread runs Python bytecode at a time.
Concurrency here is not the same as parallelism.

Threads are the right tool when work is I/O-bound (waiting on network, disk, sensors).
For CPU-bound work, you need separate processes.

---

# 3. First processes

Now replace threads with processes.

```python
import time
from multiprocessing import Process

def analyse_batch(batch_id, readings):
    print(f"Batch {batch_id}: starting")
    total = sum(x ** 2 for x in readings)
    print(f"Batch {batch_id}: result = {total}")

if __name__ == "__main__":
    batches = {
        "alpha": range(1, 500_000),
        "beta":  range(1, 500_000),
        "gamma": range(1, 500_000),
    }

    start = time.perf_counter()

    processes = [
        Process(target=analyse_batch, args=(batch_id, readings))
        for batch_id, readings in batches.items()
    ]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    elapsed = time.perf_counter() - start
    print(f"All done in {elapsed:.2f}s")
```

## New concepts

### `Process`

```python
Process(target=analyse_batch, args=("alpha", readings))
```

Same API shape as `Thread` — `start()`, `join()`, `is_alive()`.

### `if __name__ == "__main__":`

Required on Windows and with `spawn` start method.
The parent module is re-imported in each child — this guard prevents infinite spawning.

## What students observe

Time drops to roughly one batch's worth:

```text
All done in ~0.7s
```

Each process has its own interpreter — no GIL contention.

---

# 4. The isolation problem

Now show that processes do NOT share memory.

This is the most important conceptual difference from threads.

```python
import time
from multiprocessing import Process

results = {}

def analyse_batch(batch_id, readings):
    total = sum(x ** 2 for x in readings)
    results[batch_id] = total     # writing to a shared dict
    print(f"Batch {batch_id}: wrote result")

if __name__ == "__main__":
    batches = {
        "alpha": range(1, 500_000),
        "beta":  range(1, 500_000),
        "gamma": range(1, 500_000),
    }

    processes = [
        Process(target=analyse_batch, args=(batch_id, readings))
        for batch_id, readings in batches.items()
    ]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print("Results in main process:", results)
```

## What students observe

```text
Batch alpha: wrote result
Batch beta: wrote result
Batch gamma: wrote result
Results in main process: {}
```

The dictionary in the main process is empty.
Each child process has its own copy of `results`.
Writes in children never reach the parent.

## The teaching point

```text
Threads → shared memory, coordination needed
Processes → isolated memory, communication needed
```

This is the fork in the road between the two models.

---

# 5. Returning results with Queue

Now teach inter-process communication.

```python
import time
from multiprocessing import Process, Queue

def analyse_batch(batch_id, readings, result_queue):
    total = sum(x ** 2 for x in readings)
    result_queue.put((batch_id, total))

if __name__ == "__main__":
    batches = {
        "alpha": range(1, 500_000),
        "beta":  range(1, 500_000),
        "gamma": range(1, 500_000),
    }

    result_queue = Queue()

    processes = [
        Process(target=analyse_batch, args=(batch_id, readings, result_queue))
        for batch_id, readings in batches.items()
    ]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    results = {}
    while not result_queue.empty():
        batch_id, total = result_queue.get()
        results[batch_id] = total

    print("Results:", results)
```

## New concepts

### `multiprocessing.Queue`

Unlike `threading.Queue`, this one works across process boundaries.
Uses OS-level IPC (pipes) under the hood — data is serialised between processes.

### Serialisation cost

Only picklable objects can travel through the Queue.
Simple types (numbers, strings, tuples) are fine.
Complex custom objects may need extra care.

---

# 6. Pool — the professional approach

Creating and managing individual processes is low-level.
For the common case of "apply a function to many inputs", use `Pool`.

```python
import time
from multiprocessing import Pool

def analyse_batch(args):
    batch_id, readings = args
    total = sum(x ** 2 for x in readings)
    return batch_id, total

if __name__ == "__main__":
    batches = [
        ("alpha", range(1, 500_000)),
        ("beta",  range(1, 500_000)),
        ("gamma", range(1, 500_000)),
    ]

    start = time.perf_counter()

    with Pool() as pool:
        results = pool.map(analyse_batch, batches)

    elapsed = time.perf_counter() - start
    print(f"All done in {elapsed:.2f}s")
    print(dict(results))
```

## New concepts

### `Pool()`

With no argument, uses one worker process per CPU core.
The pool is reused across tasks — no spawn overhead per call.

### `pool.map(func, iterable)`

Distributes items across the pool and collects results in order.
Blocking — returns when all tasks are complete.

### Context manager

```python
with Pool() as pool:
```

Ensures processes are cleaned up correctly when done.

## What students observe

Same speed improvement as manual processes, with much less boilerplate.

---

# 7. Pool with starmap — cleaner arguments

`map` requires a single argument per call.
`starmap` unpacks tuples, which reads more naturally.

```python
from multiprocessing import Pool
import time

def analyse_batch(batch_id, readings):
    total = sum(x ** 2 for x in readings)
    return batch_id, total

if __name__ == "__main__":
    batches = [
        ("alpha", range(1, 500_000)),
        ("beta",  range(1, 500_000)),
        ("gamma", range(1, 500_000)),
    ]

    start = time.perf_counter()

    with Pool() as pool:
        results = pool.starmap(analyse_batch, batches)

    elapsed = time.perf_counter() - start
    print(f"All done in {elapsed:.2f}s")
    print(dict(results))
```

## New concept

### `pool.starmap(func, iterable)`

Each item in `iterable` is unpacked as positional arguments.
`analyse_batch` now has a natural signature again — no wrapper needed.

---

# 8. Advanced direction (next topics)

From here you can naturally teach:

## `ProcessPoolExecutor`

Higher-level API, mirrors `ThreadPoolExecutor`.

```python
from concurrent.futures import ProcessPoolExecutor
```

Enables mixing threads and processes under one unified interface.

---

## `pool.imap` and `pool.imap_unordered`

Stream results as they complete rather than waiting for all of them.
`imap_unordered` is faster when order does not matter.

---

## Shared memory (`multiprocessing.shared_memory`)

For large arrays (NumPy), copying through Queue is expensive.
Shared memory lets processes read the same buffer without serialisation.
Particularly relevant for scientific computing pipelines.

---

## `multiprocessing.Value` and `Array`

Typed shared state with built-in locking.
Lower-level than shared memory but simpler for scalars and small arrays.

---

# The most important conceptual progression

```text
Sequential execution
    ↓
Threads — concurrent but GIL-limited for CPU work
    ↓
Processes — true parallelism, isolated memory
    ↓
Memory isolation problem
    ↓
IPC with Queue
    ↓
Pool — automatic work distribution
    ↓
Higher-level executors (ProcessPoolExecutor)
    ↓
Shared memory for large data
```

---

# Threading vs processes — the one-slide summary

| | Threads | Processes |
|---|---|---|
| Memory | Shared | Isolated |
| GIL | Yes (standard Python) | No |
| Communication | Shared state + Lock | Queue / Pipe / shared memory |
| Startup cost | Low | Higher |
| Best for | I/O-bound work | CPU-bound work |
| Failure isolation | One crash can affect all | Processes are independent |