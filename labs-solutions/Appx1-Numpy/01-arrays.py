import numpy as np
import time

# EXERCISE 1: Array Creation
# Create the following arrays:
# 1. An array of integers from 5 to 15
arr1 = np.arange(5, 16)  # Remember arange is exclusive of the end value
print("Array from 5 to 15:", arr1)

# 2. An array with exactly 8 evenly spaced values between 0 and 100 (inclusive)
arr2 = np.linspace(0, 100, 8)
print("8 evenly spaced values from 0 to 100:", arr2)

# 3. A 3x3 matrix of zeros
arr3 = np.zeros((3, 3))
print("3x3 matrix of zeros:")
print(arr3)


# EXERCISE 2: Array Reshaping and Slicing
# 1. Create an array of numbers from 1 to 12
arr4 = np.arange(1, 13)
print("Array from 1 to 12:", arr4)

# 2. Reshape it into a 3x4 matrix
reshaped = arr4.reshape(3, 4)
print("Reshaped into 3x4 matrix:")
print(reshaped)

# 3. Extract the second row
second_row = reshaped[1, :]  # or simply reshaped[1]
print("Second row:", second_row)

# 4. Extract the element at position (1,2) (second row, third column)
element = reshaped[1, 2]
print("Element at position (1,2):", element)


# EXERCISE 3: Element-wise Operations
# 1. Create two arrays: one with values [10, 20, 30, 40, 50] and another with values [5, 4, 3, 2, 1]
arr5 = np.array([10, 20, 30, 40, 50])
arr6 = np.array([5, 4, 3, 2, 1])

# 2. Perform element-wise operations
print("Element-wise addition:", arr5 + arr6)
print("Element-wise subtraction:", arr5 - arr6)
print("Element-wise multiplication:", arr5 * arr6)
print("Element-wise division:", arr5 / arr6)

# 3. Calculate the square root of each element in the first array
sqrt_arr5 = np.sqrt(arr5)
print("Square root of first array:", sqrt_arr5)


# EXERCISE 4: Performance Comparison
# Compare the time it takes to perform element-wise multiplication on large Python lists vs NumPy arrays
def compare_performance(size=10**6):
    # Python list approach
    list1 = list(range(1, size+1))
    list2 = list(range(1, size+1))
    
    start_time = time.time()
    # Multiply list1 and list2 element-wise using a list comprehension
    result_list = [a * b for a, b in zip(list1, list2)]
    
    python_time = time.time() - start_time
    print(f"Python list multiplication took: {python_time:.6f} seconds")
    
    # NumPy approach
    arr1 = np.arange(1, size+1)
    arr2 = np.arange(1, size+1)
    
    start_time = time.time()
    # Multiply arr1 and arr2 element-wise using NumPy's vectorization
    result_arr = arr1 * arr2
    
    numpy_time = time.time() - start_time
    print(f"NumPy array multiplication took: {numpy_time:.6f} seconds")
    print(f"NumPy is approximately {python_time/numpy_time:.1f}x faster")

# Run the performance comparison with a smaller size for testing
compare_performance(size=10**5)

# BONUS CHALLENGE: Broadcasting
# 1. Create a 3x3 matrix of random integers between 1 and 10
random_matrix = np.random.randint(1, 11, size=(3, 3))
print("Random 3x3 matrix:")
print(random_matrix)

# 2. Subtract 5 from each element
subtracted = random_matrix - 5
print("After subtracting 5:")
print(subtracted)

# 3. Multiply each row by [1, 2, 3] (hint: use broadcasting)
multiplier = np.array([1, 2, 3])
result = random_matrix * multiplier  # Broadcasting in action
print("After multiplying each row by [1, 2, 3]:")
print(result)