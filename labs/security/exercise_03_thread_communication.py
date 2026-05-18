"""
Exercise 3: Thread Communication with Queues
============================================

This exercise introduces thread communication using queues to pass data
between threads, similar to the security.py example but simplified.

Learning Objectives:
- Use queues for thread communication
- Pass data between threads safely
- Process events from multiple sources
- Understand producer-consumer patterns

Task: Create a security system where sensors send events to a central
processor via a queue.
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
        
        # TODO: Generate door state
        door_state = random.choice(["OPEN", "CLOSED"])
        
        # TODO: Create event dictionary with type, value, and timestamp
        event = {
            "type": "door",
            "value": door_state,
            "sensor_id": sensor_id,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        }
        
        # TODO: Put the event in the queue
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
        
        # TODO: Generate motion detection (biased towards no motion)
        motion_detected = random.random() < 0.3  # 30% chance of motion
        
        # TODO: Create event dictionary
        event = {
            "type": "motion",
            "value": motion_detected,
            "sensor_id": sensor_id,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        }
        
        # TODO: Put the event in the queue
        events.put(event)
        print(f"[{sensor_id}] Sent motion event: {motion_detected}")
    
    print(f"[{sensor_id}] Motion sensor deactivated")

def event_processor():
    """
    Central processor that handles events from all sensors.
    """
    print("[PROCESSOR] Event processor activated")
    
    processed_events = 0
    
    # TODO: Process events from the queue
    while processed_events < 11:  # Total events from both sensors
        try:
            # TODO: Get an event from the queue with timeout
            event = events.get(timeout=1)
            
            # TODO: Process the event based on its type
            if event["type"] == "door":
                print(f"[PROCESSOR] Door event from {event['sensor_id']}: {event['value']} at {event['timestamp']}")
            elif event["type"] == "motion":
                status = "DETECTED" if event["value"] else "NONE"
                print(f"[PROCESSOR] Motion event from {event['sensor_id']}: {status} at {event['timestamp']}")
            
            # TODO: Mark the task as done
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
    
    # TODO: Create sensor threads
    door_thread = threading.Thread(target=door_sensor, args=("DOOR-001",))
    motion_thread = threading.Thread(target=motion_sensor, args=("MOTION-001",))
    processor_thread = threading.Thread(target=event_processor)
    
    # TODO: Start all threads
    door_thread.start()
    motion_thread.start()
    processor_thread.start()
    
    # TODO: Wait for all threads to complete
    door_thread.join()
    motion_thread.join()
    processor_thread.join()
    
    print("\n🏁 Event processing complete!")

if __name__ == "__main__":
    main()
