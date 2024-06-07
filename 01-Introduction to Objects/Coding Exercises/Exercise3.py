'''
Define the class SuperHero. The class should have a constructor that accepts the following parameters (in this order):
name- String with the name of the super hero, e.g. "Spider-Man"
secret_identity - String with the true name of the hero, e.g. "Peter Parker"
powers - A list of strings with each element representing a power, e.g. ["superhuman strength", "superhuman speed", "superhuman reflexes", "superhuman durability", "healing factor", "spider-sense alert", "heightened senses", "wallcrawling"]'''

#Code:
class SuperHero:
    def __init__(self, name, secret_identity, powers):
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers

# Testing the code
superhero = SuperHero(
    "Spider-Man",
    "Peter Parker",
    [
        "superhuman strength",
        "superhuman speed",
        "superhuman reflexes",
        "superhuman durability",
        "healing factor",
        "spider-sense alert",
        "heightened senses",
        "wallcrawling"
    ]
)

print(superhero.name)             # Output should be "Spider-Man"
print(superhero.secret_identity)  # Output should be "Peter Parker"
print(superhero.powers)           # Output should be the list of powers
