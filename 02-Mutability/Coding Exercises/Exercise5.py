'''
Use the Subway class below to help solve these problems.
class Subway:
  fare = 2.4
  def __init__(self):
    self.stops = ["Alewife", "Davis", "Porter", "Harvard", "Central", "Kendall"]
    self.current_stop= "Alewife"
    self.direction = "south"
    self.passengers = 0
    self.total_fares = 0
Create the following methods for the Subway class:
board - Accepts an integer that represents the number of passengers boarding the subway.
disembark - Accepts an integer that represents the number of passengers exiting the subway. There cannot be a negative number of passengers on a subway. The fewest number of passengers on a subway is 0.
advance - Moves the subway to the next stop. If self.direction is "south" the subway moves from Alewife to Kendall. If self.direction is "north" the subway moves from Kendall to Alewife. When the subway has reached its final stop, self.direction should change.
distance - Accepts a string that represents a stop and returns the number of stops between the subway and the desired stop. The distance should be a positive number.
change_fare - Accepts a float and changes the fare for all instances of the Subway class.
calculate_fares - Calculates the fare for each passenger boarding the subway and adds it to total_fares.
Expected Output
Use the examples below to test if your program is working as expected.
Boarding the Subway
If self.passengers is 220 and 45 people board the subway, then self.passengers would be 265.
Total Fares
If 100 passengers, in total, have boarded the train, the self.total_fares would be 240.
Exiting the Subway
If self.passengers is 113 and 23 people exit the subway, then self.passengers would be 90.
Advancing the Subway
If the subway is currently at Kendall and is traveling South, advancing the subway would change self.current_stop to "Central" and self.direction would become "north". If the subway is currently at Porter and is traveling South, advancing the subway would change self.current_stop to Harvard and self.direction would remain "south".
Calculating Distance
If the subway is currently at Davis and the desired stop is Central, the distance between them is 3 stops.
Changing the Fare
If the subway fare increased to $2.75, then fare should be 2.75 for all instances of the Subway class.'''


#Code:
class Subway:
    fare = 2.4

    def __init__(self):
        self.stops = ["Alewife", "Davis", "Porter", "Harvard", "Central", "Kendall"]
        self.current_stop = "Alewife"
        self.direction = "south"
        self.passengers = 0
        self.total_fares = 0

    def board(self, num_passengers):
        self.passengers += num_passengers
        self.calculate_fares(num_passengers)

    def disembark(self, num_passengers):
        self.passengers = max(0, self.passengers - num_passengers)

    def advance(self):
      current_index = self.stops.index(self.current_stop)
      if self.direction == "south":
         if self.current_stop == "Kendall":
            self.current_stop = "Central"
            self.direction = "north"
         else:
            self.current_stop = self.stops[current_index + 1]
      else:
         if self.current_stop == "Alewife":
            self.current_stop = "Davis"
            self.direction = "south"
         else:
            self.current_stop = self.stops[current_index - 1]

    def distance(self, stop):
        current_index = self.stops.index(self.current_stop)
        target_index = self.stops.index(stop)
        return abs(current_index - target_index)

    @classmethod
    def change_fare(cls, new_fare):
        cls.fare = new_fare

    def calculate_fares(self, num_passengers):
        self.total_fares += num_passengers * Subway.fare

# Example usage and testing

# Create a Subway instance
subway = Subway()

# Boarding the subway
subway.board(45)
print(subway.passengers)  # Expected output: 45

# Total fares
print(subway.total_fares)  # Expected output: 108.0 (45 passengers * 2.4 fare)

# Exiting the subway
subway.board(220)  # Add 220 passengers for testing
subway.disembark(23)
print(subway.passengers)  # Expected output: 242 (265 - 23)

# Advancing the subway
subway.advance()
print(subway.current_stop)  # Expected output: "Davis" (Alewife -> Davis)
print(subway.direction)  # Expected output: "south"

# Further advancing the subway to test direction change
for _ in range(5):  # Move to Kendall and change direction
    subway.advance()
print(subway.current_stop)  # Expected output: "Kendall"
print(subway.direction)  # Expected output: "north"

# Calculating distance
subway.current_stop = "Davis"  # Reset current stop for testing
print(subway.distance("Central"))  # Expected output: 3

# Changing the fare
Subway.change_fare(2.75)
print(Subway.fare)  # Expected output: 2.75
