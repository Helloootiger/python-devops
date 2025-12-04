# Sequence data type - List 

# creating list

resource_group = ["VM", "Vnet", "App service"]

# list indexing

first_resource = resource_group[0]
print("First Resource:", first_resource)

# list length

resource_group_length = len(resource_group)
print("Length of Resource Group:", resource_group_length)

# Appending to a list

updated_resource_group1 = resource_group.append("AKS")
print("Updated Resource Group1:", resource_group)

# Removing from a list

updated_resource_group2 = resource_group.remove("VM")
print("Updated Resource Group2:", resource_group)

# Slicing

subset = resource_group[0:1]
print("Subset:", subset)

# Concatenating list

new_resource_group = resource_group + ["Storage Account"]
print("New resource Group:", new_resource_group)

# Sorting list

asc_order = resource_group.sort()
print("Ordering Resources:", resource_group)

# Checking for an element in list

is_present = "VM" in resource_group
if is_present:
    print("Match:", is_present)
else:
    print("Match not found")
