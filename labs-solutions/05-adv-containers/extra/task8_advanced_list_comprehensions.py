# Lab 05 Extra - Task 8: Advanced List Comprehensions for Scientific Data
# Practice with complex list comprehensions for scientific measurements

print("=" * 50)
print("Task 8: Advanced List Comprehensions for Scientific Data")
print("=" * 50)

# Sample data - experimental measurements
measurements = [
    ("Sensor_A", 23.5, "Temperature"),
    ("Sensor_B", 24.1, "Temperature"),
    ("Sensor_C", 78.2, "Humidity"),
    ("Sensor_D", 25.2, "Temperature"),
    ("Sensor_E", 82.1, "Humidity")
]

print("Original measurements:")
for measurement in measurements:
    print(f"- {measurement}")

# Create a list of just the sensor names
sensor_names = [measurement[0] for measurement in measurements]
sensor_names = [name for name, _, _ in measurements] # (sensor, reading, type)
print(f"\nSensor names: {sensor_names}")

# Create a list of just the values
values = [measurement[1] for measurement in measurements]
values = [reading for _, reading, _ in measurements]

values = []
for measurement in measurements:
    values.append(measurement[1])

values = []
for _, reading, _ in measurements:
    values.append(reading)

print(f"Sensor values: {values}")

# Create a list of names of temperature sensors
temp_sensors = [measurement[0] for measurement in measurements if measurement[2] == "Temperature"]
print(f"Temperature sensors: {temp_sensors}")

# Create a list of values from temperature sensors
temp_values = [measurement[1] for measurement in measurements if measurement[2] == "Temperature"]
print(f"Temperature values: {temp_values}")

# Create a list of tuples (name, value) for sensors with values above 24
high_value_sensors = [(measurement[0], measurement[1]) for measurement in measurements if measurement[1] > 24]
print(f"Sensors with values above 24: {high_value_sensors}")

# Create a list of names of humidity sensors with values above 80
high_humidity_sensors = [measurement[0] for measurement in measurements 
                        if measurement[2] == "Humidity" and measurement[1] > 80]
print(f"Humidity sensors with values above 80: {high_humidity_sensors}")

# Create a dictionary from the list where sensor name is key and value is the measurement
sensor_dict = {measurement[0]: measurement[1] for measurement in measurements}
print(f"Sensor dictionary: {sensor_dict}")

# Additional advanced list comprehensions for practice
print("\nAdditional advanced examples:")

# Create a list of tuples (name, value, type) for all measurements
full_info = [(measurement[0], measurement[1], measurement[2]) for measurement in measurements]
print(f"Full measurement info: {full_info}")

# Create a list of sensor names with their status (high/normal/low)
sensor_status = [(measurement[0], "high" if measurement[1] > 24 else "normal" if measurement[1] > 20 else "low") 
                for measurement in measurements]
print(f"Sensor status: {sensor_status}")

# Create a list of temperature sensors with their values in Kelvin
temp_kelvin = [(measurement[0], measurement[1] + 273.15) for measurement in measurements 
              if measurement[2] == "Temperature"]
print(f"Temperature sensors in Kelvin: {temp_kelvin}")

# Create a list of sensors with values above average
average_value = sum(values) / len(values)
above_average = [measurement[0] for measurement in measurements if measurement[1] > average_value]
print(f"Sensors above average ({average_value:.2f}): {above_average}")

# Create a list of tuples (sensor, value, type) sorted by value
sorted_measurements = sorted(measurements, key=lambda x: x[1])
print(f"Measurements sorted by value: {sorted_measurements}")

# Create a dictionary grouped by type
type_groups = {}
for measurement in measurements:
    sensor_type = measurement[2]
    if sensor_type not in type_groups:
        type_groups[sensor_type] = []
    type_groups[sensor_type].append((measurement[0], measurement[1]))

print(f"Measurements grouped by type: {type_groups}")

# Create a list of sensor names with their relative performance (above/below median)
sorted_values = sorted(values)
median = sorted_values[len(sorted_values) // 2]
performance = [(measurement[0], "above" if measurement[1] > median else "below") 
              for measurement in measurements]
print(f"Sensor performance vs median ({median}): {performance}")

print("\n" + "=" * 50)
print("Task 8 completed successfully!")
print("=" * 50)
