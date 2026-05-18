# Security System Threading Lab

This lab introduces Python threading concepts through a realistic security system simulation. Each exercise builds upon the previous one, gradually introducing more complex threading concepts.

## Lab Structure

### Exercise 1: Basic Sensor Threads
**Concepts:** Thread creation, basic threading, thread arguments
- Create individual sensor threads (door, motion, temperature)
- Learn basic thread creation and starting

### Exercise 2: Multiple Sensors with Timing
**Concepts:** Multiple threads, random timing, concurrent execution
- Run multiple sensors simultaneously with different timing patterns
- Observe thread interleaving and concurrent output

### Exercise 3: Thread Communication with Queues
**Concepts:** Thread communication, queues, event handling
- Use queues to pass data between threads
- Implement basic event processing

### Exercise 4: Timers and Scheduled Tasks
**Concepts:** Timer threads, scheduled execution, periodic tasks
- Add timer-based features like periodic status checks
- Implement scheduled security scans

### Exercise 5: Thread Synchronization with Locks
**Concepts:** Thread safety, locks, shared resources
- Protect shared data with locks
- Implement thread-safe logging and state management

### Exercise 6: Complete Security System
**Concepts:** Integration, real-world application, advanced patterns
- Combine all concepts into a complete security monitoring system
- Implement alarm logic and system state management

## Learning Objectives

By completing this lab, you will understand:

1. **Basic Threading** - Creating and starting threads
2. **Thread Communication** - Passing data between threads using queues
3. **Thread Synchronization** - Using locks to protect shared resources
4. **Timers** - Scheduled and periodic task execution
5. **Real-world Applications** - How threading applies to actual systems
6. **Thread Safety** - Writing code that works correctly with multiple threads

## Prerequisites

- Basic Python knowledge
- Understanding of functions and classes
- Familiarity with file I/O operations

## Getting Started

1. Start with Exercise 1 and work through them sequentially
2. Each exercise includes starter code and detailed instructions
3. Complete the TODO items in each exercise
4. Test your solutions and compare with the provided solutions
5. Experiment with different parameters and configurations

## Files

- `exercise_01_basic_sensors.py` - Basic thread creation
- `exercise_02_multiple_sensors.py` - Multiple threads with timing
- `exercise_03_thread_communication.py` - Queues and event handling
- `exercise_04_timers.py` - Timer-based features
- `exercise_05_synchronization.py` - Locks and thread safety
- `exercise_06_complete_system.py` - Full security system
- `solutions/` - Complete solutions for each exercise
