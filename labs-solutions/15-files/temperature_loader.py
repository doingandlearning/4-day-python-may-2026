import csv

class TemperatureReading:
    """Class representing temperature info"""

    def __init__(self, temp, date, location, scale="Celsius"):
        self.temp = temp
        self.date = date
        self.location = location
        self.scale = scale

    def __str__(self):
        return f"TemperatureReading[{self.scale}]({self.temp} on {self.date} at {self.location})"

    def __repr__(self):
        return f"TemperatureReading({self.temp}, {self.date}, {self.location}, {self.scale})"


def load_data(filename):
    """
    Reads a CSV file and loads temperature readings.
    
    :param filename: Name of the file to load
    :return: List of TemperatureReading instances
    """
    readings = []

    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 4:
                    print(f"Skipping malformed row: {row}")
                    continue
                
                try:
                    temp = float(row[0])  # Convert temperature to float
                    scale = row[1]        # Temperature scale (Celsius, Fahrenheit, etc.)
                    date = row[2]         # Date of the reading
                    location = row[3]     # Location of the measurement

                    reading = TemperatureReading(temp, date, location, scale)
                    readings.append(reading)
                except ValueError:
                    print(f"Skipping invalid temperature value in row: {row}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    
    return readings


# Prompt user for a filename and load data
filename = input("Please enter the data file to load (default: data.csv): ").strip()
if not filename:
    filename = "data.csv"

temperatures = load_data(filename)

# Display results
if temperatures:
    print(f"\nLoaded {len(temperatures)} temperature readings:")
    for temp in temperatures:
        print(temp)
else:
    print("No valid temperature data loaded.")
