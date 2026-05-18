import mymodule
from mymodule import greet
from mymodule import Scientist as Sci  # Import with alias
import mymodule as mod  # Import entire module with alias
import sys
import math
import random

print("\n--- Using mymodule ---")
greet("Alice")  # Calling function from mymodule
scientist1 = mymodule.Scientist("Dr. Alice", "Biology")
print(scientist1)

print("\n--- Using dir() on mymodule ---")
print(dir(mymodule))  # List all attributes in mymodule

print("\n--- Module Properties ---")
print("Module Name:", mymodule.__name__)
print("Module Doc:", mymodule.__doc__)

print("\n--- Using Different Import Techniques ---")
greet("Bob")  # Using function imported directly
scientist2 = Sci("Dr. Eve", "Physics")  # Using Scientist with alias
print(scientist2)

mod.greet("Charlie")  # Using module alias

print("\n--- Using Built-in Modules ---")
print("Python Version:", sys.version)
print("Square root of 25:", math.sqrt(25))
print("Random number:", random.randint(1, 100))

