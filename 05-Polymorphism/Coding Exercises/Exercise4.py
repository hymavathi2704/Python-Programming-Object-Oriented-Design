'''
Create the Median that has the method calculate_median that calculates the median of the integers passed to the method. Use method overloading so that this method can accept anywhere from two to five parameters.
How to calculate median

Method Call	Return Value
m.calculate_median(3, 5, 1, 4, 2)	3
m.calculate_median(8, 6, 4, 2)	5.0
m.calculate_median(9, 3, 7)	7
m.calculate_median(5, 2)	3.5'''

#Code:
class Median:
  def calculate_median(self, n1, n2, n3=None, n4=None, n5=None):
    if n3 is not None and n4 is not None and n5 is not None:
      numbers = [n1, n2, n3, n4, n5]
    elif n3 is not None and n4 is not None:
      numbers = [n1, n2, n3, n4]
    elif n3 is not None:
      numbers = [n1, n2, n3]
    else:
      numbers = [n1, n2]
    
    numbers.sort()
    median_index = len(numbers) // 2
    if len(numbers) % 2 == 0:
      median = (numbers[median_index] + numbers[median_index - 1]) / 2
    else:
      median = numbers[median_index]
    return median

# Create an instance of the Median class
m = Median()

# Test cases
print(m.calculate_median(3, 5, 1, 4, 2))  # Output: 3
print(m.calculate_median(8, 6, 4, 2))     # Output: 5.0
print(m.calculate_median(9, 3, 7))        # Output: 7
print(m.calculate_median(5, 2))           # Output: 3.5    