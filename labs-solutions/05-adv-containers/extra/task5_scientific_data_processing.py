# Lab 05 Extra - Task 5: Scientific Data Processing with List Comprehensions
# Practice with list comprehensions for scientific data

print("=" * 50)
print("Task 5: Scientific Data Processing with List Comprehensions")
print("=" * 50)

# Sample data
temperatures = [20.5, 22.1, 18.7, 25.3, 19.8, 23.6, 21.2, 24.9, 17.4, 26.1]
elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron"]

print("Original temperatures (°C):", temperatures)
print("Original elements:", elements)

# Create a list of temperatures converted to Kelvin (K = C + 273.15)
kelvin_temps = [temp + 273.15 for temp in temperatures]
print(f"\nTemperatures in Kelvin: {kelvin_temps}")

# Create a list of even-indexed temperatures
even_indexed_temps = [temperatures[i] for i in range(0, len(temperatures), 2)]
print(f"Even-indexed temperatures: {even_indexed_temps}")

# Create a list of odd-indexed temperatures
odd_indexed_temps = [temperatures[i] for i in range(1, len(temperatures), 2)]
print(f"Odd-indexed temperatures: {odd_indexed_temps}")

# Create a list of temperatures above 22°C
high_temps = [temp for temp in temperatures if temp > 22]
print(f"Temperatures above 22°C: {high_temps}")

# Create a list of element name lengths
element_lengths = [len(element) for element in elements]
print(f"Element name lengths: {element_lengths}")

# Create a list of elements that start with 'H'
h_elements = [element for element in elements if element.startswith('H')]
print(f"Elements starting with 'H': {h_elements}")

# Create a list of elements longer than 6 characters
long_elements = [element for element in elements if len(element) > 6]
print(f"Elements longer than 6 characters: {long_elements}")

# Create a list of tuples (element, length) for each element
element_info = [(element, len(element)) for element in elements]
print(f"Element info (name, length): {element_info}")

# Additional list comprehension examples for practice
print("\nAdditional examples:")

# Create a list of temperatures rounded to 1 decimal place
rounded_temps = [round(temp, 1) for temp in temperatures]
print(f"Rounded temperatures: {rounded_temps}")

# Create a list of elements in uppercase
upper_elements = [element.upper() for element in elements]
print(f"Elements in uppercase: {upper_elements}")

# Create a list of temperatures with their status (hot/cold)
temp_status = ["hot" if temp > 22 else "cold" for temp in temperatures]
print(f"Temperature status: {temp_status}")

# Create a list of elements with their first letter
first_letters = [element[0] for element in elements]
print(f"First letters of elements: {first_letters}")

print("\n" + "=" * 50)
print("Task 5 completed successfully!")
print("=" * 50)
