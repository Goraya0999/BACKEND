# ------------------------------------------------------------
# Problem: Remove vowels from a string
# Description:
# This program removes all vowels (a, e, i, o, u) from a given
# string and returns the resulting string.
# ------------------------------------------------------------

# Define a list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# ---------------------- Example 1 ----------------------
# Input string
text = "I love Cybersecurity"

# Initialize an empty string to store the result
result = ""

# Iterate through each character in the string
for char in text:
    # Convert character to lowercase for case-insensitive comparison
    # If the character is NOT a vowel, add it to the result
    if char.lower() not in vowels:
        result += char

# Output the string after removing vowels
print("Processed String:", result)


# ---------------------- Example 2 ----------------------
# Input string containing only vowels
text_vowels = "aeioui"

# Initialize result string
filtered_result = ""

# Iterate through each character
for char in text_vowels:
    # Add character only if it is not a vowel
    if char.lower() not in vowels:
        filtered_result += char

# Output results
print("Processed String:", filtered_result)  # Expected: empty string
print("Length:", len(filtered_result))       # Expected: 0