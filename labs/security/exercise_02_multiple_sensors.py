"""
Exercise 2: Multiple Sensors with Timing
=======================================

This exercise demonstrates running multiple threads simultaneously with
different timing patterns, similar to the original Lab 16 but with
a security system context.

Learning Objectives:
- Create multiple threads
- Use different timing patterns for each thread
- Observe concurrent execution and output interleaving
- Understand thread independence

Task: Create multiple security sensors that run concurrently with different
monitoring intervals.
"""

import threading
import time
import random

def security_sensor(sensor_name, sensor_type, max_interval, readings=8):
    """
    Simulates a security sensor with random timing between readings.
    
    Args:
        sensor_name (str): Name of the sensor (e.g., "DOOR-001")
        sensor_type (str): Type of sensor (e.g., "Door", "Motion", "Temperature")
        max_interval (int): Maximum time between readings in seconds
        readings (int): Number of readings to take
    """
    print(f"[{sensor_name}] {sensor_type} sensor activated")
    
    for i in range(1, readings + 1):
        # TODO: Generate random sleep time between 1 and max_interval
        sleep_time = random.randint(1, max_interval)
        
        # TODO: Sleep for the random duration
        time.sleep(sleep_time)
        
        # TODO: Generate a sensor reading based on sensor type
        if sensor_type == "Door":
            reading = random.choice(["OPEN", "CLOSED"])
        elif sensor_type == "Motion":
            reading = random.choice(["DETECTED", "NONE"])
        elif sensor_type == "Temperature":
            reading = f"{random.randint(15, 30)}°C"
        else:
            reading = "UNKNOWN"
        
        # TODO: Print the sensor reading
        print(f"[{sensor_name}] Reading #{i}: {reading}")
    
    print(f"[{sensor_name}] {sensor_type} sensor deactivated")

def main():
    """
    Main function to demonstrate multiple concurrent threads.
    """
    print("🔒 Security System - Multi-Sensor Monitoring")
    print("=" * 50)
    
    # TODO: Create multiple sensor threads with different timing
    # Door sensor - checks every 1-3 seconds
    door_thread = threading.Thread(
        target=security_sensor,
        args=("DOOR-001", "Door", 3, 6)
    )
    
    # Motion sensor - checks every 1-2 seconds  
    motion_thread = threading.Thread(
        target=security_sensor,
        args=("MOTION-001", "Motion", 2, 8)
    )
    
    # Temperature sensor - checks every 2-5 seconds
    temp_thread = threading.Thread(
        target=security_sensor,
        args=("TEMP-001", "Temperature", 5, 4)
    )
    
    # TODO: Start all sensor threads
    door_thread.start()
    motion_thread.start()
    temp_thread.start()
    
    # TODO: Wait for all threads to complete
    door_thread.join()
    motion_thread.join()
    temp_thread.join()
    
    print("\n🏁 All sensor monitoring complete!")

if __name__ == "__main__":
    main()
