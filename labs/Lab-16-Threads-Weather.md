# Lab 16: Multi-Threaded Weather Station Simulator

This lab focuses on running multiple sensor readers concurrently with Python threading.

You will practise:

- creating threads that call a shared function with different arguments
- simulating irregular sensor timing with `sleep` and `random`
- using `Timer` for periodic alerts
- seeing interleaved output from concurrent threads

---

## Hints and Tips

- Pass sensor settings as arguments to `sensor_reader` instead of duplicating code.
- Call `thread.start()` on each thread, then `thread.join()` if you need to wait for completion.
- `random.randint(1, max_interval)` gives a delay between 1 and `max_interval` seconds.
- `threading.Timer(seconds, function)` runs `function` once after a delay.
- For repeating alerts, schedule the next timer from inside the alert function.

---

## Task 1: Complete the Sensor Reader

Complete this function:

`sensor_reader(sensor_name, sensor_unit, max_interval, readings_count=10)`

Rules:

1. Loop `readings_count` times.
2. Sleep a random number of seconds between 1 and `max_interval`.
3. Generate a random reading (0–100 is fine) and print: `[Temperature] Reading #1: 23 °C`.
4. Test by calling the function directly once before starting threads.

<details>
<summary>Solution (Task 1)</summary>

```python
import random
import time


def sensor_reader(sensor_name, sensor_unit, max_interval, readings_count=10):
    for i in range(1, readings_count + 1):
        sleep_time = random.randint(1, max_interval)
        time.sleep(sleep_time)
        reading_value = random.randint(0, 100)
        print(f"[{sensor_name}] Reading #{i}: {reading_value} {sensor_unit}")


sensor_reader("Temperature", "°C", 3, readings_count=3)
```

</details>

---

## Task 2: Run Five Sensor Threads

Create and start one thread per sensor:

| Sensor     | Unit  | Max interval (seconds) |
|------------|-------|-------------------------|
| Temperature| °C    | 3                       |
| Humidity   | %     | 5                       |
| Pressure   | hPa   | 7                       |
| Wind Speed | km/h  | 4                       |
| Rainfall   | mm    | 8                       |

Rules:

1. Use `threading.Thread` with `target=sensor_reader` and a tuple of arguments.
2. Take 5 readings per sensor (`readings_count=5`).
3. Start all threads; use `join()` on each so the program waits for them to finish.

<details>
<summary>Solution (Task 2)</summary>

```python
import random
import threading
import time


def sensor_reader(sensor_name, sensor_unit, max_interval, readings_count=10):
    for i in range(1, readings_count + 1):
        sleep_time = random.randint(1, max_interval)
        time.sleep(sleep_time)
        reading_value = random.randint(0, 100)
        print(f"[{sensor_name}] Reading #{i}: {reading_value} {sensor_unit}")


sensors = [
    ("Temperature", "°C", 3),
    ("Humidity", "%", 5),
    ("Pressure", "hPa", 7),
    ("Wind Speed", "km/h", 4),
    ("Rainfall", "mm", 8),
]

threads = []
for name, unit, interval in sensors:
    thread = threading.Thread(
        target=sensor_reader,
        args=(name, unit, interval),
        kwargs={"readings_count": 5},
    )
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
```

</details>

---

## Task 3: Weather Alert Timer

Write:

`weather_alert()`

Rules:

1. `weather_alert` prints: `WEATHER ALERT: Checking conditions...`
2. Use `threading.Timer(10, weather_alert)` to fire the first alert 10 seconds after start.
3. Run sensor threads alongside the timer (fewer readings per sensor is fine, e.g. 3).
4. Keep the main program alive long enough for at least one alert (e.g. `time.sleep(15)`).

<details>
<summary>Solution (Task 3)</summary>

```python
import random
import threading
import time


def sensor_reader(sensor_name, sensor_unit, max_interval, readings_count=10):
    for i in range(1, readings_count + 1):
        sleep_time = random.randint(1, max_interval)
        time.sleep(sleep_time)
        reading_value = random.randint(0, 100)
        print(f"[{sensor_name}] Reading #{i}: {reading_value} {sensor_unit}")


def weather_alert():
    print("WEATHER ALERT: Checking conditions...")


sensors = [
    ("Temperature", "°C", 2),
    ("Humidity", "%", 3),
]

threads = []
for name, unit, interval in sensors:
    thread = threading.Thread(
        target=sensor_reader,
        args=(name, unit, interval),
        kwargs={"readings_count": 3},
    )
    threads.append(thread)
    thread.start()

alert_timer = threading.Timer(10, weather_alert)
alert_timer.start()

time.sleep(15)

for thread in threads:
    thread.join()
alert_timer.cancel()
```

</details>

---

## Task 4 (Optional): Repeating Alerts and Logging

Write:

`continuous_alert()`

`log_reading(sensor_name, reading_value, logfile="weather_log.txt")`

Rules:

1. `continuous_alert` prints the alert message, then schedules itself again with `Timer(10, continuous_alert)`.
2. Call `log_reading` from inside `sensor_reader` after each reading (append one line with timestamp, sensor, value).
3. Run the station for about 30 seconds, then stop scheduling new alerts.

<details>
<summary>Solution (Task 4 Optional)</summary>

```python
import random
import threading
import time
from datetime import datetime


def log_reading(sensor_name, reading_value, logfile="weather_log.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{timestamp} | {sensor_name} | {reading_value}\n"
    with open(logfile, "a") as file:
        file.write(line)


def sensor_reader(sensor_name, sensor_unit, max_interval, readings_count=10):
    for i in range(1, readings_count + 1):
        sleep_time = random.randint(1, max_interval)
        time.sleep(sleep_time)
        reading_value = random.randint(0, 100)
        print(f"[{sensor_name}] Reading #{i}: {reading_value} {sensor_unit}")
        log_reading(sensor_name, reading_value)


def continuous_alert():
    print("WEATHER ALERT: Checking conditions...")
    timer = threading.Timer(10, continuous_alert)
    timer.daemon = True
    timer.start()


continuous_alert()

thread = threading.Thread(
    target=sensor_reader,
    args=("Temperature", "°C", 3),
    kwargs={"readings_count": 20},
)
thread.start()
time.sleep(30)
```

</details>

---

## Reflection

- Why do sensor messages appear interleaved on the console?
- What is the difference between a `Thread` and a `Timer`?
- When would logging to a file need extra care with multiple threads writing at once?
