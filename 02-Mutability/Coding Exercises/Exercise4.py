'''
Exercise 4
Use the Library class below for this coding exercise.
class Library:
  """List of available books and list of books on loan"""
  def __init__(self):
    self.available = []
    self.on_loan = []
Create the following methods for the Library class:
add_books - takes a list of book titles (strings) and adds each title to the list of available books
borrow_book - takes a book title (string) and moves it from the available list to the list of books on loan
return_book - takes a book title (string) and moves it from the list of books on loan to the list of available books
Expected Output
Assume you have an instance of the Library class called my_library. Add some books to object, and then print the list of available books.
my_library.add_books(["Four Seasons", "Say Nothing", "Milkman", "Harry Potter and the Order of the Phoenix"])
print(my_library.available)
You should see the following output:
["Four Seasons", "Say Nothing", "Milkman", "Harry Potter and the Order of the Phoenix"]
Now borrow “Harry Potter and the Order of the Phoenix” and "Say Nothing". Then print the lists of available books and books on loan.
my_library.borrow_book("Harry Potter and the Order of the Phoenix")
my_library.borrow_book("Say Nothing")
print(my_library.available)
print(my_library.on_loan)
You should see the following output:
["Four Seasons", "Milkman"]
["Harry Potter and the Order of the Phoenix", "Say Nothing"]
Finally, return the “Say Nothing” and print the lists of the books on loan and the available books.
my_library.return_book("Say Nothing")
print(my_library.available)
print(my_library.on_loan)
You should see the following output:
["Four Seasons", "Milkman", "Say Nothing"]
["Harry Potter and the Order of the Phoenix"]'''

#Code:
class Library:
    """List of available books and list of books on loan"""
    def __init__(self):
        self.available = []
        self.on_loan = []
    
    def add_books(self, book_titles):
        """Add a list of book titles to the available books"""
        self.available.extend(book_titles)
    
    def borrow_book(self, book_title):
        """Move a book from available to on_loan"""
        if book_title in self.available:
            self.available.remove(book_title)
            self.on_loan.append(book_title)
        else:
            print(f"Book '{book_title}' is not available.")

    def return_book(self, book_title):
        """Move a book from on_loan to available"""
        if book_title in self.on_loan:
            self.on_loan.remove(book_title)
            self.available.append(book_title)
        else:
            print(f"Book '{book_title}' is not on loan.")

# Example usage:
my_library = Library()

# Add books to the library
my_library.add_books(["Four Seasons", "Say Nothing", "Milkman", "Harry Potter and the Order of the Phoenix"])

# Print the list of available books
print(my_library.available)

# Borrow some books
my_library.borrow_book("Harry Potter and the Order of the Phoenix")
my_library.borrow_book("Say Nothing")

# Print lists of available books and books on loan
print(my_library.available)
print(my_library.on_loan)

# Return a book
my_library.return_book("Say Nothing")

# Print lists after returning a book
print(my_library.available)
print(my_library.on_loan)

