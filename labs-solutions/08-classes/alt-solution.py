class SensorReading:
    """
    Represents a sensor reading with an ID, timestamp, value, and unit.
    """

    def __init__(self, sensor_id: str, timestamp: str, value: float, units: str):
        """
        Initializes a sensor reading.

        :param sensor_id: Unique ID of the sensor.
        :param timestamp: Time when the reading was taken.
        :param value: Recorded measurement.
        :param units: Measurement units (e.g., °C, ppm).
        """
        self.sensor_id = sensor_id
        self.timestamp = timestamp
        self.value = value
        self.units = units

    def __str__(self):
        """Returns a human-readable string representation of the sensor reading."""
        return f"Sensor {self.sensor_id} at {self.timestamp}: {self.value} {self.units}"

    def __repr__(self):
        """Returns a developer-friendly representation of the object."""
        return f"SensorReading(sensor_id='{self.sensor_id}', timestamp='{self.timestamp}', value={self.value}, units='{self.units}')"

    def is_above_threshold(self, threshold: float) -> bool:
        """
        Checks if the reading exceeds a given threshold.

        :param threshold: Threshold value.
        :return: True if value is above threshold, False otherwise.
        """
        return self.value > threshold

    def adjust_reading(self, correction: float):
        """
        Adjusts the reading by a correction factor.

        :param correction: Value to add or subtract from the reading.
        """
        self.value += correction


# --- Demonstrating the Solution ---

# Creating sensor readings
r1 = SensorReading("TEMP_001", "2025-03-11 14:30:00", 22.5, "°C")
r2 = SensorReading("CO2_002", "2025-03-11 14:31:00", 450.0, "ppm")
r3 = SensorReading("TEMP_002", "2025-03-11 14:32:00", 19.8, "°C")

# Printing readings
print(r1)
print(r2)

# Checking if readings exceed a threshold
print(f"{r1.sensor_id} above 20°C?:", r1.is_above_threshold(20))  # True
print(f"{r2.sensor_id} above 400ppm?:", r2.is_above_threshold(400))  # True

# Adjusting readings
r1.adjust_reading(-2.5)
print(f"After correction: {r1}")

# --- Tracking Assignments ---
print("\n### Object Assignment Demonstration ###")
r4 = r1  # This does not create a new object; r4 is just another reference to r1
r4.value = 25.0
print("r1 after modifying r4:", r1)  # r1 is also modified!

# --- Working with Multiple Sensor Readings ---
readings = [r1, r2, r3]

# List all readings
print("\nAll sensor readings:")
for reading in readings:
    print(reading)

# Filter readings above a threshold using list comprehension
above_threshold_readings = [reading for reading in readings if reading.is_above_threshold(20)]
print("\nReadings above threshold:")
for reading in above_threshold_readings:
    print(reading)

# Adjust all readings
for reading in readings:
    reading.adjust_reading(1.5)

print("\nAll readings after adjustment:")
for reading in readings:
    print(reading)

