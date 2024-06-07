'''Create the class Characters which has the attribute phrases which is a list of strings passed as a parameter. Overload the <, >, and == operators so that you can make comparisons based on the total number of characters in the string.
Expected Output
If you were to run the following code with your class, the output would be True, False, and True.
sample_phrases1 = ['cat in the hat', 'green eggs and ham', 'the lorax']
sample_phrases2 = ['the taming of the shrew', 'hamlet', 'othello']

c1 = Characters(sample_phrases1)
c2 = Characters(sample_phrases2)
print(c1 > c2) # prints 'True'
print(c1 < c2) # prints 'False'
print(c1 == c1) # prints 'True'
'''

#Code:
class Characters:
  def __init__(self, phrases):
    self.phrases = phrases
    
  def total_characters(self):
    total = 0
    for phrase in self.phrases:
      total += len(phrase)
    return total
    
  def __gt__(self, obj):
    return self.total_characters() > obj.total_characters()
  
  def __lt__(self, obj):
    return self.total_characters() < obj.total_characters()
  
  def __eq__(self, obj):
    return self.total_characters() == obj.total_characters()
  
sample_phrases1 = ['cat in the hat', 'green eggs and ham', 'the lorax']
sample_phrases2 = ['the taming of the shrew', 'hamlet', 'othello']

c1 = Characters(sample_phrases1)
c2 = Characters(sample_phrases2)
print(c1 > c2) # prints 'True'
print(c1 < c2) # prints 'False'
print(c1 == c1) # prints 'True'