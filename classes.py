class Book:
  def __init__(self,title,author):
    self.title = title
    self.author = author
    
  def display_info(self):
    return f"Book {self.title} by {self.author}"
    
    
my_book = Book("9084", "George allwell")
my_book2 = Book("The code book", "simon singh")

print(my_book.display_info)
print(my_book2.display_info)