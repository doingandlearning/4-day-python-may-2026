# Lab 07 Extra - Task 3: List Comprehensions for Data Processing
# Practice replacing map/filter/lambda with comprehensions & itemgetter

from operator import itemgetter

print("=" * 50)
print("Task 3: Lambda Functions for Data Processing (Comprehensions)")
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

# Extract just the readings
readings = [reading for _, reading, _, _ in sensor_data]
print(f"\nExtracted readings: {readings}")

# Find sensors with "OK" status
ok_sensors = [t for t in sensor_data if t[3] == "OK"]
print(f"\nSensors with OK status:")
for sensor in ok_sensors:
    print(f"  {sensor[0]}: {sensor[1]}°C")

# Calculate readings above 24°C
high_readings = [t for t in sensor_data if t[1] > 24]
print(f"\nSensors with readings above 24°C:")
for sensor in high_readings:
    print(f"  {sensor[0]}: {sensor[1]}°C")

# Create a list of (sensor_id, reading) tuples for error sensors
error_sensors = [(sid, reading) for (sid, reading, _, status) in sensor_data if status == "ERROR"]
print(f"\nError sensors (ID, reading): {error_sensors}")

# Sort sensors by reading value
sorted_by_reading = sorted(sensor_data, key=itemgetter(1))
print(f"\nSensors sorted by reading value:")
for sensor in sorted_by_reading:
    print(f"  {sensor[0]}: {sensor[1]}°C")

# Additional examples

# Find sensors with readings between 23 and 25 degrees
temp_range_sensors = [t for t in sensor_data if 23 <= t[1] <= 25]
print(f"\nSensors with readings between 23-25°C:")
for sensor in temp_range_sensors:
    print(f"  {sensor[0]}: {sensor[1]}°C")

# Convert readings to Fahrenheit
fahrenheit_readings = [(sid, reading * 9/5 + 32) for (sid, reading, *_rest) in sensor_data]
print(f"\nReadings converted to Fahrenheit:")
for sensor, temp_f in fahrenheit_readings:
    print(f"  {sensor}: {temp_f:.1f}°F")

# Find sensors with specific statuses
warning_sensors = [t for t in sensor_data if t[3] in {"WARNING", "ERROR"}]
print(f"\nSensors with warnings or errors:")
for sensor in warning_sensors:
    print(f"  {sensor[0]}: {sensor[1]}°C - {sensor[3]}")

# Sort by status, then by reading
status_reading_sorted = sorted(sensor_data, key=itemgetter(3, 1))
print(f"\nSensors sorted by status, then reading:")
for sensor in status_reading_sorted:
    print(f"  {sensor[0]}: {sensor[1]}°C - {sensor[3]}")

# Calculate average reading for each status (dict & list comprehensions)
statuses = {status for *_, status in sensor_data}
status_groups = {
    s: [reading for (_, reading, *_rest) in sensor_data if _rest[-1] == s]
    for s in statuses
}

print(f"\nAverage readings by status:")
for status, rs in status_groups.items():
    avg_reading = sum(rs) / len(rs)
    print(f"  {status}: {avg_reading:.2f}°C (from {rs})")

# Find the sensor with the highest reading
max_sensor = max(sensor_data, key=itemgetter(1))
print(f"\nSensor with highest reading: {max_sensor[0]} at {max_sensor[1]}°C")

# Find the sensor with the lowest reading
min_sensor = min(sensor_data, key=itemgetter(1))
print(f"Sensor with lowest reading: {min_sensor[0]} at {min_sensor[1]}°C")

# Summary report
print(f"\nSummary report:")
ok_count = sum(1 for *_, status in sensor_data if status == "OK")
warning_count = sum(1 for *_, status in sensor_data if status == "WARNING")
error_count = sum(1 for *_, status in sensor_data if status == "ERROR")

print(f"  Total sensors: {len(sensor_data)}")
print(f"  OK: {ok_count}")
print(f"  WARNING: {warning_count}")
print(f"  ERROR: {error_count}")

avg_temp = sum(r for _, r, _, _ in sensor_data) / len(sensor_data)
print(f"  Average temperature: {avg_temp:.2f}°C")

print("\n" + "=" * 50)
print("Task 3 completed successfully!")
print("=" * 50)
