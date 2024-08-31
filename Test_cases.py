import unittest
from Library_management import Library_Management

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


if __name__ == '__main__':
    unittest.main()
