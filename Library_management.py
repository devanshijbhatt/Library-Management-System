import pandas as pd

class BookNotAvailableError(Exception):
    pass

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
        # print(self.books_df)
    
    def borrow_book(self, book_title, isbn):
        # Check if the book is available for borrowing
        if isbn in self.books_df['ISBN'].values:
            # Find the index of the book in the DataFrame
            book_index = self.books_df[self.books_df['ISBN'] == isbn].index[0]
            
            # Check if the book is borrowed or not
            if not self.books_df.at[book_index, 'Is Borrowed']:
                # Mark the book as borrowed
                self.books_df.at[book_index, 'Is Borrowed'] = True
                print("Book has been borrowed")
                print(self.books_df)
            else:
                print("Book is not available to borrow")
        else:
            print("Book not present")
    
    def return_book(self, book_title, isbn):
        if isbn in self.books_df['ISBN'].values:
            # Use ISBN to find the book index
            book_index = self.books_df[self.books_df['ISBN'] == isbn].index[0]
            # Check if the book is borrowed
            '''Check if isbn code which is given as input has same title as input in the dataframe'''
            if self.books_df.at[book_index, 'Is Borrowed']:
                self.books_df.at[book_index, 'Is Borrowed'] = False
                print("Book has been returned")
                print(self.books_df)
            else: 
                print("Book is already there. Check the ISBN code again.")
        else:
            print("The book which you want to return is not registered in the system.")
            
    def view_available_books(self):
        '''Test attempts to view all the books available in the library'''
