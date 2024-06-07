'''
Define the class Cat. The class should have a constructor but without any parameters. The constructor will generate the following attributes.
breed - "american shorthair"
color - "black"
name - "kiwi"
Test your code with print statements and the TRY IT button below before submitting your work.'''

#Code:
class Cat:
    def __init__(self):
        self.breed = "american shorthair"
        self.color = "black"
        self.name = "kiwi"

# Testing the code
cat = Cat()
print(cat.breed)  # Output should be "american shorthair"
print(cat.color)  # Output should be "black"
print(cat.name)   # Output should be "kiwi"
