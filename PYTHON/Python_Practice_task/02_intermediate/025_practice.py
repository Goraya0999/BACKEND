# ------------------------------------------------------------
# Problem: Extract all digits from a string
# Description:
# This program extracts all numeric characters (0–9) from a 
# given string and combines them into a new string.
# ------------------------------------------------------------

# Input string
text = "afedfw2342389fdvsdf89hsdvsd89er"

# Initialize an empty string to store extracted digits
digits = ""

# Iterate through each character in the string
for char in text:
    # Check if the character is a digit
    if char.isdigit():
        # Append digit to the result string
        digits += char

# Output the extracted digits
print("Extracted Digits:", digits)