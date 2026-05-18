"""
Exercise 5: Thread Synchronization with Locks
=============================================

This exercise introduces thread synchronization using locks to protect
shared resources, similar to the security.py example but simplified.

Learning Objectives:
- Use locks to protect shared data
- Understand thread safety
- Prevent race conditions
- Implement thread-safe logging

Task: Add thread-safe logging and shared state management to the
security system.
"""

import threading
import time
import random
from datetime import datetime

# Shared data and locks
log_lock = threading.Lock()
state_lock = threading.Lock()
security_state = {
    "armed": False,
    "alarm_triggered": False,
    "last_activity": None
}

def log_event(event_type, message):
    """
    Thread-safe logging function.
    """
    timestamp = datetime.now().strftime("%H:%M:%S")
    log_entry = f"[{timestamp}] {event_type}: {message}"
    
    # TODO: Use the log_lock to protect file writing
    with log_lock:
        print(log_entry)  # In real app, this would write to file
        # Simulate file writing delay
        time.sleep(0.1)

def update_security_state(key, value):
    """
    Thread-safe function to update shared security state.
    """
    # TODO: Use state_lock to protect shared state updates
    with state_lock:
        security_state[key] = value
        log_event("STATE", f"Updated {key} to {value}")

def door_sensor(sensor_id):
    """
    Door sensor with thread-safe logging.
    """
    log_event("SENSOR", f"{sensor_id} activated")
    
    for i in range(5):
        time.sleep(random.randint(2, 4))
        door_state = random.choice(["OPEN", "CLOSED"])
        
        # TODO: Log the door event thread-safely
        log_event("DOOR", f"{sensor_id} detected door {door_state}")
        
        # TODO: Update shared state if door opens
        if door_state == "OPEN":
            update_security_state("last_activity", f"Door {sensor_id} opened")
            
            # TODO: Check if system is armed and trigger alarm
            with state_lock:
                if security_state["armed"] and not security_state["alarm_triggered"]:
                    update_security_state("alarm_triggered", True)
                    log_event("ALARM", "Door opened while system armed!")
    
    log_event("SENSOR", f"{sensor_id} deactivated")

def motion_sensor(sensor_id):
    """
    Motion sensor with thread-safe logging.
    """
    log_event("SENSOR", f"{sensor_id} activated")
    
    for i in range(6):
        time.sleep(random.randint(1, 3))
        motion_detected = random.random() < 0.4
        
        if motion_detected:
            # TODO: Log motion detection thread-safely
            log_event("MOTION", f"{sensor_id} detected motion")
            
            # TODO: Update shared state
            update_security_state("last_activity", f"Motion detected by {sensor_id}")
            
            # TODO: Check if system is armed and trigger alarm
            with state_lock:
                if security_state["armed"] and not security_state["alarm_triggered"]:
                    update_security_state("alarm_triggered", True)
                    log_event("ALARM", "Motion detected while system armed!")
    
    log_event("SENSOR", f"{sensor_id} deactivated")

def system_controller():
    """
    System controller that manages security state.
    """
    log_event("CONTROLLER", "Security controller activated")
    
    # TODO: Arm the system after 3 seconds
    time.sleep(3)
    update_security_state("armed", True)
    log_event("CONTROLLER", "System ARMED")
    
    # TODO: Disarm the system after 10 seconds
    time.sleep(7)
    update_security_state("armed", False)
    log_event("CONTROLLER", "System DISARMED")

def main():
    """
    Main function to demonstrate thread synchronization.
    """
    print("🔒 Security System - Thread Synchronization")
    print("=" * 50)
    
    # TODO: Create and start all threads
    door_thread = threading.Thread(target=door_sensor, args=("DOOR-001",))
    motion_thread = threading.Thread(target=motion_sensor, args=("MOTION-001",))
    controller_thread = threading.Thread(target=system_controller)
    
    door_thread.start()
    motion_thread.start()
    controller_thread.start()
    
    # TODO: Wait for all threads to complete
    door_thread.join()
    motion_thread.join()
    controller_thread.join()
    
    # TODO: Print final security state
    with state_lock:
        print(f"\n📊 Final Security State:")
        for key, value in security_state.items():
            print(f"  {key}: {value}")
    
    print("\n🏁 Thread synchronization demonstration complete!")

if __name__ == "__main__":
    main()
