# What are Functions?
#
# Functions are a convenient way to divide your code into useful blocks.
# That way we can reuse the code.
# Python uses indentation to define code blocks, instead of brackets

# def myFunction():
#     print("Hello From My Function!")
#     print("Hi")
#
# myFunction()

# def myFunctionWithArgs(username, greeting):
#     print("Hello, {} , From My Function!, I wish you {}".format(username, greeting))
#
# myFunctionWithArgs("Dalon", "Good morning")

# Functions may return a value to the caller, using the keyword- 'return'

def sumTwoNumbers(a, b):
    return a + b




# The 'is' operator
#
# Unlike the double equals operator "==", the "is" operator
# does not match the values of the variables, but the instances themselves.

# x = [1, 2, 3]
# y = [1, 2, 3]
# print(x == y)  # Prints out True
# print(x is y)  # Prints out False

# The "not" operator
#
# Using "not" before a boolean expression inverts it:

# print(not False) # Prints out True
# print((not False) == (False)) # Prints out False

if __name__ == "__main__":
    result = sumTwoNumbers(5, 3)
    print(result)

    print(not False)  # Prints out True
    print((not False) == (False))  # Prints out False