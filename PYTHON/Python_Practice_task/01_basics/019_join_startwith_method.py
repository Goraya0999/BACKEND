# join() method:
# The join() method is used to concatenate (combine) elements of an iterable
# (such as a list or tuple) into a single string, using a specified separator.

x_list = ['Hello', 'world']

# Join the list elements into a string with a space as the separator
x_string = " ".join(x_list)

print(x_string)

# startswith() method:
# The startswith() method checks whether a string begins with a specified prefix.
# It returns True if the string starts with the given value, otherwise False.

def start(x: str) -> bool:
    return x.lower().startswith("py")  # convert to lowercase for case-insensitive check

x = "Python"
print(start(x))