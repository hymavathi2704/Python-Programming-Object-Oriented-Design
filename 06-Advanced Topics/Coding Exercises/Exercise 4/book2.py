class Book:
  def __init__(self, title, author, genre):
    self.author = author
    self.title = title
    self.genre = genre
    
  def __repr__(self):
    return f'Book({self.title}, {self.author}, {self.genre})'