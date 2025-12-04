# Sequence data type - List 

# creating list

resource_group = ("VM", "Vnet", "App service")

# list indexing

first_resource = resource_group[0]
print("First Resource:", first_resource)

# list length

resource_group_length = len(resource_group)
print("Length of Resource Group:", resource_group_length)

# Slicing

subset = resource_group[0:1]
print("Subset:", subset)

# Concatenating list

new_resource_group = resource_group + (1, "Storage Account")
print("New resource Group:", new_resource_group)


# Checking for an element in list

is_present = "2" in resource_group
if is_present:
    print("Match:", is_present)
else:
    print("Match not found")

# Tuple packing and unpacking

coordinates = (3, 4)

x, y = coordinates

def get_coordinates():
    return(x, y)

x, y = get_coordinates()

print("Coordinates:", y, x)
