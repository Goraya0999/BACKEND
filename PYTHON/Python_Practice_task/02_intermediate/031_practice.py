"""
Assign a value to `x` using a ternary conditional expression.

Condition:
    5 > 10 → evaluates to False

Logic:
    - If True  → x = "yes"
    - If False → x = "no"

Result:
    x will be assigned "no"
"""

x = "yes" if 5 > 10 else "no"
print(x)
#------------------------------------
val = input("Enter Character: ").strip().lower()
vowels = ['a', 'e', 'i', 'o', 'u']

if len(val) != 1:
    print("Error: Enter only one character")
else:
    if val in vowels:
        print(f"{val} is a vowel")
    else:
        print(f"{val} is not a vowel")