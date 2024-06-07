#Complete the Airplane and Train classes so that when an instance of each is passed to the passengers function, they will return the total number of passengers on board.

#Code:



class Airplane:
  def __init__(self, first_class, business_class, coach):
    self.first_class = first_class
    self.business_class = business_class
    self.coach = coach
    
  def total(self):
    return self.first_class + self.business_class + self.coach
  
class Train:
  def __init__(self, car1, car2, car3, car4, car5):
    self.car1 = car1
    self.car2 = car2
    self.car3 = car3
    self.car4 = car4
    self.car5 = car5
    
  def total(self):
    return self.car1 + self.car2 + self.car3 + self.car4 + self.car5
  
def passengers(obj):
  print(f'There are {obj.total()} passengers on board.')

  # Create instances of Airplane and Train
airplane = Airplane(10, 20, 150)
train = Train(30, 40, 50, 60, 70)

# Call the passengers function with instances of Airplane and Train
passengers(airplane)  # Output: There are 180 passengers on board.
passengers(train)     # Output: There are 250 passengers on board.
