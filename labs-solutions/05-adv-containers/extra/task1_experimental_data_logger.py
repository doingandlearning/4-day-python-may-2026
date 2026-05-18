# Lab 05 Extra - Task 1: Experimental Data Logger
# Practice with dictionaries for sensor readings

print("=" * 50)
print("Task 1: Experimental Data Logger")
print("=" * 50)

# Sample data - sensor readings (sensor_id: temperature_celsius)
sensor_readings = {
    "Sensor_A": 23.5,
    "Sensor_B": 24.1,
    "Sensor_C": 22.8,
    "Sensor_D": 25.2,
    "Sensor_E": 23.9
}

# Print all sensor names
print("Sensor names:")
for name in sensor_readings:
    print(f"- {name}")

# Print all temperature readings
print("\nTemperature readings:")
for temp in sensor_readings.values():
    print(f"- {temp}°C")

# Print Sensor_A's reading
print(f"\nSensor_A's reading: {sensor_readings['Sensor_A']}°C")

# Add a new sensor "Sensor_F" with reading 24.7
sensor_readings["Sensor_F"] = 24.7
print(f"\nAdded Sensor_F: {sensor_readings}")

# Update Sensor_B's reading to 25.1
sensor_readings["Sensor_B"] = 25.1
print(f"Updated Sensor_B's reading: {sensor_readings}")

# Remove Sensor_C from the readings
del sensor_readings["Sensor_C"]
print(f"Removed Sensor_C: {sensor_readings}")

# Find the sensor with the highest temperature
highest_temp = max(sensor_readings.values())
print(f"\nHighest temperature: {highest_temp}°C")

# Find which sensor has the highest temperature
for name, temp in sensor_readings.items():
    if temp == highest_temp:
        print(f"Sensor with highest temperature: {name}")
        break

# Find the sensor with the lowest temperature
lowest_temp = min(sensor_readings.values())
print(f"Lowest temperature: {lowest_temp}°C")

# Find which sensor has the lowest temperature
for name, temp in sensor_readings.items():
    if temp == lowest_temp:
        print(f"Sensor with lowest temperature: {name}")
        break

# Calculate the average temperature
total_temp = sum(sensor_readings.values())
average_temp = total_temp / len(sensor_readings)
print(f"Average temperature: {average_temp:.2f}°C")

# Print sensors with readings above 24°C
print("\nSensors with readings above 24°C:")
for name, temp in sensor_readings.items():
    if temp > 24:
        print(f"- {name}: {temp}°C")

print("\n" + "=" * 50)
print("Task 1 completed successfully!")
print("=" * 50)
