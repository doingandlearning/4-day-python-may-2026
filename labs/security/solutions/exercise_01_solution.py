"""
Exercise 1 Solution: Basic Sensor Threads
=========================================

Complete solution demonstrating basic threading concepts.
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
    
    for i in range(5):  # Check 5 times
        time.sleep(check_interval)
        
        door_state = random.choice(["OPEN", "CLOSED"])
        print(f"[{sensor_id}] Door is {door_state}")
    
    print(f"[{sensor_id}] Door sensor deactivated")

def main():
    """
    Main function to demonstrate basic threading.
    """
    print("🔒 Security System - Basic Door Monitoring")
    print("=" * 50)
    
    # Create a door sensor thread
    door_thread = threading.Thread(
        target=door_sensor, 
        args=("DOOR-001", 2)
    )
    
    # Start the door sensor thread
    door_thread.start()
    
    # Wait for the thread to complete
    door_thread.join()
    
    print("\n🏁 Door monitoring complete!")

if __name__ == "__main__":
    main()
