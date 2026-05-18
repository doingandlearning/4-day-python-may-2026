"""
Exercise 6: Complete Security System
====================================

This exercise combines all previous concepts into a complete security
monitoring system, similar to the security.py example but with
educational structure.

Learning Objectives:
- Integrate all threading concepts
- Build a complete multi-threaded application
- Understand real-world threading patterns
- Implement proper thread lifecycle management

Task: Create a complete security system that integrates all the concepts
learned in previous exercises.
"""

import threading
import queue
import time
import random
from datetime import datetime
from dataclasses import dataclass
from typing import Literal

# Type definitions
EventType = Literal["door", "motion", "cmd", "status"]
SystemState = Literal["armed", "disarmed", "alarm"]

@dataclass
class SecurityEvent:
    """Represents a security system event."""
    type: EventType
    value: str
    sensor_id: str
    timestamp: str

class SecuritySystem:
    """
    Complete security system with multiple sensors and event processing.
    """
    
    def __init__(self):
        self.events = queue.Queue(maxsize=100)
        self.state = "disarmed"
        self.alarm_triggered = False
        self.running = True
        self.lock = threading.Lock()
        self.threads = []
        
    def log_event(self, message):
        """Thread-safe logging."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {message}")
    
    def update_state(self, new_state):
        """Thread-safe state update."""
        with self.lock:
            old_state = self.state
            self.state = new_state
            self.log_event(f"State changed: {old_state} -> {new_state}")
    
    def door_sensor(self, sensor_id):
        """Door sensor thread."""
        self.log_event(f"Door sensor {sensor_id} activated")
        
        try:
            while self.running:
                time.sleep(random.randint(2, 5))
                door_state = random.choice(["OPEN", "CLOSED"])
                
                event = SecurityEvent(
                    type="door",
                    value=door_state,
                    sensor_id=sensor_id,
                    timestamp=datetime.now().strftime("%H:%M:%S")
                )
                
                self.events.put(event, timeout=1)
                self.log_event(f"Door {sensor_id}: {door_state}")
                
        except Exception as e:
            self.log_event(f"Door sensor {sensor_id} error: {e}")
        finally:
            self.log_event(f"Door sensor {sensor_id} deactivated")
    
    def motion_sensor(self, sensor_id):
        """Motion sensor thread."""
        self.log_event(f"Motion sensor {sensor_id} activated")
        
        try:
            while self.running:
                time.sleep(random.randint(1, 3))
                motion_detected = random.random() < 0.3
                
                if motion_detected:
                    event = SecurityEvent(
                        type="motion",
                        value="DETECTED",
                        sensor_id=sensor_id,
                        timestamp=datetime.now().strftime("%H:%M:%S")
                    )
                    
                    self.events.put(event, timeout=1)
                    self.log_event(f"Motion {sensor_id}: DETECTED")
                    
        except Exception as e:
            self.log_event(f"Motion sensor {sensor_id} error: {e}")
        finally:
            self.log_event(f"Motion sensor {sensor_id} deactivated")
    
    def event_processor(self):
        """Central event processor thread."""
        self.log_event("Event processor activated")
        
        try:
            while self.running or not self.events.empty():
                try:
                    event = self.events.get(timeout=0.5)
                    self._process_event(event)
                    self.events.task_done()
                except queue.Empty:
                    continue
                    
        except Exception as e:
            self.log_event(f"Event processor error: {e}")
        finally:
            self.log_event("Event processor deactivated")
    
    def _process_event(self, event):
        """Process individual events."""
        with self.lock:
            armed = (self.state == "armed")
            
        if event.type == "door" and event.value == "OPEN" and armed:
            self._trigger_alarm(f"Door {event.sensor_id} opened while armed")
        elif event.type == "motion" and event.value == "DETECTED" and armed:
            self._trigger_alarm(f"Motion detected by {event.sensor_id} while armed")
        
        self.log_event(f"Processed {event.type} event from {event.sensor_id}")
    
    def _trigger_alarm(self, reason):
        """Trigger security alarm."""
        with self.lock:
            if not self.alarm_triggered:
                self.alarm_triggered = True
                self.state = "alarm"
                self.log_event(f"🚨 ALARM TRIGGERED: {reason}")
    
    def system_controller(self):
        """System controller thread."""
        self.log_event("System controller activated")
        
        try:
            # Arm system after 5 seconds
            time.sleep(5)
            self.update_state("armed")
            self.log_event("System ARMED")
            
            # Disarm system after 15 seconds
            time.sleep(10)
            self.update_state("disarmed")
            self.log_event("System DISARMED")
            
        except Exception as e:
            self.log_event(f"System controller error: {e}")
        finally:
            self.log_event("System controller deactivated")
    
    def status_monitor(self):
        """Periodic status monitoring."""
        self.log_event("Status monitor activated")
        
        try:
            while self.running:
                time.sleep(3)
                with self.lock:
                    status = f"State: {self.state}, Alarm: {self.alarm_triggered}"
                self.log_event(f"Status: {status}")
                
        except Exception as e:
            self.log_event(f"Status monitor error: {e}")
        finally:
            self.log_event("Status monitor deactivated")
    
    def start(self):
        """Start the security system."""
        self.log_event("Starting security system...")
        
        # Create and start all threads
        self.threads = [
            threading.Thread(target=self.door_sensor, args=("DOOR-001",), daemon=True),
            threading.Thread(target=self.motion_sensor, args=("MOTION-001",), daemon=True),
            threading.Thread(target=self.event_processor, daemon=True),
            threading.Thread(target=self.system_controller, daemon=True),
            threading.Thread(target=self.status_monitor, daemon=True),
        ]
        
        for thread in self.threads:
            thread.start()
    
    def stop(self):
        """Stop the security system."""
        self.log_event("Stopping security system...")
        self.running = False
        
        # Wait for all threads to complete
        for thread in self.threads:
            if thread.is_alive():
                thread.join(timeout=2)
        
        self.log_event("Security system stopped")

def main():
    """
    Main function to demonstrate complete security system.
    """
    print("🔒 Complete Security System")
    print("=" * 50)
    
    # TODO: Create and start security system
    security = SecuritySystem()
    security.start()
    
    # TODO: Run for 20 seconds
    try:
        time.sleep(20)
    except KeyboardInterrupt:
        print("\nInterrupted by user")
    finally:
        # TODO: Stop the security system
        security.stop()
    
    print("\n🏁 Security system demonstration complete!")

if __name__ == "__main__":
    main()
