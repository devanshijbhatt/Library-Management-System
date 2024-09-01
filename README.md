# Library Management System
## Problem Statement
This is a technical assessment designed by Incubyte in which the task was to develop a Library Management System which should have four functionalities which are Add new books, Borrow the books, Return the borrowed books and View available books.
These are the requirements for each modules.
1. Add Books:
* Users should be able to add new books to the library.
* Each book should have a unique identifier (e.g., ISBN), title, author, and
publication year.
2. Borrow Books:
* Users should be able to borrow a book from the library.
* The system should ensure that the book is available before allowing it to be
borrowed.
* If the book is not available, the system should raise an appropriate error.
3. Return Books:
* Users should be able to return a borrowed book.
* The system should update the availability of the book accordingly.
4. View Available Books:
* Users should be able to view a list of all available books in the library.

## Solution
I have provided the solution for this assessment. I have used Python Language and used Pandas library for creating the small database for the library and have desinged four functions for adding, borrowing, returning and viewing the available books. I have created some test cases to test the modules of the system using unittest library. 
To run the Library Management System and Test cases you need to install and import two libraries which are Pandas and unittest. To install these libraries perform these commands in the terminal.
$ pip install pandas
import pandas as pd
import unittest