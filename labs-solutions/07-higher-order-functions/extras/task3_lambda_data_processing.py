# Lab 07 Extra - Task 3: Lambda Functions for Data Processing
# Practice with lambda functions for processing sensor data

print("=" * 50)
print("Task 3: Lambda Functions for Data Processing")
print("=" * 50)

# Sample sensor data: (sensor_id, reading, timestamp, status)
sensor_data = [
    ("SENSOR_A", 23.5, "10:30", "OK"),
    ("SENSOR_B", 25.1, "10:31", "WARNING"),
    ("SENSOR_C", 22.8, "10:32", "OK"),
    ("SENSOR_D", 26.3, "10:33", "ERROR"),
    ("SENSOR_E", 24.7, "10:34", "OK")
]

print("Original sensor data:")
for sensor in sensor_data:
    print(f"  {sensor[0]}: {sensor[1]}°C at {sensor[2]} - {sensor[3]}")

# Use lambda to extract just the readings from sensor data
readings = list(map(lambda x: x[1], sensor_data))
print(f"\nExtracted readings: {readings}")

# Use lambda to find sensors with "OK" status
ok_sensors = list(filter(lambda x: x[3] == "OK", sensor_data))
print(f"\nSensors with OK status:")
for sensor in ok_sensors:
    print(f"  {sensor[0]}: {sensor[1]}°C")

# Use lambda to calculate readings above 24°C
high_readings = list(filter(lambda x: x[1] > 24, sensor_data))
print(f"\nSensors with readings above 24°C:")
for sensor in high_readings:
    print(f"  {sensor[0]}: {sensor[1]}°C")

# Use lambda to create a list of (sensor_id, reading) tuples for error sensors
error_sensors = list(map(lambda x: (x[0], x[1]), filter(lambda x: x[3] == "ERROR", sensor_data)))
print(f"\nError sensors (ID, reading): {error_sensors}")

# Use lambda to sort sensors by reading value
sorted_by_reading = sorted(sensor_data, key=lambda x: x[1])
print(f"\nSensors sorted by reading value:")
for sensor in sorted_by_reading:
    print(f"  {sensor[0]}: {sensor[1]}°C")

# Additional lambda examples
print(f"\nAdditional lambda examples:")

# Find sensors with readings between 23 and 25 degrees
temp_range_sensors = list(filter(lambda x: 23 <= x[1] <= 25, sensor_data))
print(f"Sensors with readings between 23-25°C:")
for sensor in temp_range_sensors:
    print(f"  {sensor[0]}: {sensor[1]}°C")

# Convert readings to Fahrenheit
fahrenheit_readings = list(map(lambda x: (x[0], x[1] * 9/5 + 32), sensor_data))
print(f"\nReadings converted to Fahrenheit:")
for sensor, temp_f in fahrenheit_readings:
    print(f"  {sensor}: {temp_f:.1f}°F")

# Find sensors with specific statuses
warning_sensors = list(filter(lambda x: x[3] in ["WARNING", "ERROR"], sensor_data))
print(f"\nSensors with warnings or errors:")
for sensor in warning_sensors:
    print(f"  {sensor[0]}: {sensor[1]}°C - {sensor[3]}")

# Sort by status, then by reading
status_reading_sorted = sorted(sensor_data, key=lambda x: (x[3], x[1]))
print(f"\nSensors sorted by status, then reading:")
for sensor in status_reading_sorted:
    print(f"  {sensor[0]}: {sensor[1]}°C - {sensor[3]}")

# Calculate average reading for each status
status_groups = {}
for sensor in sensor_data:
    status = sensor[3]
    if status not in status_groups:
        status_groups[status] = []
    status_groups[status].append(sensor[1])

print(f"\nAverage readings by status:")
for status, readings in status_groups.items():
    avg_reading = sum(readings) / len(readings)
    print(f"  {status}: {avg_reading:.2f}°C (from {readings})")

# Find the sensor with the highest reading
max_sensor = max(sensor_data, key=lambda x: x[1])
print(f"\nSensor with highest reading: {max_sensor[0]} at {max_sensor[1]}°C")

# Find the sensor with the lowest reading
min_sensor = min(sensor_data, key=lambda x: x[1])
print(f"Sensor with lowest reading: {min_sensor[0]} at {min_sensor[1]}°C")

# Create a summary report using lambdas
print(f"\nSummary report:")
ok_count = len(list(filter(lambda x: x[3] == "OK", sensor_data)))
warning_count = len(list(filter(lambda x: x[3] == "WARNING", sensor_data)))
error_count = len(list(filter(lambda x: x[3] == "ERROR", sensor_data)))

print(f"  Total sensors: {len(sensor_data)}")
print(f"  OK: {ok_count}")
print(f"  WARNING: {warning_count}")
print(f"  ERROR: {error_count}")

avg_temp = sum(map(lambda x: x[1], sensor_data)) / len(sensor_data)
print(f"  Average temperature: {avg_temp:.2f}°C")

print("\n" + "=" * 50)
print("Task 3 completed successfully!")
print("=" * 50)
