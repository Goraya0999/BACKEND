# ------------------------------------------------------------
# Problem: Count words in a string without using len()
# Description:
# This program counts the number of words by counting spaces.
# Words = spaces + 1 (for non-empty string)
# ------------------------------------------------------------

# Input string
text = "I hate my university classes"

# Initialize word counter
word_count = 1  # Start with 1 assuming non-empty string

# Loop through each character
for char in text:
    # Increment count when a space is found
    if char == " ":
        word_count += 1

# Output total words
print("Total Words:", word_count)