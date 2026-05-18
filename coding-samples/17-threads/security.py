# security_unit.py
from __future__ import annotations
import threading, queue, time, csv, random
from dataclasses import dataclass, field
from typing import Literal, TypedDict

EventType = Literal["door", "motion", "cmd"]
class Event(TypedDict):
    type: EventType
    value: object
    t: float

@dataclass
class Config:
    armed: bool = False
    max_pin_attempts: int = 3
    failed_pin_attempts: int = 0
    lock: threading.Lock = field(default_factory=threading.Lock)  # protects fields above

running = True
events: "queue.Queue[Event]" = queue.Queue(maxsize=256)
config = Config()

def log_line(path: str, row: list[object]) -> None:
    # Minimal, safe CSV append
    with open(path, "a", newline="") as f:
        csv.writer(f).writerow(row)

def door_sensor():
    """Simulate door contact: 'open' or 'closed' bursts."""
    try:
        state = "closed"
        while running:
            time.sleep(random.uniform(0.5, 2.0))
            state = "open" if state == "closed" else "closed"
            events.put({"type": "door", "value": state, "t": time.time()}, timeout=1)
    except Exception as e:
        print(f"[door] fatal: {e!r}")
    finally:
        print("[door] stopping")

def motion_sensor():
    """Simulate motion spikes True/False."""
    try:
        detected = False
        while running:
            time.sleep(0.3)
            # Randomly flip motion (biased towards False)
            detected = random.random() < 0.25
            events.put({"type": "motion", "value": detected, "t": time.time()}, timeout=1)
    except Exception as e:
        print(f"[motion] fatal: {e!r}")
    finally:
        print("[motion] stopping")

def processor(log_path: str = "events_log.csv"):
    """Consume events; raise alarm if armed and suspicious activity occurs."""
    # Simple rule: if ARMED and (door opens OR motion True), alarm.
    alarm = False
    try:
        # header
        log_line(log_path, ["t", "type", "value", "armed", "alarm"])
        while running or not events.empty():
            try:
                ev = events.get(timeout=0.5)
            except queue.Empty:
                continue

            # Read/modify shared config under lock
            if ev["type"] == "cmd":
                val = ev["value"]
                with config.lock:
                    if val == "arm":
                        config.armed = True
                    elif val == "disarm":
                        config.armed = False
                print(f"[processor] CMD -> {val}")

            elif ev["type"] in ("door", "motion"):
                # snapshot armed state atomically
                with config.lock:
                    armed_now = config.armed

                # rule evaluation
                if armed_now and (
                    (ev["type"] == "door" and ev["value"] == "open") or
                    (ev["type"] == "motion" and ev["value"] is True)
                ):
                    alarm = True
                # log every event
                log_line(log_path, [ev["t"], ev["type"], ev["value"], armed_now, alarm])
                if alarm:
                    print(f"[ALARM] Event: {ev['type']} -> {ev['value']} (armed={armed_now})")
            else:
                print(f"[processor] Unknown event: {ev}")

            events.task_done()
    except Exception as e:
        print(f"[processor] fatal: {e!r}")
    else:
        print("[processor] clean loop exit")
    finally:
        print("[processor] stopping")

def commander():
    """Issue arm/disarm commands on a timer (pretend keypad/policy)."""
    try:
        while running:
            time.sleep(3.0)
            events.put({"type": "cmd", "value": "arm", "t": time.time()}, timeout=1)
            time.sleep(4.0)
            events.put({"type": "cmd", "value": "disarm", "t": time.time()}, timeout=1)
    except Exception as e:
        print(f"[cmd] fatal: {e!r}")
    finally:
        print("[cmd] stopping")

if __name__ == "__main__":
    threads = [
        threading.Thread(target=door_sensor, name="door", daemon=True),
        threading.Thread(target=motion_sensor, name="motion", daemon=True),
        threading.Thread(target=processor, name="processor", daemon=False),  # keep alive
        threading.Thread(target=commander, name="commander", daemon=True),
    ]
    for t in threads: t.start()

    try:
        time.sleep(10)  # run for a bit
    finally:
        # guarantee shutdown
        running = False
        for t in threads:
            if t is not threading.current_thread():
                t.join(timeout=2)
        print("Shutdown complete.")
