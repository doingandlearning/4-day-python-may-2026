# Lab 07 Extra - Task 8: Scope Demonstration with Nested Functions
# Comprehensive example showing scope in action with nested functions

print("=" * 50)
print("Task 8: Scope Demonstration with Nested Functions")
print("=" * 50)

# Global variable
lab_temperature = 22.0
experiment_id = 0

print(f"Global variables initialized:")
print(f"  lab_temperature = {lab_temperature}°C")
print(f"  experiment_id = {experiment_id}")

def analyze_sample(sample_temperature):
    """Analyze a sample and demonstrate scope concepts"""
    global experiment_id
    experiment_id += 1
    
    # Local variables inside the function
    sample_id = f"SAMPLE_{experiment_id:03d}"
    temperature_difference = sample_temperature - lab_temperature
    analysis_time = 5.0  # minutes
    
    print(f"\n--- Analyzing {sample_id} ---")
    print(f"Global lab_temperature: {lab_temperature}°C")
    print(f"Sample temperature: {sample_temperature}°C")
    print(f"Local temperature_difference: {temperature_difference}°C")
    print(f"Local analysis_time: {analysis_time} minutes")
    
    def calculate_deviation():
        """Nested function that uses both global and local variables"""
        # This function can access:
        # - Global variables (lab_temperature, experiment_id)
        # - Local variables from outer function (sample_temperature, temperature_difference)
        
        # Use lambda inside the nested function for calculations
        temperature_f = lambda temp: temp * 9/5 + 32
        deviation_percent = lambda diff, base: (diff / base) * 100
        
        print(f"  Inside calculate_deviation:")
        print(f"    Can access global lab_temperature: {lab_temperature}°C")
        print(f"    Can access global experiment_id: {experiment_id}")
        print(f"    Can access local sample_temperature: {sample_temperature}°C")
        print(f"    Can access local temperature_difference: {temperature_difference}°C")
        
        # Lambda calculations
        lab_temp_f = temperature_f(lab_temperature)
        sample_temp_f = temperature_f(sample_temperature)
        deviation = deviation_percent(temperature_difference, lab_temperature)
        
        print(f"    Lab temperature in Fahrenheit: {lab_temp_f:.1f}°F")
        print(f"    Sample temperature in Fahrenheit: {sample_temp_f:.1f}°F")
        print(f"    Temperature deviation: {deviation:.1f}%")
        
        return {
            'deviation_percent': deviation,
            'lab_temp_f': lab_temp_f,
            'sample_temp_f': sample_temp_f
        }
    
    def quality_assessment():
        """Another nested function demonstrating scope"""
        # Create local variables that shadow outer function variables
        temperature_difference = abs(temperature_difference)  # This shadows the outer variable
        
        # Lambda for quality scoring
        quality_score = lambda diff: max(0, 100 - diff * 10)
        
        print(f"  Inside quality_assessment:")
        print(f"    Local temperature_difference (absolute): {temperature_difference}°C")
        print(f"    Outer temperature_difference (original): {sample_temperature - lab_temperature}°C")
        
        score = quality_score(temperature_difference)
        print(f"    Quality score: {score}/100")
        
        return score
    
    # Call the nested functions
    deviation_data = calculate_deviation()
    quality_score = quality_assessment()
    
    # Local variables are not accessible outside the function
    print(f"  Analysis complete for {sample_id}")
    print(f"  Quality score: {quality_score}")
    
    return {
        'sample_id': sample_id,
        'deviation_data': deviation_data,
        'quality_score': quality_score
    }

# Test the function with different samples
print("\nTesting analyze_sample with different samples:")

samples = [25.5, 20.0, 28.3, 18.7, 24.1]
results = []

for temp in samples:
    result = analyze_sample(temp)
    results.append(result)

print(f"\nGlobal variables after analysis:")
print(f"  lab_temperature: {lab_temperature}°C (unchanged)")
print(f"  experiment_id: {experiment_id} (modified)")

# Demonstrate variable shadowing
print(f"\nDemonstrating variable shadowing:")

def shadowing_demonstration():
    """Demonstrate variable shadowing with global variables"""
    # Create local variables with same names as globals
    lab_temperature = 30.0  # This shadows the global
    experiment_id = 999     # This shadows the global
    
    print(f"Inside shadowing_demonstration:")
    print(f"  Local lab_temperature: {lab_temperature}°C")
    print(f"  Local experiment_id: {experiment_id}")
    print(f"  Global lab_temperature (via globals()): {globals()['lab_temperature']}°C")
    print(f"  Global experiment_id (via globals()): {globals()['experiment_id']}")
    
    def inner_function():
        """Inner function showing scope inheritance"""
        # This function sees the local variables from the outer function
        print(f"    Inside inner_function:")
        print(f"      lab_temperature: {lab_temperature}°C (from outer function)")
        print(f"      experiment_id: {experiment_id} (from outer function)")
        
        # Can still access globals if needed
        print(f"      Global lab_temperature: {globals()['lab_temperature']}°C")
    
    inner_function()

