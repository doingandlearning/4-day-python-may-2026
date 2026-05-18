# Lab 06 Extra - Task 8: Data Processing Pipeline
# Practice with functions to create a complete data processing pipeline

print("=" * 50)
print("Task 8: Data Processing Pipeline")
print("=" * 50)

import random

def read_sensor_data():
    """Simulate reading sensor data - returns a list of sensor readings"""
    # Simulate sensor readings with some noise and potential anomalies
    base_temperature = 22.0
    readings = []
    
    # Generate 20 readings around the base temperature
    for i in range(20):
        # Add some random variation
        variation = random.uniform(-2.0, 2.0)
        reading = base_temperature + variation
        
        # Occasionally add an anomaly
        if random.random() < 0.1:  # 10% chance of anomaly
            reading += random.uniform(-5.0, 5.0)
        
        readings.append(round(reading, 1))
    
    return readings

def filter_valid_readings(readings, min_val, max_val):
    """Filter readings within a specified range"""
    valid_readings = []
    for reading in readings:
        if min_val <= reading <= max_val:
            valid_readings.append(reading)
    return valid_readings

def calculate_statistics(readings):
    """Calculate basic statistics for a list of readings"""
    if len(readings) == 0:
        return {"mean": 0, "max": 0, "min": 0, "range": 0, "count": 0}
    
    mean = sum(readings) / len(readings)
    max_val = max(readings)
    min_val = min(readings)
    range_val = max_val - min_val
    count = len(readings)
    
    return {
        "mean": round(mean, 2),
        "max": max_val,
        "min": min_val,
        "range": round(range_val, 2),
        "count": count
    }

def detect_anomalies(readings, threshold):
    """Find readings more than threshold standard deviations from mean"""
    if len(readings) <= 1:
        return []
    
    # Calculate mean and standard deviation
    mean = sum(readings) / len(readings)
    variance = sum((x - mean) ** 2 for x in readings) / (len(readings) - 1)
    std_dev = variance ** 0.5
    
    anomalies = []
    for reading in readings:
        z_score = abs(reading - mean) / std_dev
        if z_score > threshold:
            anomalies.append(reading)
    
    return anomalies

def generate_report(statistics, anomalies, original_count):
    """Generate a formatted report of the data analysis"""
    print("=" * 40)
    print("SENSOR DATA ANALYSIS REPORT")
    print("=" * 40)
    print(f"Original readings: {original_count}")
    print(f"Valid readings: {statistics['count']}")
    print(f"Filtered out: {original_count - statistics['count']}")
    print()
    print("STATISTICS:")
    print(f"  Mean temperature: {statistics['mean']}°C")
    print(f"  Maximum temperature: {statistics['max']}°C")
    print(f"  Minimum temperature: {statistics['min']}°C")
    print(f"  Temperature range: {statistics['range']}°C")
    print()
    print("ANOMALY DETECTION:")
    if anomalies:
        print(f"  Anomalies detected: {len(anomalies)}")
        print(f"  Anomalous readings: {anomalies}")
    else:
        print("  No anomalies detected")
    print("=" * 40)

def process_sensor_data():
    """Main function that processes sensor data using all other functions"""
    print("Starting sensor data processing pipeline...")
    print()
    
    # Step 1: Read sensor data
    print("Step 1: Reading sensor data...")
    raw_readings = read_sensor_data()
    print(f"Raw sensor readings: {raw_readings}")
    print()
    
    # Step 2: Filter valid readings
    print("Step 2: Filtering valid readings (15°C to 30°C)...")
    valid_readings = filter_valid_readings(raw_readings, 15.0, 30.0)
    print(f"Valid readings: {valid_readings}")
    print()
    
    # Step 3: Calculate statistics
    print("Step 3: Calculating statistics...")
    statistics = calculate_statistics(valid_readings)
    print(f"Statistics: {statistics}")
    print()
    
    # Step 4: Detect anomalies
    print("Step 4: Detecting anomalies (2 standard deviations)...")
    anomalies = detect_anomalies(valid_readings, 2.0)
    print(f"Anomalies: {anomalies}")
    print()
    
    # Step 5: Generate report
    print("Step 5: Generating report...")
    generate_report(statistics, anomalies, len(raw_readings))
    
    return {
        "raw_readings": raw_readings,
        "valid_readings": valid_readings,
        "statistics": statistics,
        "anomalies": anomalies
    }

# Test the individual functions
print("Testing individual functions:")

# Test read_sensor_data
print("1. Testing read_sensor_data():")
sensor_data = read_sensor_data()
print(f"   Generated {len(sensor_data)} readings: {sensor_data[:5]}...")

# Test filter_valid_readings
print("\n2. Testing filter_valid_readings():")
valid_data = filter_valid_readings(sensor_data, 20.0, 25.0)
print(f"   Valid readings (20-25°C): {valid_data}")

# Test calculate_statistics
print("\n3. Testing calculate_statistics():")
stats = calculate_statistics(valid_data)
print(f"   Statistics: {stats}")

# Test detect_anomalies
print("\n4. Testing detect_anomalies():")
anomalies = detect_anomalies(valid_data, 1.5)
print(f"   Anomalies (1.5σ): {anomalies}")

# Test generate_report
print("\n5. Testing generate_report():")
generate_report(stats, anomalies, len(sensor_data))

# Run the complete pipeline
print("\n" + "=" * 60)
print("RUNNING COMPLETE DATA PROCESSING PIPELINE")
print("=" * 60)

result = process_sensor_data()

# Additional analysis
print("\nAdditional analysis:")
print(f"Data quality: {(len(result['valid_readings']) / len(result['raw_readings'])) * 100:.1f}% valid readings")
print(f"Temperature stability: {result['statistics']['range']:.1f}°C range")
if result['anomalies']:
    print(f"Anomaly rate: {(len(result['anomalies']) / len(result['valid_readings'])) * 100:.1f}%")

print("\n" + "=" * 50)
print("Task 8 completed successfully!")
print("=" * 50)
