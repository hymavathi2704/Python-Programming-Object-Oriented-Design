'''
Use the parent classes to the left to help you solve this problem. The first parent is the Person class with some very generic information. The second class, CardHolder, is the class for a credit card holder. Create the child class PlantinumClient. This class inherits all of the attributes of both parent classes. In addition, the child class has the attributes cash_back and rewards. cash_back should be set to 0.02 and rewards should be set to 0. Override the process_sale method so that 2% of each sale is added to rewards.
Expected Output
Declare an instance of the PlatinumClient class as shown below.
platinum = PlatinumClient("Sarah", "101 Main Street", 123364)
Your class should be able to execute the code below in the stated order and produce the given return values.
Order	Code	Return Value
1	platinum.process_sale(100)	N/A
2	print(platinum.rewards)	2
3	print(platinum.balance)	100
4	platinum.make_payment(50)	N/A
5	print(platinum.balance)	50
6	print(platinum.get_info())	Sarah lives at 101 Main Street.'''

#Code:
# parent classes
class Person:
  def __init__(self, name, address):
    self.name = name
    self.address = address
    
  def get_info(self):
    return f"{self.name} lives at {self.address}."
  
class CardHolder:
  def __init__(self, account_number):
    self.account_number = account_number
    self.balance = 0
    self.credit_limit = 5000
    
  def process_sale(self, price):
    self.balance += price
    
  def make_payment(self, amount):
    self.balance -= amount
    
# declare child class here
class PlatinumClient(Person, CardHolder):
  def __init__(self, name, address, account_number):
    Person.__init__(self, name, address)
    CardHolder.__init__(self, account_number)
    self.cash_back = 0.02
    self.rewards = 0
    
  def process_sale(self, price):
    self.balance += price
    self.rewards += self.cash_back * price

    # Instantiate the PlatinumClient object
platinum = PlatinumClient("Sarah", "101 Main Street", 123364)

# Execute the code in the stated order and print the return values
platinum.process_sale(100)     # N/A
print(platinum.rewards)        # Output: 2
print(platinum.balance)        # Output: 100
platinum.make_payment(50)      # N/A
print(platinum.balance)        # Output: 50
print(platinum.get_info())     # Output: Sarah lives at 101 Main Street.