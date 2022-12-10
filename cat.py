class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "cat")
        self.breed = breed

    def __str__(self):
        return f"{super().__str__()} of breed {self.breed}"

# create a Cat object and print its attributes
fluffy = Cat("Fluffy", "Persian")
print(fluffy)
# output: Fluffy is a cat of breed Persian
