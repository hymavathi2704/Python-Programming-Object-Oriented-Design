'''
The code to the left creates a class called Bank. This class has a branch name, the number of customers, and a list of the amount of money in each customer’s bank account. The method branch_total takes the list of customer money and returns the total amount of money held by the bank.
Create the class RegionalBank as a child of the Bank class. This class has a name, the number of customers in the region, and a 2D list of all of the money in the bank accounts for each branch. Extend the RegionalBank class by adding the method regional_total which returns the total amount of money kept in all of the banks in the region.
Instantiate an object from the RegionalBank class and use the variable accounts as the 2D list of bank account. Print out the result from regional_total.
Expected Output
The TRY IT button will run your code with the following value for the accounts variable. Your program should print 170000.
accounts = [
              [10000, 13000, 22000],
              [30000, 7000, 19000],
              [15000, 23000, 31000]
           ]
'''

#Code:
# DO NOT ALTER THIS CODE
import sys
strings = [l.split(",") for l in sys.argv[1].split("*")]
accounts = [[int(n) for n in s] for s in strings]

class Bank:
  def __init__(self, name, customers, accounts):
    self.name = name
    self.customers = customers
    self.accounts = accounts
    
  def branch_total(self, accounts):
    total = 0
    for account in accounts:
      total += account
    return total

# Write your code here
class RegionalBank(Bank):
  def regional_total(self):
    total = 0
    for account in accounts:
      total += self.branch_total(account)
    return total
  
my_bank = RegionalBank("Bank of America", 9, accounts)
print(my_bank.regional_total())