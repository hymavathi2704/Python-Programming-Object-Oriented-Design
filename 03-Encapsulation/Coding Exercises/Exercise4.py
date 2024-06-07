'''
Define the Dancer class which has attributes for name, nationality, and style. Use the Python convention to make these attributes private. Create the getters and setters using the property function.
Expected Output
Initialize an object of the Dancer class as follows:
my_dancer = Dancer("Savion Glover", "American", "tap")
Task	Output
print(my_dancer.name)	Savion Glover
print(my_dancer.nationality)	American
print(my_dancer.style)	tap
my_dancer.name = 'Anna Pavlova'	N/A
my_dancer.nationality = 'Russian'	N/A
my_dancer.style = 'ballet'	N/A
print(my_dancer.name)	Anna Pavlova
print(my_dancer.nationality)	Russian
print(my_dancer.style)	ballet
Important
Use the property function; follow the Python convention for private attributes.'''

#Code:
class Dancer:
  def __init__(self, name, nationality, style):
    self._name = name
    self._nationality = nationality
    self._style = style
    
  def get_name(self):
    return self._name
  
  def set_name(self, new_value):
    self._name = new_value
    
  def get_nationality(self):
    return self._nationality
  
  def set_nationality(self, new_value):
    self._nationality = new_value
    
  def get_style(self):
    return self._style
  
  def set_style(self, new_value):
    self._style = new_value
    
  name = property(get_name, set_name)
  nationality = property(get_nationality, set_nationality)
  style = property(get_style, set_style)

# Example usage
my_dancer = Dancer("Savion Glover", "American", "tap")
print(my_dancer.name)  # Savion Glover
print(my_dancer.nationality)  # American
print(my_dancer.style)  # tap

my_dancer.name = 'Anna Pavlova'
my_dancer.nationality = 'Russian'
my_dancer.style = 'ballet'

print(my_dancer.name)  # Anna Pavlova
print(my_dancer.nationality)  # Russian
print(my_dancer.style)  # ballet