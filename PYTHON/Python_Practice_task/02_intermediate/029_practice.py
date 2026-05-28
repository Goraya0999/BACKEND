# ------------------------------------------------------------
# Problem: Check if a year is a leap year
# Description:
# This program validates a 4-digit year and checks whether
# it is a leap year using proper rules.
# ------------------------------------------------------------

# Take input as string for validation
year_input = input("Enter a 4-digit year: ")

# Validate input (must be 4 digits)
if year_input.isdigit() and len(year_input) == 4:
    
    # Convert to integer after validation
    year = int(year_input)

    # Leap year logic:
    # - Divisible by 4
    # - Not divisible by 100 unless also divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
else:
    print("❌ Invalid input! Please enter exactly a 4-digit number.")