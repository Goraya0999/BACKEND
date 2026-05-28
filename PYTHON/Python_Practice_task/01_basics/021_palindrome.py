# Palindrome:
# A palindrome is a word, phrase, or sequence that reads the same
# forward and backward (e.g., "racecar", "madam").

def is_palindrome(x: str) -> bool:
    # Reverse the string using slicing
    x_reverse = x[::-1]
    
    # Compare original string with reversed string
    return x == x_reverse

# Example usage
x = "racecar"
print(is_palindrome(x))