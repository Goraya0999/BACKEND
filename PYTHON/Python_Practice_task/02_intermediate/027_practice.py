# ------------------------------------------------------------
# Problem: Check if a number is positive, negative, or zero
# Description:
# This program takes an integer input from the user and 
# determines whether the number is positive, negative, or zero.
# ------------------------------------------------------------

# Take input from the user
number = int(input("Enter a number: "))

# Check the nature of the number
if number < 0:
    print(f"{number} is a negative number.")
elif number == 0:
    print("The number is zero.")
else:
    print(f"{number} is a positive number.")