# book.py

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def __repr__(self):
        return f'Book({self.title}, {self.author}, {self.genre})'

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author and self.genre == other.genre
        return False

    def __lt__(self, other):
        return self.title < other.title
