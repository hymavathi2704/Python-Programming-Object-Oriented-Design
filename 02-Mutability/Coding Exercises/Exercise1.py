'''
The code below creates the CelestialBody class as well as the function compared_to_earth. Transform the compared_to_earth function so that it becomes an instance method of the CelestialBody class.
Expected Output
Printing the compared_to_earth instance method should return 11.208892860782516.'''

#Code:
class CelestialBody:
    """Represents a celestial body"""
    def __init__(self, name, diameter, distance, moons):
        self.name = name
        self.diameter = diameter
        self.distance = distance
        self.moons = moons
    
    def compared_to_earth(self):
        """Determines the size of a celestial
        body relative to Earth using diameter"""
        earth_diameter = 12756.3  # diameter of Earth in kilometers
        relative_size = self.diameter / earth_diameter
        return relative_size

# Creating an instance of CelestialBody
planet = CelestialBody("Jupiter", 142984, 778360000, 79)

# Testing the compared_to_earth method
print(planet.compared_to_earth())  # Output should be 11.208892860782516
