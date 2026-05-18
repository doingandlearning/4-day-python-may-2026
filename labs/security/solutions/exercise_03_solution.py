"""
Exercise 3 Solution: Thread Communication with Queues
=====================================================

Complete solution demonstrating thread communication using queues.
"""

import threading
import queue
import time
import random
from datetime import datetime

# Global queue for events
events = queue.Queue()

def door_sensor(sensor_id):
    """
    Door sensor that sends events to the central processor.
    """
    print(f"[{sensor_id}] Door sensor activated")
    
    for i in range(5):
        time.sleep(random.randint(1, 3))
        door_state = random.choice(["OPEN", "CLOSED"])
        
        event = {
            "type": "door",
            "value": door_state,
            "sensor_id": sensor_id,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        }
        
        events.put(event)
        print(f"[{sensor_id}] Sent door event: {door_state}")
    
    print(f"[{sensor_id}] Door sensor deactivated")

def motion_sensor(sensor_id):
    """
    Motion sensor that sends events to the central processor.
    """
    print(f"[{sensor_id}] Motion sensor activated")
    
    for i in range(6):
        time.sleep(random.randint(1, 2))
        motion_detected = random.random() < 0.3  # 30% chance of motion
        
        if motion_detected:
            event = {
                "type": "motion",
                "value": motion_detected,
                "sensor_id": sensor_id,
                "timestamp": datetime.now().strftime("%H:%M:%S")
            }
            
            events.put(event)
            print(f"[{sensor_id}] Sent motion event: {motion_detected}")
    
    print(f"[{sensor_id}] Motion sensor deactivated")

def event_processor():
    """
    Central processor that handles events from all sensors.
    """
    print("[PROCESSOR] Event processor activated")
    
    processed_events = 0
    
    while processed_events < 11:  # Total events from both sensors
        try:
            event = events.get(timeout=1)
            
            if event["type"] == "door":
                print(f"[PROCESSOR] Door event from {event['sensor_id']}: {event['value']} at {event['timestamp']}")
            elif event["type"] == "motion":
                status = "DETECTED" if event["value"] else "NONE"
                print(f"[PROCESSOR] Motion event from {event['sensor_id']}: {status} at {event['timestamp']}")
            
            events.task_done()
            processed_events += 1
            
        except queue.Empty:
            print("[PROCESSOR] No events received, continuing...")
    
    print("[PROCESSOR] Event processor deactivated")

def main():
    """
    Main function to demonstrate thread communication with queues.
    """
    print("🔒 Security System - Event Processing")
    print("=" * 50)
    
    # Create sensor threads
    door_thread = threading.Thread(target=door_sensor, args=("DOOR-001",))
    motion_thread = threading.Thread(target=motion_sensor, args=("MOTION-001",))
    processor_thread = threading.Thread(target=event_processor)
    
    # Start all threads
    door_thread.start()
    motion_thread.start()
    processor_thread.start()
    
    # Wait for all threads to complete
    door_thread.join()
    motion_thread.join()
    processor_thread.join()
    
    print("\n🏁 Event processing complete!")

if __name__ == "__main__":
    main()
