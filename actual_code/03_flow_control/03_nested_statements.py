authenticated = True
role = "engineer"  # physicist, engineer, operator
experiment = "atlas"  # atlas, cms, alice
assigned_experiment = "atlas"
experiment_status = "running"
restricted = True
clearance_level = 4
time_of_day = "night"  # day or night

import sys


# 1. Look for statements than can combined
# 2. Early exit/return

if not authenticated:  # guard condition
    print("User not authenticated.")
    sys.exit(0)

# I know they have been authenticated!
if not (role == "physicist" or role == "engineer" or role == "operator"):
    print("Invalid role.")
    sys.exit(0)

# I know they have a valid role!

if experiment != assigned_experiment:
    print("You are not assigned to this experiment.")
    sys.exit()


if experiment_status == "running":
    if restricted:
        if clearance_level >= 5:
            if time_of_day == "night":
                if role == "operator":
                    print("Access granted for restricted night operation.")
                else:
                    print("Only operators may access restricted experiments at night.")
            else:
                print("Access granted.")
        else:
            print("Insufficient clearance level.")
    else:
        if time_of_day == "night":
            if role == "operator":
                print("Access granted for night operation.")
            else:
                print("Night access restricted to operators.")
        else:
            print("Access granted.")
else:
    print("Experiment is not running.")


test_score = 10
if test_score < 40:
    print("F")
elif test_score < 50:
    print("E")  # 40-50