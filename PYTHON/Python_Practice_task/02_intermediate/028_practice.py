# ------------------------------------------------------------
# Problem: Find the maximum of two numbers without using max()
# Description:
# This program takes two integer inputs from the user and 
# determines the greater (maximum) number using conditional logic.
# ------------------------------------------------------------

# Take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Determine the maximum number
if num1 > num2:
    maximum = num1
else:
    maximum = num2

# Output the result
print(f"{maximum} is the maximum number.")