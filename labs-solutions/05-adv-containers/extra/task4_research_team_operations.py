# Lab 05 Extra - Task 4: Research Team Operations
# Practice with sets to find relationships between research teams

print("=" * 50)
print("Task 4: Research Team Operations")
print("=" * 50)

# Sample data - researchers on different projects
physics_team = {"Dr. Smith", "Dr. Johnson", "Dr. Brown", "Dr. Davis", "Dr. Wilson"}
chemistry_team = {"Dr. Johnson", "Dr. Davis", "Dr. Miller", "Dr. Taylor", "Dr. Anderson"}

# Print all physics team members
print("Physics team members:")
for member in physics_team:
    print(f"- {member}")

# Print all chemistry team members
print("\nChemistry team members:")
for member in chemistry_team:
    print(f"- {member}")

# Find researchers working on both projects (intersection)
both_projects = physics_team & chemistry_team
print(f"\nResearchers working on both projects: {both_projects}")

# Find researchers working only on physics (difference)
only_physics = physics_team - chemistry_team
print(f"Researchers working only on physics: {only_physics}")

# Find researchers working only on chemistry (difference)
only_chemistry = chemistry_team - physics_team
print(f"Researchers working only on chemistry: {only_chemistry}")

# Find all researchers (working on either project) (union)
all_researchers = physics_team | chemistry_team
print(f"All researchers (either project): {all_researchers}")

# Find researchers working on neither project (if we know all researchers)
# Let's assume we have a complete list of all researchers
all_researchers_list = {"Dr. Smith", "Dr. Johnson", "Dr. Brown", "Dr. Davis", "Dr. Wilson", 
                       "Dr. Miller", "Dr. Taylor", "Dr. Anderson", "Dr. White", "Dr. Black"}
all_researchers_set = set(all_researchers_list)
neither_project = all_researchers_set - all_researchers
print(f"Researchers working on neither project: {neither_project}")

# Check if "Dr. Smith" is on the physics team
if "Dr. Smith" in physics_team:
    print("\nYes, Dr. Smith is on the physics team")
else:
    print("\nNo, Dr. Smith is not on the physics team")

# Check if "Dr. Miller" is on the physics team
if "Dr. Miller" in physics_team:
    print("Yes, Dr. Miller is on the physics team")
else:
    print("No, Dr. Miller is not on the physics team")

# Additional set operations for practice
print(f"\nNumber of physics team members: {len(physics_team)}")
print(f"Number of chemistry team members: {len(chemistry_team)}")
print(f"Number of researchers on both teams: {len(both_projects)}")
print(f"Total unique researchers: {len(all_researchers)}")

print("\n" + "=" * 50)
print("Task 4 completed successfully!")
print("=" * 50)
