# 1. Single-threaded version

Start simple.

This establishes:

* functions
* timing
* sequential execution

```python
from time import sleep
import random

def door_sensor(sensor_id):
    for _ in range(5):
        sleep(2)

        state = random.choice(["open", "closed"])

        print(f"{sensor_id}: {state}")

door_sensor("front")
door_sensor("back")
door_sensor("side")

print("All done.")
```

## What students observe

The sensors run one after another:

```text
front ...
front ...
front ...
back ...
back ...
side ...
```

Nothing overlaps.

---

# 2. First threads

Now introduce concurrency.

```python
from time import sleep
import random
from threading import Thread

def door_sensor(sensor_id):
    for _ in range(5):
        sleep(2)

        state = random.choice(["open", "closed"])

        print(f"{sensor_id}: {state}")

threads = [
    Thread(target=door_sensor, args=(sensor,))
    for sensor in ["front", "back", "side"]
]

for thread in threads:
    thread.start()

print("Threads started")

for thread in threads:
    thread.join()

print("All done.")
```

---

## New concepts

### `Thread`

```python
Thread(target=door_sensor, args=("front",))
```

### `start()`

Actually launches concurrent execution.

### `join()`

Waits for completion.

---

## What students observe

Output becomes interleaved:

```text
front: open
side: closed
back: open
```

This is the first visible evidence of concurrency.

---

# 3. Shared state

Now teach communication between threads.

```python
from time import sleep
import random
from threading import Thread

current_state = {}

def door_sensor(sensor_id):
    for _ in range(5):
        sleep(2)

        state = random.choice(["open", "closed"])

        current_state[sensor_id] = state

threads = [
    Thread(target=door_sensor, args=(sensor,))
    for sensor in ["front", "back", "side"]
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(current_state)
```

---

## New concept

Threads can share memory.

This is one of the most important differences between:

* threading
* multiprocessing

---

# 4. Add a monitoring thread

Now create a separate observer thread.

```python
from time import sleep
import random
from threading import Thread

current_state = {}

def door_sensor(sensor_id):
    for _ in range(5):
        sleep(2)

        state = random.choice(["open", "closed"])
        current_state[sensor_id] = state

def monitor():
    while True:
        sleep(1)

        print(current_state)

threads = [
    Thread(target=door_sensor, args=(sensor,))
    for sensor in ["front", "back", "side"]
]

monitor_thread = Thread(target=monitor, daemon=True)

for thread in threads:
    thread.start()

monitor_thread.start()

for thread in threads:
    thread.join()

print("All done.")
```

---

## New concepts

### Daemon threads

```python
daemon=True
```

The monitor automatically dies when the program exits.

---

# 5. Introduce race conditions

Now explain:

> Multiple threads are reading/writing the same data simultaneously.

This is unsafe:

```python
current_state[sensor_id] = state
```

and:

```python
print(current_state)
```

happen concurrently.

This is where synchronization enters.

---

# 6. Add a Lock

Now teach thread safety.

```python
from time import sleep
import random
from threading import Thread, Lock

current_state = {}
state_lock = Lock()

def door_sensor(sensor_id):
    for _ in range(5):
        sleep(2)

        state = random.choice(["open", "closed"])

        with state_lock:
            current_state[sensor_id] = state

def monitor():
    while True:
        sleep(1)

        with state_lock:
            print(current_state)

threads = [
    Thread(target=door_sensor, args=(sensor,))
    for sensor in ["front", "back", "side"]
]

monitor_thread = Thread(target=monitor, daemon=True)

for thread in threads:
    thread.start()

monitor_thread.start()

for thread in threads:
    thread.join()

print("All done.")
```

---

## New concepts

### Critical section

```python
with state_lock:
```

Only one thread can enter at a time.

---

## Important teaching moment

Without locks:

* corrupted state
* inconsistent reads
* race conditions

With locks:

* synchronization
* safety
* predictability

---

# 7. Graceful shutdown with Event

Now remove the daemon shortcut.

Teach cooperative signaling.

```python
from time import sleep
import random
from threading import Thread, Lock, Event

current_state = {}
state_lock = Lock()

stop_event = Event()

def door_sensor(sensor_id):
    for _ in range(5):
        sleep(2)

        state = random.choice(["open", "closed"])

        with state_lock:
            current_state[sensor_id] = state

def monitor():
    while not stop_event.is_set():
        sleep(1)

        with state_lock:
            print(current_state)

threads = [
    Thread(target=door_sensor, args=(sensor,))
    for sensor in ["front", "back", "side"]
]

monitor_thread = Thread(target=monitor)

for thread in threads:
    thread.start()

monitor_thread.start()

for thread in threads:
    thread.join()

stop_event.set()

monitor_thread.join()

print("All done.")
```

---

## New concepts

### `Event`

A thread-safe signaling mechanism.

### Cooperative cancellation

Threads check:

```python
stop_event.is_set()
```

---

# 8. Producer-consumer with Queue

Now introduce the professional approach.

Instead of shared dictionaries, use message passing.

```python
from time import sleep
import random
from threading import Thread
from queue import Queue

events = Queue()

def door_sensor(sensor_id):
    for _ in range(5):
        sleep(random.uniform(1, 3))

        state = random.choice(["open", "closed"])

        events.put((sensor_id, state))

def monitor():
    while True:
        sensor, state = events.get()

        print(f"{sensor}: {state}")

        events.task_done()

threads = [
    Thread(target=door_sensor, args=(sensor,))
    for sensor in ["front", "back", "side"]
]

monitor_thread = Thread(target=monitor, daemon=True)

for thread in threads:
    thread.start()

monitor_thread.start()

for thread in threads:
    thread.join()

events.join()

print("All done.")
```

---

# Why Queue is important

This teaches:

## Shared-state threading

Earlier approach:

* harder
* lock-heavy
* race conditions

## Message-passing threading

Queue approach:

* safer
* cleaner
* scalable
* common in production systems

---

# 9. Advanced direction (next topics)

From here you can naturally teach:

## ThreadPoolExecutor

Higher-level threading.

```python
from concurrent.futures import ThreadPoolExecutor
```

---

## Deadlocks

Two locks waiting on each other.

---

## Semaphores

Limit concurrent access.

---

## Condition variables

Thread coordination.

---

# The most important conceptual progression

The real educational path is:

```text
Sequential execution
    ↓
Concurrent execution
    ↓
Shared state
    ↓
Race conditions
    ↓
Synchronization
    ↓
Thread coordination
    ↓
Message passing
    ↓
High-level concurrency patterns
```

Your original example already sits around stages 4–6, which is why it’s a strong teaching sample.

