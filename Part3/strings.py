# Introduction to strings

# Single line string, you can use single or double quotes
myVar = "Hi! How are you doing today?"

print(myVar)

# Multi-line string, using 3 single quotes or 3 double quotes
myVar = """This is a very long string,
            It goes into the next line"""

print(myVar)

# Raw string with special characters
myVar = r"This is special \ %s etc."

print(myVar)

# Multiplying strings
print("Hi" * 3)

# Adding strings
print("Hi! " + "How are you doing?")

# String slicing and indexing
myVar = "Hello world!"

# Note: indexes start from 0 in python
print(myVar[3])

# Negative index
# Note: Negative index start from -1, count from right side
print(myVar[-3])

print(myVar[1:3])  # Slicing, myVar(start, end), it excludes end index
print(myVar[:3])   # Slicing from start
print(myVar[1:])   # Slicing till end
print(myVar[1:6:2])  # Increment by 2
print(myVar[-1::1])  # Reverse a string

# Formatting strings
a = 10
b = 20

# Classical approach
print("The sum of %d + %d = %d" % (a, b, a + b))

# Using .format method on strings
print("The sum of {0} + {1} = {2}".format(a, b, a + b))
