'''
Define the class Observation which will help record observational data from a scientific outpost in Antarctica. The class should have a constructor that accepts parameters for date, temperature, elevation, precipitation, and penguins. Since Antarctica is a desert, precipitation should default to 0.
date- String with the date of the observation, e.g. "October 26, 2019"
temperature - Float with the temperature in Celsius, e.g. -47
elevation - Float with elevation in meters, e.g. 329.4
penguins - Integer representing the number of penguins observed, e.g. 3
precipitation- Float with precipitation in centimeters, e.g. 0.7'''

#Code:
class Observation:
    def __init__(self, date, temperature, elevation, penguins, precipitation=0):
        self.date = date
        self.temperature = temperature
        self.elevation = elevation
        self.penguins = penguins
        self.precipitation = precipitation

# Testing the code
observation = Observation(
    "October 26, 2019",
    -47.0,
    329.4,
    3,
    0.7
)

print(observation.date)            # Output should be "October 26, 2019"
print(observation.temperature)     # Output should be -47.0
print(observation.elevation)       # Output should be 329.4
print(observation.penguins)        # Output should be 3
print(observation.precipitation)   # Output should be 0.7

# Testing with default precipitation
observation_default_precip = Observation(
    "October 27, 2019",
    -45.0,
    330.0,
    5
)

print(observation_default_precip.date)            # Output should be "October 27, 2019"
print(observation_default_precip.temperature)     # Output should be -45.0
print(observation_default_precip.elevation)       # Output should be 330.0
print(observation_default_precip.penguins)        # Output should be 5
print(observation_default_precip.precipitation)   # Output should be 0 (default value)
