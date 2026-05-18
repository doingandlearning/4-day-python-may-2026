"""Weather data processing module."""

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def average_temperature(temperatures):
    """Calculate the average temperature from a list."""
    if not temperatures:
        raise ValueError("Temperature list cannot be empty")
    return sum(temperatures) / len(temperatures)

def detect_anomalies(temperatures, threshold):
    """
    Identify temperature anomalies.
    Returns a list of temperatures that exceed the threshold.
    """
    return [temp for temp in temperatures if abs(temp) > threshold]

