from time import sleep
import random
from threading import Thread, Event, Lock

current_state = {}

stop_event = Event()
state_lock = Lock()

test_var = "Hello"

def door_sensor(sensor_id):
    for i in range(5):
        sleep(2)
        state = random.choice([f"{i}open", f"{i}closed"])
        print(test_var)
        with state_lock:
            current_state[sensor_id] = state

def monitor():
    while not stop_event.is_set():
        sleep(1)
        with state_lock:
            print(current_state)

threads = [
    Thread(target=door_sensor, args=(door,))
    for door in ["Front door", "Back door", "Side door"]
]

monitor_thread = Thread(target=monitor)

for thread in threads:
    thread.start()

monitor_thread.start()

print("Threads started")

sleep(3)
test_var = "I have been changed"

for thread in threads:
    thread.join()

stop_event.set()
monitor_thread.join()

print("Threads finished")