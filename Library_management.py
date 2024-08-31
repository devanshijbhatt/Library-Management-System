import pandas as pd

class Book:
    def __init__(self, isbn, title, author, publication_year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year

class Library_Management:
    """
    This class is used to keep records of books in the library.
    It has total four modules: 'Display Books', 'Borrow Books', 'Add Books', 'Return Books'"""
    def __init__(self):
        # Create and empty dataframe to store books
        self.books_df = pd.DataFrame(columns= ["ISBN", "Title", "Author", "Publication Year", "Is Borrowed"])
    def add_book(self,book):
        # Check if the book with the same ISBN already exists
        if book.isbn in self.books_df['ISBN'].values:
            print("A book with this ISBN already exists.")
        else:
            # Add the book details to the DataFrame
            new_book_df =  pd.DataFrame([{
                "ISBN": book.isbn,
                "Title": book.title,
                "Author": book.author,
                "Publication Year": book.publication_year,
                "Is Borrowed": False
            }])
            self.books_df = pd.concat([self.books_df, new_book_df], ignore_index=True)
            print(f"Book '{book.title}' added to the library.")
