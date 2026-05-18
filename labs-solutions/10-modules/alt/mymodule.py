"""This is a sample module for the lab."""

# print("Hello! I am the mymodule module.")  # This should only run once when imported

def greet(name):
    """Prints a greeting message."""
    print(f"Hello, {name}!")

class Scientist:
    """A simple class representing a scientist."""
    
    def __init__(self, name, field):
        self.name = name
        self.field = field

    def __str__(self):
        return f"{self.name} is a scientist in the field of {self.field}."

# Function to test __main__
def main():
    print("This should only run when executed directly.")

# Run only if executed directly (not when imported)
if __name__ == "__main__":
    main()

