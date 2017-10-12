# What is a class? Think of a class as a blueprint. It isn't something in itself,
# it simply describes how to make something. You can create lots of objects from that
# blueprint - known technically as instances.


class Pet:
    def __init__(self, name):
        self.name = name

    def getName(self):
        print("Name of the Pet is:", self.name)

    def setName(self, newName):
        self.name = newName


class Dog(Pet):
    def __init__(self, name, color):
        self.color = color
        super().__init__(name)

    def __str__(self):
        return self.name + " " + self.color


dog = Dog("Tom", "white")

# dog.getName()
#
# dog.setName("Black")
#
# dog.getName()

print(dog)
