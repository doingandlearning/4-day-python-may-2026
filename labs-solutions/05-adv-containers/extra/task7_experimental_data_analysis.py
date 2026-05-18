# Lab 05 Extra - Task 7: Experimental Data Analysis with Sets and Dictionaries
# Practice with both sets and dictionaries for experimental data analysis

print("=" * 50)
print("Task 7: Experimental Data Analysis with Sets and Dictionaries")
print("=" * 50)

# Sample experimental data
experiment_results = {
    "Trial_1": ["Pass", "Fail", "Pass", "Pass", "Fail", "Pass", "Pass", "Fail"],
    "Trial_2": ["High", "Low", "High", "High", "Low", "High", "Low", "High"],
    "Trial_3": ["Red", "Blue", "Green", "Red", "Blue", "Red", "Green", "Blue"]
}

print("Experimental results:")
for trial, results in experiment_results.items():
    print(f"{trial}: {results}")

# Print all results for each trial
print("\nAll results for each trial:")
for trial, results in experiment_results.items():
    print(f"{trial}: {results}")

# Find unique results for each trial
print("\nUnique results for each trial:")
for trial, results in experiment_results.items():
    unique_results = set(results)
    print(f"{trial}: {unique_results}")

# Count how many times "Pass" appears in Trial_1
pass_count = experiment_results["Trial_1"].count("Pass")
print(f"\n'Pass' appears {pass_count} times in Trial_1")

# Count how many times "High" appears in Trial_2
high_count = experiment_results["Trial_2"].count("High")
print(f"'High' appears {high_count} times in Trial_2")

# Find the most common result in Trial_3
trial_3_results = experiment_results["Trial_3"]
result_counts = {}
for result in trial_3_results:
    if result in result_counts:
        result_counts[result] += 1
    else:
        result_counts[result] = 1

most_common_count = max(result_counts.values())
most_common_results = [result for result, count in result_counts.items() if count == most_common_count]
print(f"Most common result(s) in Trial_3: {most_common_results} (appears {most_common_count} times)")

# Find results that appear more than once in Trial_1
trial_1_results = experiment_results["Trial_1"]
trial_1_counts = {}
for result in trial_1_results:
    if result in trial_1_counts:
        trial_1_counts[result] += 1
    else:
        trial_1_counts[result] = 1

repeated_results = [result for result, count in trial_1_counts.items() if count > 1]
print(f"Results that appear more than once in Trial_1: {repeated_results}")

# Create a set of all unique results across all trials
all_results = set()
for trial, results in experiment_results.items():
    for result in results:
        all_results.add(result)

print(f"All unique results across all trials: {all_results}")

# Additional analysis using sets
print("\nAdditional set operations:")

# Find results that appear in all trials
trial_1_set = set(experiment_results["Trial_1"])
trial_2_set = set(experiment_results["Trial_2"])
trial_3_set = set(experiment_results["Trial_3"])

common_to_all = trial_1_set & trial_2_set & trial_3_set
print(f"Results common to all trials: {common_to_all}")

# Find results unique to each trial
unique_to_trial_1 = trial_1_set - trial_2_set - trial_3_set
unique_to_trial_2 = trial_2_set - trial_1_set - trial_3_set
unique_to_trial_3 = trial_3_set - trial_1_set - trial_2_set

print(f"Results unique to Trial_1: {unique_to_trial_1}")
print(f"Results unique to Trial_2: {unique_to_trial_2}")
print(f"Results unique to Trial_3: {unique_to_trial_3}")

# Find results that appear in exactly two trials
trial_1_2_common = trial_1_set & trial_2_set
trial_1_3_common = trial_1_set & trial_3_set
trial_2_3_common = trial_2_set & trial_3_set

in_exactly_two = (trial_1_2_common | trial_1_3_common | trial_2_3_common) - common_to_all
print(f"Results appearing in exactly two trials: {in_exactly_two}")

print("\n" + "=" * 50)
print("Task 7 completed successfully!")
print("=" * 50)
