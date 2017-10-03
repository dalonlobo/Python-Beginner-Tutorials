# Modules and Packages
#
# Modules in Python are simply Python files with the .py extension,
# which implement a set of functions. Modules are imported from other modules using the import command.
#
# To import a module, we use the import command.

from funcdemo import sumTwoNumbers

print(sumTwoNumbers(1, 2))

# We can look for which functions are implemented in each module by using the dir function

# Writing packages
#
# Packages are namespaces which contain multiple packages and modules themselves.
# They are simply directories, but with a twist.
#
# Each package in Python is a directory which MUST contain a special file
# called __init__.py. This file can be empty, and it indicates that the directory it
# contains is a Python package, so it can be imported the same way a module can be imported.

# https://docs.python.org/3/library/
