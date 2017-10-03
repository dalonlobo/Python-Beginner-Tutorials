# Python uses boolean variables to evaluate conditions. The boolean values are True and False.
#
# x = 2
# print(x == 2)  # prints out True
# print(x == 3)  # prints out False
# print(x < 3)   # prints out True

# Boolean operators
#
# The "and" and "or" boolean operators allow building complex boolean expressions, for example:
#
# name = "John"
# age = 23
# if name != "John" and age == 23:
#     print("Your name is John, and you are also 23 years old.")
# else:
#     print("Condition is false")
#
# if name == "John" or name == "Rick":
#     print("Your name is either John or Rick.")


# The "in" operator
#
# The "in" operator could be used to check if a specified object
# exists within an iterable object container, such as a list:

name = "Dalon"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")
elif name in ["Dalon", 3, 4]:
    print("I found you in elif")
else:
    print("Hello Dalon")