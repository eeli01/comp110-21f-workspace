"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dicitonary literal representation
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from dictionary
# by its key
schools.pop("Duke")

# Test for existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

# Can turn above statement into an if-else statement
# if "Duke" in schools:
#   print("Found the key 'Duke' in schools")
# else:
#   print("No key 'Duke' in schools")

# Update / Reassign a key-valye pair
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

# Demonstration of dictionary literals

# Empty dictionary literal
schools = {}  # same as dict()
print(schools)

# Alernatively, can initialize key-value pairs
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26150}
print(schools)

# This example would create three separate dictionaries in heap


# What happens when a key accessed does not exist?
# print(schools["UNCC"])
# Gives KeyError
# Gives traceback that says:
#   (working from botom to top) in file working in and on what line the error occurs
#   gives statement that causes error to occur

# Example for looping over the keys of a dict
for school in schools: 
    print(f"Key: {school} -> Value: {schools[school]}")