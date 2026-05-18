"""
Exercise 1: Basic Sensor Threads
================================

This exercise introduces the fundamental concepts of threading by creating
individual sensor threads for a security system.

Learning Objectives:
- Create and start threads
- Pass arguments to thread functions
- Understand basic thread execution
- Observe thread behavior

Task: Create a basic door sensor that monitors door state changes.
"""

import threading
import time
import random

def door_sensor(sensor_id, check_interval=2):
    """
    Simulates a door sensor that checks door state periodically.
    
    Args:
        sensor_id (str): Unique identifier for this sensor
        check_interval (int): How often to check the door (seconds)
    """
    print(f"[{sensor_id}] Door sensor activated")
    
    # TODO: Complete the door monitoring loop
    for i in range(5):  # Check 5 times
        # TODO: Sleep for the check_interval
        time.sleep(check_interval)
        
        # TODO: Simulate door state (randomly open/closed)
        door_state = random.choice(["OPEN", "CLOSED"])
        
        # TODO: Print the door state with sensor ID and timestamp
        print(f"[{sensor_id}] Door is {door_state}")
    
    print(f"[{sensor_id}] Door sensor deactivated")

def main():
    """
    Main function to demonstrate basic threading.
    """
    print("🔒 Security System - Basic Door Monitoring")
    print("=" * 50)
    
    # TODO: Create a door sensor thread
    # Use sensor_id="DOOR-001" and check_interval=2
    door_thread = threading.Thread(
        target=door_sensor, 
        args=("DOOR-001", 2)
    )
    
    # TODO: Start the door sensor thread
    door_thread.start()
    
    # TODO: Wait for the thread to complete
    door_thread.join()
    
    print("\n🏁 Door monitoring complete!")

if __name__ == "__main__":
    main()
