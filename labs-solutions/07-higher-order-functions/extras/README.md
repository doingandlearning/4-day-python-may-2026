# Lab 07 Extra Solutions: Lambda Functions, Scope, and Practical Applications

This directory contains solutions for the Lab 07 Extra practice exercises focused on lambda functions, variable scope, and practical applications for engineers and scientists.

## Files Overview

### Individual Task Solutions
- `task1_sorting_scientific_data.py` - Lambda functions for sorting experimental data
- `task2_scope_practice.py` - Local vs global scope with scientific calculations
- `task3_lambda_data_processing.py` - Lambda functions for processing sensor data
- `task4_engineering_applications.py` - Practical engineering material selection
- `task5_scope_function_composition.py` - Scope in nested functions and composition
- `task6_lambda_statistical_analysis.py` - Lambda functions for statistical analysis
- `task7_complex_sorting.py` - Complex sorting with multiple criteria
- `task8_scope_demonstration.py` - Comprehensive scope demonstration

### Main Runner
- `run_all_lambda_scope_tasks.py` - Executes all tasks in sequence

## How to Use

### Run Individual Tasks
```bash
python task1_sorting_scientific_data.py
python task2_scope_practice.py
# ... etc for each task
```

### Run All Tasks
```bash
python run_all_lambda_scope_tasks.py
```

## Learning Objectives

Each task reinforces specific concepts:

1. **Task 1**: Lambda functions for sorting with custom criteria
2. **Task 2**: Understanding local vs global scope
3. **Task 3**: Lambda functions with map(), filter(), and data processing
4. **Task 4**: Practical engineering applications with material selection
5. **Task 5**: Scope in nested functions and function composition
6. **Task 6**: Lambda functions for statistical calculations
7. **Task 7**: Complex sorting with multiple criteria
8. **Task 8**: Comprehensive scope demonstration with closures

## Key Concepts Practiced

### **Lambda Functions**
- **Sorting with custom keys** - most practical use case
- **Data processing** with map() and filter()
- **Statistical calculations** for quick computations
- **Engineering applications** for material analysis

### **Scope (Local vs Global)**
- **Global variables** - accessible everywhere
- **Local variables** - only accessible within their function
- **Variable shadowing** - local variables hide globals with same name
- **Nonlocal keyword** - modifying outer function variables
- **Closures** - functions that "remember" their environment

### **Practical Applications**
- **Scientific data analysis** - experimental data processing
- **Engineering material selection** - cost and performance analysis
- **Sensor data processing** - real-world IoT applications
- **Statistical analysis** - data science fundamentals

## Scientific Context

All examples use realistic scientific and engineering scenarios:
- **Experimental data** with temperature, pressure, and results
- **Sensor readings** with timestamps and status
- **Material properties** for engineering decisions
- **Equipment analysis** with efficiency and maintenance costs
- **Statistical analysis** of measurement data

## When to Use Lambdas

### **Good Uses:**
- **Sorting with custom criteria** - `sorted(data, key=lambda x: x.field)`
- **Simple transformations** - `map(lambda x: x*2, numbers)`
- **Simple filtering** - `filter(lambda x: x > 0, numbers)`
- **One-time calculations** that don't need a full function

### **Avoid When:**
- **Complex logic** - use regular functions instead
- **Multiple statements** - lambdas should be simple
- **Repeated use** - define a named function
- **Readability suffers** - clarity is more important than brevity

## Scope Best Practices

### **Global Variables:**
- **Use sparingly** - only for truly global state
- **Use `global` keyword** when modifying from functions
- **Consider alternatives** like passing parameters

### **Local Variables:**
- **Prefer local** over global when possible
- **Use meaningful names** to avoid confusion
- **Understand shadowing** - local variables hide globals

### **Nested Functions:**
- **Can access outer function variables** - closure behavior
- **Use `nonlocal`** to modify outer function variables
- **Great for encapsulation** and data hiding
