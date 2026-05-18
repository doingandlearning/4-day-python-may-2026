# Lab 04 Extra: Practice with Lists and Tuples - Solution

# Task 1: Student Grade Tracker
print("=" * 40)
print("Task 1: Student Grade Tracker")
print("=" * 40)

grades = [
    ("Alice", 85), ("Bob", 92), ("Charlie", 78), 
    ("Diana", 96), ("Eve", 88), ("Frank", 73)
]

# Print all student names
print("Student names:")
for name, grade in grades:
    print(name)

# Print all grades
print("\nAll grades:")
for name, grade in grades:
    print(grade)

# Find the highest grade
highest = grades[0][1]  # Start with first grade
for name, grade in grades:
    if grade > highest:
        highest = grade
print(f"\nHighest grade: {highest}")

# Find the lowest grade
lowest = grades[0][1]  # Start with first grade
for name, grade in grades:
    if grade < lowest:
        lowest = grade
print(f"Lowest grade: {lowest}")

# Calculate the average grade
total = 0
for name, grade in grades:
    total += grade
average = total / len(grades)
print(f"Average grade: {average}")

# Print students with grades above 85
print("\nStudents with grades above 85:")
for name, grade in grades:
    if grade > 85:
        print(f"{name}: {grade}")

# Task 2: Shopping List Manager
print("\n" + "=" * 40)
print("Task 2: Shopping List Manager")
print("=" * 40)

shopping_list = ["apples", "bananas", "milk", "bread", "eggs"]

# Print the shopping list
print("Original shopping list:")
for item in shopping_list:
    print(f"- {item}")

# Add "cheese" to the end
shopping_list.append("cheese")
print("\nAfter adding 'cheese':")
for item in shopping_list:
    print(f"- {item}")

# Add "butter" at position 2
shopping_list.insert(2, "butter")
print("\nAfter adding 'butter' at position 2:")
for item in shopping_list:
    print(f"- {item}")

# Remove "milk" from the list
shopping_list.remove("milk")
print("\nAfter removing 'milk':")
for item in shopping_list:
    print(f"- {item}")

# Print the first 3 items
print("\nFirst 3 items:")
for i in range(3):
    print(f"- {shopping_list[i]}")

# Print the last 2 items
print("\nLast 2 items:")
for i in range(-2, 0):
    print(f"- {shopping_list[i]}")

# Check if "bread" is in the list
if "bread" in shopping_list:
    print("\nYes, 'bread' is in the list")
else:
    print("\nNo, 'bread' is not in the list")

# Print the length of the list
print(f"\nLength of shopping list: {len(shopping_list)}")

# Task 3: Number Analysis
print("\n" + "=" * 40)
print("Task 3: Number Analysis")
print("=" * 40)

numbers = [15, 23, 8, 42, 17, 31, 6, 55, 29, 12]

# Print all numbers
print("All numbers:")
for num in numbers:
    print(num)

# Count how many numbers are even
even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
print(f"\nEven numbers count: {even_count}")

# Count how many numbers are odd
odd_count = 0
for num in numbers:
    if num % 2 == 1:
        odd_count += 1
print(f"Odd numbers count: {odd_count}")

# Find the largest number
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(f"Largest number: {largest}")

# Find the smallest number
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print(f"Smallest number: {smallest}")

# Print numbers greater than 20
print("\nNumbers greater than 20:")
for num in numbers:
    if num > 20:
        print(num)

# Print numbers between 10 and 30
print("\nNumbers between 10 and 30:")
for num in numbers:
    if 10 < num < 30:
        print(num)

# Calculate the sum of all numbers
total = 0
for num in numbers:
    total += num
print(f"\nSum of all numbers: {total}")

# Task 4: Coordinate Pairs
print("\n" + "=" * 40)
print("Task 4: Coordinate Pairs")
print("=" * 40)

coordinates = [(0, 0), (3, 4), (1, 1), (5, 12), (2, 2)]

# Print all coordinates
print("All coordinates:")
for coord in coordinates:
    print(coord)

# Print just the x-coordinates
print("\nX-coordinates:")
for x, y in coordinates:
    print(x)

# Print just the y-coordinates
print("\nY-coordinates:")
for x, y in coordinates:
    print(y)

# Find the coordinate with the largest x-value
largest_x = coordinates[0]
for coord in coordinates:
    if coord[0] > largest_x[0]:
        largest_x = coord
print(f"\nCoordinate with largest x-value: {largest_x}")

# Find the coordinate with the largest y-value
largest_y = coordinates[0]
for coord in coordinates:
    if coord[1] > largest_y[1]:
        largest_y = coord
print(f"Coordinate with largest y-value: {largest_y}")

# Print coordinates where both x and y are greater than 2
print("\nCoordinates where both x and y > 2:")
for x, y in coordinates:
    if x > 2 and y > 2:
        print((x, y))

# Task 5: Temperature Readings
print("\n" + "=" * 40)
print("Task 5: Temperature Readings")
print("=" * 40)

temperatures = [
    ("Monday", 22), ("Tuesday", 25), ("Wednesday", 23),
    ("Thursday", 27), ("Friday", 24), ("Saturday", 26), ("Sunday", 21)
]

