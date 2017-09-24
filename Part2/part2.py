#!/usr/bin/python3.6

# Exploring print function
print("Hello", "World", sep="----", end=" Ending...\n")

# Using variables to give a name to the location
myVar1 = "Any object"  # A string
myVar2 = 100  # An integer assignment
myVar3 = 1000.0  # A floating point

# Arithmetic operations

a = 21
b = 10
c = 0

c = a + b
print("a + b =", c)

c = a - b
print("a - b =", c)

c = a * b
print("a * b =", c)

c = a / b
print("a / b =", c)

c = a % b
print("a % b =", c)

a = 2
b = 3
c = a ** b
print("a ** b =", c)

a = 10
b = 5
c = a // b
print("a // b =", c)

# Accept input from the user
userInput = input("Please enter your name: ")
print("Good Bye", userInput)
