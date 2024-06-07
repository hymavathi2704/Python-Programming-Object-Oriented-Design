'''
Define the class BigCat which will help record information on the animals in the Panthera genus (tiger, lion, jaguar, leopard, and snow leopard). Since all animals are in the same genus, the object should have the class attribute genus with the value panthera. The constructor should accept the following parameters (in this order):
species- String with the species of the animal, e.g. "tigris"
common_name - String with the common name of the animal, e.g. "tiger"
habitat - List of strings with location of the animal, e.g. ["asia"]
'''

#Code:
class BigCat:
    genus = "panthera"
    
    def __init__(self, species, common_name, habitat):
        self.species = species
        self.common_name = common_name
        self.habitat = habitat

# Testing the code
big_cat = BigCat(
    "tigris",
    "tiger",
    ["asia"]
)

print(BigCat.genus)          # Output should be "panthera"
print(big_cat.species)       # Output should be "tigris"
print(big_cat.common_name)   # Output should be "tiger"
print(big_cat.habitat)       # Output should be ["asia"]
