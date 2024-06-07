'''
Define the Country class which has attributes for name, capital, population, and continent. Please use the Python convention for making these attributes private.
Expected Output:
Initialize an object of the Country class as follows:
my_country = Country('France', 'Paris', 67081000, 'Europe')
Task	                       Output
Print the name attribute	   France
Print the capital attribute	   Paris
Print the population attribute 67081000
Print the continent attribute  Europe
Important
You do not need to create any getters or setters; just follow the Python convention for private attributes.
'''

#Code:
class Country:
  def __init__(self, name, capital, population, continent):
    self._name = name
    self._capital = capital
    self._population = population
    self._continent = continent
# Initialize an object of the Country class
my_country = Country('France', 'Paris', 67081000, 'Europe')

# Print the attributes
print(my_country._name)        # Output: France
print(my_country._capital)     # Output: Paris
print(my_country._population)  # Output: 67081000
print(my_country._continent)   # Output: Europe