"""
Exercise 4 Solution: Timers and Scheduled Tasks
===============================================

Complete solution demonstrating timer-based threading.
"""

import threading
import time
import random
from datetime import datetime

def security_alert():
    """
    Function to be called by timer - prints a security alert.
    """
    print("🚨 SECURITY ALERT: System status check required!")

def periodic_status_check():
    """
    Periodic status check that reschedules itself.
    """
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"📊 [STATUS] System check at {current_time}")
    
    # Simulate some status checks
    cpu_usage = random.randint(10, 90)
    memory_usage = random.randint(20, 80)
    print(f"📊 [STATUS] CPU: {cpu_usage}%, Memory: {memory_usage}%")
    
    # Schedule the next status check in 5 seconds
    timer = threading.Timer(5.0, periodic_status_check)
    timer.daemon = True  # Dies when main program exits
    timer.start()

def door_sensor(sensor_id, duration=15):
    """
    Door sensor that runs for a specified duration.
    """
    print(f"[{sensor_id}] Door sensor activated")
    start_time = time.time()
    
    while time.time() - start_time < duration:
        time.sleep(random.randint(2, 4))
        door_state = random.choice(["OPEN", "CLOSED"])
        print(f"[{sensor_id}] Door is {door_state}")
    
    print(f"[{sensor_id}] Door sensor deactivated")

def main():
    """
    Main function to demonstrate timer-based features.
    """
    print("🔒 Security System - Timer Features")
    print("=" * 50)
    
    # Create a one-time alert timer (3 seconds delay)
    alert_timer = threading.Timer(3.0, security_alert)
    alert_timer.start()
    
    # Start periodic status checks
    periodic_status_check()
    
    # Create and start door sensor thread
    door_thread = threading.Thread(target=door_sensor, args=("DOOR-001", 15))
    door_thread.start()
    
    # Run the system for 15 seconds
    print("System running for 15 seconds...")
    time.sleep(15)
    
    # Wait for door sensor to complete
    door_thread.join()
    
    print("\n🏁 Timer demonstration complete!")

if __name__ == "__main__":
    main()