shadowing_demonstration()

print(f"\nGlobal variables after shadowing demonstration:")
print(f"  lab_temperature: {lab_temperature}°C (unchanged)")
print(f"  experiment_id: {experiment_id} (unchanged)")

# Demonstrate nonlocal keyword
print(f"\nDemonstrating nonlocal keyword:")

def nonlocal_demonstration():
    """Demonstrate nonlocal keyword usage"""
    counter = 0
    
    def increment_counter():
        nonlocal counter  # This allows modifying the outer function's variable
        counter += 1
        print(f"    Counter incremented to: {counter}")
    
    def create_incrementer():
        """Return a function that increments the counter"""
        return lambda: increment_counter()
    
    print(f"Initial counter: {counter}")
    increment_counter()
    increment_counter()
    
    # Create a function that increments the counter
    inc_func = create_incrementer()
    inc_func()
    inc_func()
    
    print(f"Final counter: {counter}")

nonlocal_demonstration()

# Demonstrate closure with lambda
print(f"\nDemonstrating closure with lambda:")

def create_temperature_converter(base_temp):
    """Create a temperature converter with a base temperature"""
    # This lambda "closes over" the base_temp variable
    return lambda sample_temp: {
        'celsius_diff': sample_temp - base_temp,
        'fahrenheit_diff': (sample_temp - base_temp) * 9/5,
        'percent_diff': ((sample_temp - base_temp) / base_temp) * 100
    }

# Create different converters
room_temp_converter = create_temperature_converter(20.0)
lab_temp_converter = create_temperature_converter(lab_temperature)

print(f"Room temperature converter (base: 20°C):")
for temp in [18.0, 22.0, 25.0]:
    result = room_temp_converter(temp)
    print(f"  {temp}°C: {result}")

print(f"\nLab temperature converter (base: {lab_temperature}°C):")
for temp in [20.0, 24.0, 26.0]:
    result = lab_temp_converter(temp)
    print(f"  {temp}°C: {result}")

# Demonstrate scope with class-like behavior using nested functions
print(f"\nDemonstrating class-like behavior with nested functions:")

def create_equipment_monitor(equipment_name):
    """Create an equipment monitor with state"""
    # "Private" variables (local to the outer function)
    _status = "OFF"
    _temperature = 20.0
    _runtime_hours = 0.0
    
    def get_status():
        return _status
    
    def set_status(new_status):
        nonlocal _status
        _status = new_status
        print(f"  {equipment_name} status changed to: {_status}")
    
    def update_temperature(new_temp):
        nonlocal _temperature
        _temperature = new_temp
        print(f"  {equipment_name} temperature updated to: {_temperature}°C")
    
    def add_runtime(hours):
        nonlocal _runtime_hours
        _runtime_hours += hours
        print(f"  {equipment_name} runtime increased by {hours}h to {_runtime_hours}h")
    
    def get_info():
        return {
            'name': equipment_name,
            'status': _status,
            'temperature': _temperature,
            'runtime': _runtime_hours
        }
    
    # Return a dictionary of functions (like methods)
    return {
        'get_status': get_status,
        'set_status': set_status,
        'update_temperature': update_temperature,
        'add_runtime': add_runtime,
        'get_info': get_info
    }

# Create equipment monitors
pump_monitor = create_equipment_monitor("Pump_A")
compressor_monitor = create_equipment_monitor("Compressor_B")

print(f"Equipment monitors created:")
print(f"  Pump_A info: {pump_monitor['get_info']()}")
print(f"  Compressor_B info: {compressor_monitor['get_info']()}")

# Use the monitors
pump_monitor['set_status']("ON")
pump_monitor['update_temperature'](25.5)
pump_monitor['add_runtime'](2.5)

compressor_monitor['set_status']("STANDBY")
compressor_monitor['update_temperature'](18.0)

print(f"\nAfter operations:")
print(f"  Pump_A info: {pump_monitor['get_info']()}")
print(f"  Compressor_B info: {compressor_monitor['get_info']()}")

print("\n" + "=" * 50)
print("Task 8 completed successfully!")
print("=" * 50)
