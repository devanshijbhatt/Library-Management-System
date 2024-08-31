import unittest
from Library_management import Library_Management, Book  # Import necessary classes

class TestLibrary(unittest.TestCase):
    def test_addbooks(self):
        """
        Test that it can add books in the system
        """
        library = Library_Management()  # Create an instance of the Library_Management class
        book = Book("BID001", "The Great Gatsby", "F. Scott Fitzgerald", 1925)  # Create a Book instance
        library.add_book(book)  # Add the book to the library
        
        # Check if the book was added successfully
        result = "BID001" in library.books_df['ISBN'].values
        self.assertTrue(result, "The book was not added successfully.")

if __name__ == '__main__':
    unittest.main()
