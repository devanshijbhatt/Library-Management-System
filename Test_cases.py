import unittest
from Library_management import Library_Management,BookNotAvailableError, Book

class TestLibrary(unittest.TestCase):
    def test_add_books(self):
        """
        Test that it can add books to the system with auto-generated ISBN.
        """
        library = Library_Management()

        # Add a book to the library
        library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

        # Check if the book was added successfully
        added_book = library.books_df.iloc[0]
        self.assertEqual(added_book["Title"], "The Great Gatsby")
        self.assertEqual(added_book["Author"], "F. Scott Fitzgerald")
        self.assertEqual(added_book["Publication Year"], 1925)
        
        library.add_book("To Kill a Mockingbird", "Harper Lee", 1960)
        added_book = library.books_df.iloc[1]
        self.assertEqual(added_book["Title"], "To Kill a Mockingbird")
        self.assertEqual(added_book["Author"], "Harper Lee")
        self.assertEqual(added_book["Publication Year"], 1960)
        
    def test_borrow_book(self):
        """
        Test that it can borrow a book from the library if it's available
        """
        library = Library_Management()
        library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
        library.add_book("To Kill a Mockingbird", "Harper Lee", 1960)

        # Borrow the first book (ISBN should be 1)
        library.borrow_book("The Great Gatsby",1)
        
    def test_borrow_book_not_available(self):
        """
        Test that attempting to borrow a book that is already borrowed raises an error.
        """
        library = Library_Management()
        library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
        library.borrow_book("The Great Gatsby", 1)
        library.borrow_book("The Great Gatsby",1)
    
    def test_borrow_book_not_present(self):
        ''' Test that attempts to borrow a book which is not available in the library'''
        library = Library_Management()
        library.add_book("The Twilight Saga", "Stephenie Meyer", 2005)
        library.borrow_book("New Moon", 3)
        
    def test_return_book(self):
        '''Test that attempts to return the borrowed book'''
        library = Library_Management()
        library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
        library.add_book("The Twilight Saga", "Stephenie Meyer", 2005)
        library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
        # Borrow the book
        library.borrow_book("The Great Gatsby", 3)
        library.return_book("The Great Gatsby", 3)
        # Check if the book is marked as not borrowed
        book_status = library.books_df[library.books_df['ISBN'] == 3].iloc[0]['Is Borrowed']
        self.assertFalse(book_status, "The book was not marked as returned.")
        
    def test_return_book_not_borrowed(self):
        '''Test attempts to return a book which was not borrowed'''
        library = Library_Management()
        library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
        library.add_book("The Twilight Saga", "Stephenie Meyer", 2005)
        library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
        # Borrow the book
        library.borrow_book("The Twilight Saga", 2)
        library.return_book("The Great Gatsby", 3)
        
    def test_return_book_not_present(self):
        '''Test attempts to return a book which is not even added in the library'''
        library = Library_Management()
        library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
        library.add_book("The Twilight Saga", "Stephenie Meyer", 2005)
        library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
        library.return_book("New Moon", 4)
        
    
    
        
if __name__ == '__main__':
    unittest.main()
