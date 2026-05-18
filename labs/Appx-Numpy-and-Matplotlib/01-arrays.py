import numpy as np
import time

# EXERCISE 1: Array Creation
# Create the following arrays:
# 1. An array of integers from 5 to 15
# 2. An array with exactly 8 evenly spaced values between 0 and 100 (inclusive)
# 3. A 3x3 matrix of zeros
# YOUR CODE HERE:




# EXERCISE 2: Array Reshaping and Slicing
# 1. Create an array of numbers from 1 to 12
# 2. Reshape it into a 3x4 matrix
# 3. Extract the second row
# 4. Extract the element at position (1,2) (second row, third column)
# YOUR CODE HERE:




# EXERCISE 3: Element-wise Operations
# 1. Create two arrays: one with values [10, 20, 30, 40, 50] and another with values [5, 4, 3, 2, 1]
# 2. Perform element-wise addition, subtraction, multiplication, and division
# 3. Calculate the square root of each element in the first array
# YOUR CODE HERE:




# EXERCISE 4: Performance Comparison
# Compare the time it takes to perform element-wise multiplication on large Python lists vs NumPy arrays
def compare_performance(size=10**6):
    # Python list approach
    list1 = list(range(1, size+1))
    list2 = list(range(1, size+1))
    
    start_time = time.time()
    # Multiply list1 and list2 element-wise using a list comprehension
    # YOUR CODE HERE:
    
    
    python_time = time.time() - start_time
    print(f"Python list multiplication took: {python_time:.6f} seconds")
    
    # NumPy approach
    arr1 = np.arange(1, size+1)
    arr2 = np.arange(1, size+1)
    
    start_time = time.time()
    # Multiply arr1 and arr2 element-wise using NumPy's vectorization
    # YOUR CODE HERE:
    
    
    numpy_time = time.time() - start_time
    print(f"NumPy array multiplication took: {numpy_time:.6f} seconds")
    print(f"NumPy is approximately {python_time/numpy_time:.1f}x faster")

# Run the performance comparison with a smaller size for testing
compare_performance(size=10**5)

# BONUS CHALLENGE: Broadcasting
# 1. Create a 3x3 matrix of random integers between 1 and 10
# 2. Subtract 5 from each element
# 3. Multiply each row by [1, 2, 3] (hint: use broadcasting)
# YOUR CODE HERE: