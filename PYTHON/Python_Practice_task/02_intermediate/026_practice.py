# ------------------------------------------------------------
# Problem: Check whether a number is even or odd
# Description:
# This program takes an integer input from the user and checks
# whether the number is even or odd using the modulus operator.
# ------------------------------------------------------------

# Take input from the user
number = int(input("Enter a number: "))

# Check if the number is divisible by 2
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")