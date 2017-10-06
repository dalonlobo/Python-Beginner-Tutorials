colors = ['red\n', 'yellow\n', 'blue\n']

# Writing to files
f = open('colors.txt', 'w')

f.writelines(colors)

f.close()

# Reading from files
f = open('colors.txt', 'r')

print(f.readlines())

f.close()

# Using context manager
with open("test.txt", "w") as f:
    f.writelines(colors)

with open("test.txt", "r+") as f:
    print(f.readlines())


