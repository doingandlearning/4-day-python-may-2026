# Lab 05 Extra - Task 6: Laboratory Equipment Database
# Practice with nested dictionaries for equipment management

print("=" * 50)
print("Task 6: Laboratory Equipment Database")
print("=" * 50)

# Sample equipment database
equipment = {
    "Microscope_001": {"type": "Optical", "location": "Lab_A", "status": "Active"},
    "Centrifuge_002": {"type": "Centrifuge", "location": "Lab_B", "status": "Maintenance"},
    "Spectrometer_003": {"type": "Analytical", "location": "Lab_A", "status": "Active"}
}

print("Initial equipment database:")
for equipment_id, details in equipment.items():
    print(f"- {equipment_id}: {details}")

# Print all equipment names
print("\nAll equipment names:")
for equipment_id in equipment.keys():
    print(f"- {equipment_id}")

# Print Microscope_001's location
print(f"\nMicroscope_001's location: {equipment['Microscope_001']['location']}")

# Print Centrifuge_002's status
print(f"Centrifuge_002's status: {equipment['Centrifuge_002']['status']}")

# Add new equipment "Balance_004" with type "Weighing", location "Lab_C", status "Active"
equipment["Balance_004"] = {"type": "Weighing", "location": "Lab_C", "status": "Active"}
print(f"\nAdded Balance_004: {equipment['Balance_004']}")

# Update Spectrometer_003's status to "Calibration"
equipment["Spectrometer_003"]["status"] = "Calibration"
print(f"Updated Spectrometer_003 status: {equipment['Spectrometer_003']}")

# Remove Centrifuge_002 from equipment
del equipment["Centrifuge_002"]
print("Removed Centrifuge_002 from equipment")

# Print all equipment locations
print("\nAll equipment locations:")
for equipment_id, details in equipment.items():
    print(f"- {equipment_id}: {details['location']}")

# Print all equipment statuses
print("\nAll equipment statuses:")
for equipment_id, details in equipment.items():
    print(f"- {equipment_id}: {details['status']}")

# Find equipment in Lab_A
print("\nEquipment in Lab_A:")
for equipment_id, details in equipment.items():
    if details["location"] == "Lab_A":
        print(f"- {equipment_id}: {details}")

# Additional operations for practice
print("\nAdditional operations:")

# Find equipment by type
print("\nOptical equipment:")
for equipment_id, details in equipment.items():
    if details["type"] == "Optical":
        print(f"- {equipment_id}: {details}")

# Find active equipment
print("\nActive equipment:")
for equipment_id, details in equipment.items():
    if details["status"] == "Active":
        print(f"- {equipment_id}: {details}")

# Count equipment by location
lab_counts = {}
for equipment_id, details in equipment.items():
    location = details["location"]
    if location in lab_counts:
        lab_counts[location] += 1
    else:
        lab_counts[location] = 1

print(f"\nEquipment count by location: {lab_counts}")

# Count equipment by status
status_counts = {}
for equipment_id, details in equipment.items():
    status = details["status"]
    if status in status_counts:
        status_counts[status] += 1
    else:
        status_counts[status] = 1

print(f"Equipment count by status: {status_counts}")

print("\n" + "=" * 50)
print("Task 6 completed successfully!")
print("=" * 50)
