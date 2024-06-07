'''
Use the CelestialBody class to the left as the parent class. Create the Satellite and Planet classes, both of which are children of CelestialBody. Using the super() keyword to extend the __init__ method of the parent class, add the attribute host_planet to the Satellite class and add the attribute host_star to the Planet class.
Expected Attributes
After extending the __init__ method, your classes should have the following attributes.
CelestialBody	Satellite	Planet
size	size	size
mass	mass	mass
composition	composition	composition
name	name	name
host_planet	host_star
'''

#Code:
class CelestialBody:
    def __init__(self, size, mass, composition, name):
        self.size = size
        self.mass = mass
        self.composition = composition
        self.name = name

class Satellite(CelestialBody):
    def __init__(self, size, mass, composition, name, host_planet):
        super().__init__(size, mass, composition, name)
        self.host_planet = host_planet

class Planet(CelestialBody):
    def __init__(self, size, mass, composition, name, host_star):
        super().__init__(size, mass, composition, name)
        self.host_star = host_star

# Example usage:
# Creating instances of Satellite and Planet
moon = Satellite("Small", "0.0735 × 10^24 kg", "Rocky", "Moon", "Earth")
earth = Planet("Big", "5.972 × 10^24 kg", "Rocky and Gaseous", "Earth", "Sun")

# Printing attributes to verify
print(f"Satellite - Name: {moon.name}, Host Planet: {moon.host_planet}")
print(f"Planet - Name: {earth.name}, Host Star: {earth.host_star}")
