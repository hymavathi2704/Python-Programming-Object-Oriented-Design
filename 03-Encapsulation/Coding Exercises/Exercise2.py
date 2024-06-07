'''
Exercise 2
Define the Artist class which has attributes for name, medium, style, and famous_artwork. Do not use the Python convention to make these attributes.
Expected Output
Initialize an object of the Artist class as follows:
my_artist = Artist('Bill Watterson', 'ink and paper', 'cartoons', 'Calvin and Hobbes')
Task	Output
Print the name attribute	Error Message
Print the medium attribute	Error Message
Print the style attribute	Error Message
Print the famous artwork attribute	Error Message
Print _Artist__name	Bill Watterson
Print _Artist__medium	ink and paper
Print _Artist__style	cartoons
Print _Artist__famous_artwork	Calvin and Hobbes
Important
You do not need to create any getters or setters; do not follow the Python convention for private attributes.
'''

#Code:
class Artist:
  def __init__(self, name, medium, style, famous_artwork):
    self.__name = name
    self.__medium = medium
    self.__style = style
    self.__famous_artwork = famous_artwork
# Initialize an object of the Artist class
my_artist = Artist('Bill Watterson', 'ink and paper', 'cartoons', 'Calvin and Hobbes')

# Trying to print the attributes directly will cause an error
try:
    print(my_artist.name)
except AttributeError as e:
    print(f"Error Message: {e}")

try:
    print(my_artist.medium)
except AttributeError as e:
    print(f"Error Message: {e}")

try:
    print(my_artist.style)
except AttributeError as e:
    print(f"Error Message: {e}")

try:
    print(my_artist.famous_artwork)
except AttributeError as e:
    print(f"Error Message: {e}")

# Print the attributes using name mangling
print(my_artist._Artist__name)            # Output: Bill Watterson
print(my_artist._Artist__medium)          # Output: ink and paper
print(my_artist._Artist__style)           # Output: cartoons
print(my_artist._Artist__famous_artwork)  # Output: Calvin and Hobbes