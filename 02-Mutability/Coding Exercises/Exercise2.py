'''Using the same CelestialBody class, write a static method closer_to_sun that compares two CelectialBody objects and returns the name of the object that is closes to the sun.
Expected Output
If the objects mercury and venus are compared, then the method would return Mercury.'''

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

# Creating instances of CelestialBody
mercury = CelestialBody("Mercury", 4879.4, 57909000, 0)
venus = CelestialBody("Venus", 12103.6, 108160000, 0)

# Testing the closer_to_sun static method
print(CelestialBody.closer_to_sun(mercury, venus))  # Output should be "Mercury"
