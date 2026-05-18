"""
Basic Weather Station - Simplified version for Lab 16 Part 1
This covers the core threading concepts without the advanced features.
"""

import threading
import time
import random

def sensor_reader(sensor_name, sensor_unit, max_interval, readings_count=10):
    """
    Basic sensor reader function - equivalent to the original printer() function
    but with more meaningful output.
    """
    for i in range(1, readings_count + 1):
        # Generate random sleep time (equivalent to original lab)
        sleep_time = random.randint(1, max_interval)
        time.sleep(sleep_time)
        
        # Generate random reading value
        reading_value = random.randint(0, 100)
        
        # Print the reading (equivalent to printing letters in original)
        print(f"[{sensor_name}] Reading #{i}: {reading_value} {sensor_unit}")

def main():
    """
    Main function - equivalent to the original lab's thread creation.
    """
    print("🌤️  Basic Weather Station")
    print("=" * 30)
    
    # Create sensor threads (equivalent to original t1-t5)
    t1 = threading.Thread(target=sensor_reader, args=("Temperature", "°C", 3))
    t2 = threading.Thread(target=sensor_reader, args=("Humidity", "%", 5))
    t3 = threading.Thread(target=sensor_reader, args=("Pressure", "hPa", 7))
    t4 = threading.Thread(target=sensor_reader, args=("Wind Speed", "km/h", 4))
    t5 = threading.Thread(target=sensor_reader, args=("Rainfall", "mm", 8))
    
    # Start all threads (equivalent to original start() calls)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    
    # Wait for all threads to complete
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    
    print("\n🏁 All sensor readings complete!")

if __name__ == "__main__":
    main()
