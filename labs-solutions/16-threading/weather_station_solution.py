"""
Weather Station Simulator - Threading Lab Solution
This solution demonstrates all the threading concepts from Lab 16
"""

import threading
import time
import random
from datetime import datetime
import os

# Global variables for thread synchronization
log_lock = threading.Lock()
data_lock = threading.Lock()
sensor_data = {}

def sensor_reader(sensor_name, sensor_unit, max_interval, readings_count=10):
    """
    Simulates a weather sensor that takes readings at random intervals.
    
    Args:
        sensor_name (str): Name of the sensor
        sensor_unit (str): Unit of measurement
        max_interval (int): Maximum time between readings in seconds
        readings_count (int): Number of readings to take
    """
    for i in range(1, readings_count + 1):
        # Generate random sleep time between 1 and max_interval seconds
        sleep_time = random.randint(1, max_interval)
        time.sleep(sleep_time)
        
        # Generate random sensor reading (0-100 for simplicity)
        reading_value = random.randint(0, 100)
        
        # Print the reading
        print(f"[{sensor_name}] Reading #{i}: {reading_value} {sensor_unit}")
        
        # Log the data (thread-safe)
        log_data(sensor_name, reading_value, sensor_unit)
        
        # Update shared sensor data (thread-safe)
        update_sensor_data(sensor_name, reading_value, sensor_unit)

def log_data(sensor_name, value, unit):
    """
    Thread-safe logging of sensor data to a file.
    """
    with log_lock:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {sensor_name}: {value} {unit}\n"
        
        with open("weather_log.txt", "a") as f:
            f.write(log_entry)

def update_sensor_data(sensor_name, value, unit):
    """
    Thread-safe update of shared sensor data.
    """
    with data_lock:
        sensor_data[sensor_name] = {
            'value': value,
            'unit': unit,
            'timestamp': datetime.now().strftime("%H:%M:%S")
        }

def weather_alert():
    """
    Prints a weather alert message.
    """
    print("⚠️  WEATHER ALERT: Checking conditions...")

def continuous_alert():
    """
    Creates a repeating weather alert system.
    """
    weather_alert()
    # Schedule the next alert
    timer = threading.Timer(10.0, continuous_alert)
    timer.daemon = True  # Dies when main program exits
    timer.start()

def status_report():
    """
    Prints current status of all sensors.
    """
    with data_lock:
        print("\n📊 CURRENT SENSOR STATUS:")
        print("-" * 40)
        for sensor, data in sensor_data.items():
            print(f"{sensor}: {data['value']} {data['unit']} (last updated: {data['timestamp']})")
        print("-" * 40)
        print()

def periodic_status():
    """
    Creates a repeating status report every 15 seconds.
    """
    status_report()
    # Schedule the next status report
    timer = threading.Timer(15.0, periodic_status)
    timer.daemon = True
    timer.start()

def main():
    """
    Main function that sets up and runs the weather station simulation.
    """
    print("🌤️  Starting Weather Station Simulator...")
    print("=" * 50)
    
    # Clear any existing log file
    if os.path.exists("weather_log.txt"):
        os.remove("weather_log.txt")
    
    # Create sensor threads
    sensors = [
        ("Temperature", "°C", 3),      # 1-3 seconds
        ("Humidity", "%", 5),          # 2-5 seconds  
        ("Pressure", "hPa", 7),        # 3-7 seconds
        ("Wind Speed", "km/h", 4),     # 1-4 seconds
        ("Rainfall", "mm", 8)          # 4-8 seconds
    ]
    
    threads = []
    
    # Create and start sensor threads
    for sensor_name, unit, max_interval in sensors:
        thread = threading.Thread(
            target=sensor_reader,
            args=(sensor_name, unit, max_interval, 8)  # 8 readings each
        )
        thread.daemon = True  # Dies when main program exits
        threads.append(thread)
        thread.start()
    
    # Start continuous weather alerts
    continuous_alert()
    
    # Start periodic status reports
    periodic_status()
    
    # Run for 30 seconds
    print("Weather station running for 30 seconds...")
    time.sleep(30)
    
    print("\n🏁 Weather station simulation complete!")
    print("Check 'weather_log.txt' for detailed sensor data.")

if __name__ == "__main__":
    main()