# Print all temperatures
print("All temperatures:")
for day, temp in temperatures:
    print(f"{day}: {temp}°C")

# Find the hottest day
hottest = temperatures[0]
for day, temp in temperatures:
    if temp > hottest[1]:
        hottest = (day, temp)
print(f"\nHottest day: {hottest[0]} with {hottest[1]}°C")

# Find the coldest day
coldest = temperatures[0]
for day, temp in temperatures:
    if temp < coldest[1]:
        coldest = (day, temp)
print(f"Coldest day: {coldest[0]} with {coldest[1]}°C")

# Print days with temperature above 24
print("\nDays with temperature above 24°C:")
for day, temp in temperatures:
    if temp > 24:
        print(f"{day}: {temp}°C")

# Print days with temperature below 25
print("\nDays with temperature below 25°C:")
for day, temp in temperatures:
    if temp < 25:
        print(f"{day}: {temp}°C")

# Calculate the average temperature
total_temp = 0
for day, temp in temperatures:
    total_temp += temp
average_temp = total_temp / len(temperatures)
print(f"\nAverage temperature: {average_temp:.1f}°C")

# Task 6: Word List Operations
print("\n" + "=" * 40)
print("Task 6: Word List Operations")
print("=" * 40)

words = ["python", "programming", "computer", "science", "data", "analysis"]

# Print all words
print("All words:")
for word in words:
    print(word)

# Print words longer than 6 characters
print("\nWords longer than 6 characters:")
for word in words:
    if len(word) > 6:
        print(word)

# Print words that start with 'p'
print("\nWords that start with 'p':")
for word in words:
    if word[0] == 'p':
        print(word)

# Print words that end with 'n'
print("\nWords that end with 'n':")
for word in words:
    if word[-1] == 'n':
        print(word)

# Count how many words have exactly 5 letters
count_5_letters = 0
for word in words:
    if len(word) == 5:
        count_5_letters += 1
print(f"\nWords with exactly 5 letters: {count_5_letters}")

# Print the longest word
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print(f"Longest word: {longest}")

# Print the shortest word
shortest = words[0]
for word in words:
    if len(word) < len(shortest):
        shortest = word
print(f"Shortest word: {shortest}")

# Task 7: Mixed Data Processing
print("\n" + "=" * 40)
print("Task 7: Mixed Data Processing")
print("=" * 40)

people = [
    ("Alice", 25, True), ("Bob", 30, False), ("Charlie", 22, True),
    ("Diana", 35, False), ("Eve", 19, True), ("Frank", 28, True)
]

# Print all names
print("All names:")
for name, age, is_student in people:
    print(name)

# Print all ages
print("\nAll ages:")
for name, age, is_student in people:
    print(age)

# Print names of students
print("\nNames of students:")
for name, age, is_student in people:
    if is_student:
        print(name)

# Print names of non-students
print("\nNames of non-students:")
for name, age, is_student in people:
    if not is_student:
        print(name)

# Print people older than 25
print("\nPeople older than 25:")
for name, age, is_student in people:
    if age > 25:
        print(f"{name} (age {age})")

# Print people younger than 30
print("\nPeople younger than 30:")
for name, age, is_student in people:
    if age < 30:
        print(f"{name} (age {age})")

# Count how many students there are
student_count = 0
for name, age, is_student in people:
    if is_student:
        student_count += 1
print(f"\nNumber of students: {student_count}")

# Count how many non-students there are
non_student_count = 0
for name, age, is_student in people:
    if not is_student:
        non_student_count += 1
print(f"Number of non-students: {non_student_count}")

# Task 8: Simple Statistics
print("\n" + "=" * 40)
print("Task 8: Simple Statistics")
print("=" * 40)

scores = [78, 85, 92, 67, 89, 94, 76, 88, 91, 83]

# Print all scores
print("All scores:")
for score in scores:
    print(score)

# Find the highest score
highest_score = scores[0]
for score in scores:
    if score > highest_score:
        highest_score = score
print(f"\nHighest score: {highest_score}")

# Find the lowest score
lowest_score = scores[0]
for score in scores:
    if score < lowest_score:
        lowest_score = score
print(f"Lowest score: {lowest_score}")

# Calculate the average score
total_score = 0
for score in scores:
    total_score += score
average_score = total_score / len(scores)
print(f"Average score: {average_score:.1f}")

# Count scores above 85
above_85 = 0
for score in scores:
    if score > 85:
        above_85 += 1
print(f"Scores above 85: {above_85}")

# Count scores below 80
below_80 = 0
for score in scores:
    if score < 80:
        below_80 += 1
print(f"Scores below 80: {below_80}")

# Print scores in the 80s (80-89)
print("\nScores in the 80s:")
for score in scores:
    if 80 <= score <= 89:
        print(score)

# Print scores in the 90s (90-99)
print("\nScores in the 90s:")
for score in scores:
    if 90 <= score <= 99:
        print(score)

print("\n" + "=" * 50)
print("All tasks completed successfully!")
print("=" * 50)
