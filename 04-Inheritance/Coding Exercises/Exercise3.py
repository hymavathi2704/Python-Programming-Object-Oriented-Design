'''
Create the class Child such that the following criteria are met:
Child is a subclass of Parent1 and Parent2
Override identify so that it returns “This method is called from Child”
Create the method identify2 that invokes the identify method from Parent2. This must be done using the super() keyword.
Expected Output
Assume that child_object is an instance of the Child class. Then the following would be true:
child_object.identify() would return This method is called from Child
child_object.identify2() would return This method is called from Parent2
'''

#Code:
class Parent1:
  def identify(self):
    return "This method is called from Parent1"
    
class Parent2:
  def identify(self):
    return "This method is called from Parent2"
    
# declare child class here
class Child(Parent2, Parent1):
  def identify(self):
    return "This method is called from Child"
  
  def identify2(self):
    return super().identify()
# Instantiate the Child object
child_object = Child()

# Call the methods and print the results to verify
print(child_object.identify())   # Output: This method is called from Child
print(child_object.identify2())  # Output: This method is called from Parent2
