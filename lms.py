import time

class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self.is_borrowed = False
    
    def __str__(self):
      status = "Available" if not self.is_borrowed else "Borrowed"
      return f"{self.title} by {self.author} status - {status}"
      
class Libary:
  def __init__(self):
    self.books = []
    
  def add_book(self, title, author):
    book = Book(title, author)
    self.books.append(book)      
    print(f"Successfully added book - {title}")
    
  def view_book(self):
    if not self.books:
      print("No book in the library")
    else:
      for b in self.books:
        print(f"{b.title}\n__________\n___________")
        
  def borrow_book(self,title):
    for books in self.books:
      if books.title == title and not books.is_borrowed:
        books.is_borrowed = True
        print(f"You have successfully borrowed {books.title} by {books.author}")
      elif books.title == title and  books.is_borrowed:
          print(f"{title} is borrowed")
      else:
          print(f"Reverse for book with title - {title} not found")

        
  def return_book(self, title):
    for book in self.books:
      if book.title == title and book.is_borrowed:
        book.is_borrowed = False
        print("Return success")

  def search_book(self, query):
      for book in self.books:
          if query in  book.title or query in book.author:
              print(f"{book.title} by {book.author}\n____________\n")
          else:
              print(f"Result for {query} not found!!!")
       
    


def main():
    library = Libary()

    while True:
        print("Welcome to junior's signature Library")
        print("Choose a number 1-6:")
        print("1. Add book to library")
        print("2. view books in library")
        print("3. Borrow a book")
        print("4. Return borrowed book")
        print("5. Search for a book")
        print("6. quit")
        try:
            option = int(input("Enter option: "))
        except ValueError:
            print("Invalid option\nEnter option 1-5\n")
        if option == 1:
            title = input("Enter book title: ")
            author = input("Enter author's name: ")
            library.add_book(title=title, author=author)
        elif option  == 2:
            library.view_book()
        elif option == 3:
            title = input("Enter book title: ")
            library.borrow_book(title=title)
        elif option == 4:
            title = input("Enter book title: ")
            library.return_book(title=title)
        elif option == 5:
            query = input("search book by title or author's name\n: ")
            library.search_book(query=query)
        elif option == 6:
            ask = input("Are you sure you want to quit? (y/n): ").lower()
            if ask == "y":
                print("Exiting junior's signature library")
                time.sleep(3)
                print("Bye")
                break
            elif ask == "n":
                continue
            else:
                print("Invalid Input\nTry again!!!")
                
        else:
            print("Invalid Input")
            
            
        
        
main();
        
        
        
    
    
