'''
Use the parent class Book to help you solve this problem. Create the child class BlogPost and override the constructor so that the child class has the following attributes:
website - a string that represents the website hosting the blog post
title - a string that represents the title of the blog post
author - a string that represents the author of the blog post
word_count - an integer that represents the number of words in the blog post
genre - a string that represents the genre of the blog post
page_views - an integer that represents the page views for the blog post
Expected Output
The table below shows the expected output for the indicated instantiation. Use the TRY IT button below and verify that your child class works as expected.
Object Instantiation	Print Statement	Output
my_post = BlogPost("Vogue", "Hot Summer Trends", "Amy Gutierrez", 2319, "fashion", 2748)	print(my_post.website)	Vogue
print(my_post.title)	Hot Summer Trends
print(my_post.author)	Amy Gutierrez
print(my_post.word_count)	2139
print(my_post.genre)	fashion
print(my_post.page_views)	2748
'''

#Code:
# parent class
class Book:
  def __init__(self, title, author, genre):
    self.title = title
    self.author = author
    self.genre = genre

# child class
# child class
class BlogPost(Book):
  def __init__(self, website, title, author, word_count, genre, page_views):
    super().__init__(title, author, genre)
    self.website = website
    self.word_count = word_count
    self.page_views = page_views
# Instantiate the BlogPost object
my_post = BlogPost("Vogue", "Hot Summer Trends", "Amy Gutierrez", 2319, "fashion", 2748)

# Print the attributes to verify
print(my_post.website)       # Output: Vogue
print(my_post.title)         # Output: Hot Summer Trends
print(my_post.author)        # Output: Amy Gutierrez
print(my_post.word_count)    # Output: 2319
print(my_post.genre)         # Output: fashion
print(my_post.page_views)    # Output: 2748
