# Lab 07 Extra - Task 2: Scope Practice with Scientific Calculations
# Practice with local vs global scope in scientific calculations

print("=" * 50)
print("Task 2: Scope Practice with Scientific Calculations")
print("=" * 50)

# Global variables
PI = 3.14159
GRAVITY = 9.81  # m/s²
experiment_count = 0

print("Global variables defined:")
print(f"PI = {PI}")
print(f"GRAVITY = {GRAVITY} m/s²")
print(f"experiment_count = {experiment_count}")

def calculate_circle_area(radius):
    """Calculate circle area using global PI"""
    # This function can read the global PI variable
    area = PI * radius ** 2
    print(f"Inside calculate_circle_area: PI = {PI}")
    return area

def calculate_pendulum_period(length):
    """Calculate pendulum period using global GRAVITY"""
    # This function can read the global GRAVITY variable
    period = 2 * PI * (length / GRAVITY) ** 0.5
    
    # Create local variables inside the function
    frequency = 1 / period
    local_gravity = GRAVITY * 0.1  # Local variable with different value
    
    print(f"Inside calculate_pendulum_period:")
    print(f"  Global GRAVITY = {GRAVITY}")
    print(f"  Local local_gravity = {local_gravity}")
    print(f"  Local frequency = {frequency:.4f} Hz")
    
    return period

def increment_experiment_counter():
    """Modify global experiment counter"""
    global experiment_count  # Need global keyword to modify global variable
    experiment_count += 1
    print(f"Experiment counter incremented to: {experiment_count}")

def demonstrate_scope_confusion():
    """Demonstrate scope confusion with variable shadowing"""
    # This function has a local variable with same name as global
    PI = 3.0  # This shadows the global PI
    print(f"Inside demonstrate_scope_confusion:")
    print(f"  Local PI = {PI}")
    print(f"  Global PI (accessed with globals()) = {globals()['PI']}")

# Test the functions
print("\nTesting calculate_circle_area:")
radius = 5.0
area = calculate_circle_area(radius)
print(f"Area of circle with radius {radius}: {area:.2f}")

print(f"\nGlobal PI is still: {PI}")

print("\nTesting calculate_pendulum_period:")
length = 1.0  # 1 meter pendulum
period = calculate_pendulum_period(length)
print(f"Period of {length}m pendulum: {period:.3f} seconds")

print(f"\nGlobal GRAVITY is still: {GRAVITY}")

print("\nTesting global variable modification:")
print(f"Initial experiment_count: {experiment_count}")
increment_experiment_counter()
increment_experiment_counter()
print(f"Final experiment_count: {experiment_count}")

print("\nTesting scope confusion:")
demonstrate_scope_confusion()
print(f"Global PI is still: {PI}")

# Demonstrate what happens when you try to modify global without global keyword
def try_to_modify_global():
    """This will cause an error if we try to modify global without global keyword"""
    print("Trying to modify global without 'global' keyword...")
    # This would cause an error:
    # experiment_count += 1  # UnboundLocalError!
    print("(Skipping the error for demonstration)")

try_to_modify_global()

# Additional scope examples
print("\nAdditional scope examples:")

def nested_scope_example():
    """Demonstrate nested scope"""
    outer_var = "I'm in the outer function"
    
    def inner_function():
        """Inner function can access outer function's variables"""
        print(f"Inner function can see: {outer_var}")
        print(f"Inner function can see global PI: {PI}")
        
        # Inner function can modify outer function's variables
        nonlocal outer_var
        outer_var = "Modified by inner function"
        print(f"Inner function modified outer_var to: {outer_var}")
    
    print(f"Before calling inner function: {outer_var}")
    inner_function()
    print(f"After calling inner function: {outer_var}")

print("\nTesting nested scope:")
nested_scope_example()

# Demonstrate variable shadowing in nested functions
def shadowing_example():
    """Demonstrate variable shadowing"""
    x = "outer"
    
    def inner():
        x = "inner"  # This shadows the outer x
        print(f"Inside inner function: x = {x}")
    
    print(f"Before calling inner: x = {x}")
    inner()
    print(f"After calling inner: x = {x}")

print("\nTesting variable shadowing:")
shadowing_example()

print("\n" + "=" * 50)
print("Task 2 completed successfully!")
print("=" * 50)
