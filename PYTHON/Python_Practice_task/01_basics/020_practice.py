# count() method:
# The count() method returns the number of occurrences of a specified substring in a string.
# The lower() method is used here to ensure case-insensitive counting.

x = "banana"

# Convert string to lowercase (only one lower() is needed) and count occurrences of "a"
countt = x.lower().count("a")
print(countt)

#-----------------------------------#

# Reverse string using slicing:
# Slicing with [::-1] reverses the entire string.

reverse_x = x[::-1]
print(reverse_x)