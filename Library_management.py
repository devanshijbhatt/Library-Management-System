import pandas as pd

# Library_management.py
class Book:
    def __init__(self, isbn, title, author, publication_year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year

class Library_Management:
    """
    This class is used to keep records of books in the library.
    It has total four modules: 'Display Books', 'Borrow Books', 'Add Books', 'Return Books'
    """
    isbn_counter = 0  # Class-level variable to keep track of ISBN numbers

    def __init__(self):
        # Create an empty dataframe to store books
        self.books_df = pd.DataFrame(columns=["ISBN", "Title", "Author", "Publication Year", "Is Borrowed"])

    def add_book(self, title, author, publication_year):
        # Increment the ISBN counter by 1 for each new book
        Library_Management.isbn_counter += 1
        isbn = Library_Management.isbn_counter
        
        # Create a new Book object
        book = Book(isbn, title, author, publication_year)

        # Add the book details to the DataFrame using concat
        new_book_df = pd.DataFrame([{
            "ISBN": book.isbn,
            "Title": book.title,
            "Author": book.author,
            "Publication Year": book.publication_year,
            "Is Borrowed": False
        }])

        self.books_df = pd.concat([self.books_df, new_book_df], ignore_index=True)
        print(f"Book '{book.title}' added to the library with ISBN '{book.isbn}'.")
        print(self.books_df)