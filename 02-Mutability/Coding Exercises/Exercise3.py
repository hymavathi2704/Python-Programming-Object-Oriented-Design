'''
Using the same CelestialBody class, create a factory method called make_earth. This method returns a CelestialBody object for planet Earth. Earth is 149,600,000 km from the Sun, has a diameter of 12,756.3 km, and has one moon.
Expected Output
The factory method should return a CelestialBody object. This object should be able to do the following things:
print(my_planet.name) will return Earth
print(my_planet.distance) will return 149600000
print(my_planet.diameter) will return 12756.3
print(my_planet.moons) will return 1'''

#Code:
class CelestialBody:
    """Represents a celestial body"""
    def __init__(self, name, diameter, distance, moons):
        self.name = name
        self.diameter = diameter
        self.distance = distance
        self.moons = moons
    
    def compared_to_earth(self):
        """Determines the size of a celestial body relative to Earth using diameter"""
        earth_diameter = 12756.3  # diameter of Earth in kilometers
        relative_size = self.diameter / earth_diameter
        return relative_size

    @staticmethod
    def closer_to_sun(body1, body2):
        """Compares two CelestialBody objects and returns the name of the one closer to the sun"""
        if body1.distance < body2.distance:
            return body1.name
        else:
            return body2.name
    
    @classmethod
    def make_earth(cls):
        """Factory method to create a CelestialBody object representing Earth"""
        return cls("Earth", 12756.3, 149600000, 1)

# Creating an instance of CelestialBody using the factory method
my_planet = CelestialBody.make_earth()

# Testing the factory method
print(my_planet.name)       # Output should be "Earth"
print(my_planet.distance)   # Output should be 149600000
print(my_planet.diameter)   # Output should be 12756.3
print(my_planet.moons)      # Output should be 1
