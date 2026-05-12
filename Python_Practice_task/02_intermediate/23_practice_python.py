#Problem statement :
#  In given sentence , Capitalize the first letter of each word

x_string="i love cybersecurity"
# title() method :
# The title() method in Python is used to convert a string so that each word starts with a capital letter and the remaining letters are lowercase.
cap_first_letter = x_string.title()
print(cap_first_letter)


#--Check if all character in a string is digit
# isdigit() method:
# used to check if string has digit
print(x_string.isdigit())  # False
print("1233455".isdigit()) # true