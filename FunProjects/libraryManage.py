class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author):
        self.books[title] = {"author": author, "available": True}
        print(f"Book {title} added.")

    def borrow_book(self, title):
        if title not in self.books:
            print(f"{title} not available.")
        elif self.books[title]["available"] == False:
            print(f"'{title}' is already borrowed.")
        else:
            self.books[title]["available"] = True
            print(f"You borrowed '{title}'.")

    def return_book(self, title):
 
        if self.books[title]["available"] == False:
 
        if  title not in self.books:
           print(f"'{title}' is not in the library.")
        elif self.books[title]["available"] == True:
 
            print(f"'{title}' was not borrowed.")
        else:
            self.books[title]["available"] = True
            print(f"You returned '{title}'")
    def display_books(self):
        for title, details in self.books.items():
            status = "Available" if details["available"] else "Not Available"
            print(f"Title: {title}, Author: {details['author']}, Status: {status}")

 
library = Library()
library.add_book("1984", "George Orwell")
library.borrow_book("1984")
library.return_book("1984")
library.display_books()
