# ------------------------------------------------------------
# Problem: Grading System
# Description:
# This program calculates percentage and assigns grades
# based on marks obtained and total marks.
# ------------------------------------------------------------

# Take input from user
marks = int(input("Enter obtained marks: "))
total_marks = int(input("Enter total marks: "))

# Validate input
if marks > total_marks or total_marks <= 0:
    print("❌ Invalid input! Please enter valid marks.")
else:
    # Calculate percentage
    percentage = (marks / total_marks) * 100

    print(f"Percentage: {percentage:.2f}%")

    # Assign grades
    if 90 <= percentage <= 100:
        print("Grade: A+")
    elif percentage >= 80:
        print("Grade: B")
    elif percentage >= 70:
        print("Grade: C")
    elif percentage >= 60:
        print("Grade: D")
    else:
        print("Grade: F (Fail)")