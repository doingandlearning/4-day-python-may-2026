# Lab 07 Extra - Task 5: Scope and Function Composition
# Practice with scope in nested functions and lambda usage

print("=" * 50)
print("Task 5: Scope and Function Composition")
print("=" * 50)

# Global experiment counter
experiment_count = 0

print(f"Initial global experiment_count: {experiment_count}")

def run_experiment():
    """Run an experiment and demonstrate scope"""
    global experiment_count
    experiment_count += 1
    
    # Local variables inside the function
    temperature = 25.0 + (experiment_count * 0.5)  # Vary temperature slightly
    pressure = 101.3 + (experiment_count * 0.1)    # Vary pressure slightly
    
    print(f"\nRunning experiment #{experiment_count}:")
    print(f"  Local temperature: {temperature}°C")
    print(f"  Local pressure: {pressure} kPa")
    print(f"  Global experiment_count: {experiment_count}")
    
    def calculate_efficiency():
        """Nested function that uses local variables from outer function"""
        # This function can access the local variables from run_experiment
        efficiency = (temperature * pressure) / 1000  # Simple efficiency calculation
        
        # Use lambda inside the nested function
        temperature_f = lambda temp: temp * 9/5 + 32
        pressure_psi = lambda press: press * 0.145038
        
        print(f"  Inside calculate_efficiency:")
        print(f"    Can access temperature: {temperature}°C")
        print(f"    Can access pressure: {pressure} kPa")
        print(f"    Calculated efficiency: {efficiency:.3f}")
        print(f"    Temperature in Fahrenheit: {temperature_f(temperature):.1f}°F")
        print(f"    Pressure in PSI: {pressure_psi(pressure):.2f} psi")
        
        return efficiency
    
    # Call the nested function
    efficiency = calculate_efficiency()
    
    # Local variables are not accessible outside the function
    print(f"  Efficiency returned: {efficiency:.3f}")
    
    return efficiency

# Run several experiments
print("Running multiple experiments:")
efficiencies = []
for i in range(3):
    eff = run_experiment()
    efficiencies.append(eff)

print(f"\nFinal global experiment_count: {experiment_count}")
print(f"Efficiencies collected: {efficiencies}")

# Demonstrate scope with variable shadowing
print(f"\nDemonstrating variable shadowing:")

def scope_demonstration():
    """Demonstrate various scope concepts"""
    # Local variable
    x = "local_x"
    y = "local_y"
    
    print(f"Outer function - x: {x}, y: {y}")
    
    def inner_function():
        """Inner function with scope examples"""
        # This shadows the outer x
        x = "inner_x"
        
        # This modifies the outer y (if we use nonlocal)
        nonlocal y
        y = "modified_by_inner"
        
        # Lambda that uses local x
        process_x = lambda val: f"Processed: {val}"
        
        print(f"Inner function - x: {x}, y: {y}")
        print(f"Lambda result: {process_x(x)}")
        
        # Can still access global variables
        print(f"Can access global experiment_count: {experiment_count}")
    
    print(f"Before calling inner - x: {x}, y: {y}")
    inner_function()
    print(f"After calling inner - x: {x}, y: {y}")

scope_demonstration()

# Demonstrate lambda with closure
print(f"\nDemonstrating lambda with closure:")

def create_multiplier(factor):
    """Create a function that multiplies by a factor"""
    # This lambda "closes over" the factor variable
    return lambda x: x * factor

# Create different multipliers
double = create_multiplier(2)
triple = create_multiplier(3)
half = create_multiplier(0.5)

print(f"Double 5: {double(5)}")
print(f"Triple 5: {triple(5)}")
print(f"Half of 10: {half(10)}")

# Demonstrate lambda with multiple parameters
print(f"\nDemonstrating lambda with multiple parameters:")

def create_calculator():
    """Create a calculator with different operations"""
    operations = {
        'add': lambda x, y: x + y,
        'multiply': lambda x, y: x * y,
        'power': lambda x, y: x ** y,
        'divide': lambda x, y: x / y if y != 0 else float('inf')
    }
    return operations

calc = create_calculator()
print(f"Calculator operations:")
print(f"  5 + 3 = {calc['add'](5, 3)}")
print(f"  5 * 3 = {calc['multiply'](5, 3)}")
print(f"  5 ^ 3 = {calc['power'](5, 3)}")
print(f"  15 / 3 = {calc['divide'](15, 3)}")

# Demonstrate scope with global variable modification
print(f"\nDemonstrating global variable modification:")

def modify_global_counter():
    """Modify the global counter"""
    global experiment_count
    old_count = experiment_count
    experiment_count += 10
    print(f"Modified global counter from {old_count} to {experiment_count}")

print(f"Before modification: {experiment_count}")
modify_global_counter()
print(f"After modification: {experiment_count}")

# Demonstrate what happens without global keyword
def try_to_modify_without_global():
    """This will create a local variable instead of modifying global"""
    # This creates a local variable, doesn't modify the global
    experiment_count = 999
    print(f"Inside function (local variable): {experiment_count}")

print(f"\nBefore calling function without global: {experiment_count}")
try_to_modify_without_global()
print(f"After calling function without global: {experiment_count}")

print("\n" + "=" * 50)
print("Task 5 completed successfully!")
print("=" * 50)
