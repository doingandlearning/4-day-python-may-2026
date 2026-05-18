# Lab 05 Extra - Task 2: Laboratory Inventory
# Practice with dictionaries for chemical inventory management

print("=" * 50)
print("Task 2: Laboratory Inventory")
print("=" * 50)

# Start with an empty inventory
inventory = {}

# Add 500ml of hydrochloric acid to inventory
inventory["hydrochloric acid"] = "500ml"
print("Added hydrochloric acid: 500ml")

# Add 250g of sodium chloride to inventory
inventory["sodium chloride"] = "250g"
print("Added sodium chloride: 250g")

# Add 100ml of ethanol to inventory
inventory["ethanol"] = "100ml"
print("Added ethanol: 100ml")

# Add 50g of potassium hydroxide to inventory
inventory["potassium hydroxide"] = "50g"
print("Added potassium hydroxide: 50g")

# Print the entire inventory
print("\nEntire inventory:")
for chemical, quantity in inventory.items():
    print(f"- {chemical}: {quantity}")

# Print just the chemicals
print("\nChemicals in inventory:")
for chemical in inventory.keys():
    print(f"- {chemical}")

# Print just the quantities
print("\nQuantities in inventory:")
for quantity in inventory.values():
    print(f"- {quantity}")

# Check if "hydrochloric acid" is in the cart
if "hydrochloric acid" in inventory:
    print("\nYes, 'hydrochloric acid' is in inventory")
else:
    print("\nNo, 'hydrochloric acid' is not in inventory")

# Check if "sulfuric acid" is in the cart
if "sulfuric acid" in inventory:
    print("Yes, 'sulfuric acid' is in inventory")
else:
    print("No, 'sulfuric acid' is not in inventory")

# Update hydrochloric acid quantity to 750ml
inventory["hydrochloric acid"] = "750ml"
print(f"\nUpdated hydrochloric acid quantity: {inventory['hydrochloric acid']}")

# Remove sodium chloride from inventory
del inventory["sodium chloride"]
print("Removed sodium chloride from inventory")

# Print the updated inventory
print("\nUpdated inventory:")
for chemical, quantity in inventory.items():
    print(f"- {chemical}: {quantity}")

# Print the total number of different chemicals
print(f"\nTotal number of different chemicals: {len(inventory)}")

print("\n" + "=" * 50)
print("Task 2 completed successfully!")
print("=" * 50)
