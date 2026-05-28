# index() and find() methods:

# The index() method returns the position (index) of the first occurrence
# of a specified substring. If the substring is not found, it raises a ValueError.

# The find() method also returns the index of the substring,
# but returns -1 instead of raising an error if the substring is not found.

x = "Hello world"

# Convert string to lowercase for case-insensitive search
req_index1 = x.lower().find("world")   # returns -1 if not found
req_index2 = x.lower().index("world")  # raises error if not found

# Print results
print(req_index1)
print(req_index2)