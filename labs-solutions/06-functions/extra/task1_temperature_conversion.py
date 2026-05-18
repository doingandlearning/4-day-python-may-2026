# Lab 06 Extra - Task 1: Temperature Conversion Functions
# Practice with functions for temperature conversions

print("=" * 50)
print("Task 1: Temperature Conversion Functions")
print("=" * 50)

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    kelvin = celsius + 273.15
    return kelvin

def convert_temperature(temp, from_scale, to_scale):
    """Convert between any two temperature scales"""
    # First convert to Celsius
    if from_scale.lower() == 'fahrenheit':
        celsius = fahrenheit_to_celsius(temp)
    elif from_scale.lower() == 'kelvin':
        celsius = temp - 273.15
    else:  # already celsius
        celsius = temp
    
    # Then convert to target scale
    if to_scale.lower() == 'fahrenheit':
        return celsius_to_fahrenheit(celsius)
    elif to_scale.lower() == 'kelvin':
        return celsius_to_kelvin(celsius)
    else:  # celsius
        return celsius

# Test the basic conversion functions
test_temps = [0, 25, 100]
print("Temperature conversions:")
for temp in test_temps:
    f = celsius_to_fahrenheit(temp)
    k = celsius_to_kelvin(temp)
    print(f"{temp}°C = {f:.1f}°F = {k:.1f}K")

# Test the general conversion function
print("\nGeneral conversion function tests:")
print(f"25°C to Fahrenheit: {convert_temperature(25, 'celsius', 'fahrenheit'):.1f}°F")
print(f"77°F to Kelvin: {convert_temperature(77, 'fahrenheit', 'kelvin'):.1f}K")
print(f"300K to Celsius: {convert_temperature(300, 'kelvin', 'celsius'):.1f}°C")
print(f"212°F to Celsius: {convert_temperature(212, 'fahrenheit', 'celsius'):.1f}°C")

# Additional test cases
print("\nAdditional test cases:")
print(f"Freezing point: {convert_temperature(0, 'celsius', 'fahrenheit'):.1f}°F")
print(f"Boiling point: {convert_temperature(100, 'celsius', 'fahrenheit'):.1f}°F")
print(f"Room temperature: {convert_temperature(20, 'celsius', 'kelvin'):.1f}K")
print(f"Absolute zero: {convert_temperature(0, 'kelvin', 'celsius'):.1f}°C")

print("\n" + "=" * 50)
print("Task 1 completed successfully!")
print("=" * 50)
