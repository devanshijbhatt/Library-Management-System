# Library Management System
## Problem Statement
This is a technical assessment designed by Incubyte in which the task was to develop a Library Management System which should have four functionalities which are Add new books, Borrow the books, Return the borrowed books and View available books.

## Features
* Add Books: Add new books to the library with an auto-generated ISBN.
* Borrow Books: Borrow books if they are available.
* Return Books: Return borrowed books.
* View Available Books: Display a list of all available books in the library.

## Solution
I have provided the solution for this assessment. I have used Python Language and used Pandas library for creating the small database for the library and have desinged four functions for adding, borrowing, returning and viewing the available books. I have created some test cases to test the modules of the system using unittest library. 

### Prerequisites
Before you begin, ensure you have the following installed:
* Python 3.7 or later
* pip (Python package installer)

To run the Library Management System and Test cases you need to install and import two libraries which are Pandas and unittest. To install these libraries perform these commands in the terminal.
```bash
$ pip install pandas
```
```bash
import pandas as pd
```
```bash
import unittest
```

### Usage
You can use the system by running the python script in this manner. These are some of the examples to access the modules.

1. Add Books
```bash
from Library_management import Library_Management
library = Library_Management()
library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
```
2. Borrow Books
```bash
library.borrow_book("The Great Gatsby", 1)
```
3. Return Books:
```bash
library.return_book("The Great Gatsby", 1)
```
4. View Available Books
```bash
library.view_available_books()
```

# Running the tests
To run the all test cases for the Library Management System, use the following command:
```bash
python -m unittest test_library_management.py
```

To run a particular module, use the below function:
```bash
python -m unittest test_borrow_book
```
## Contributing
If you'd like to contribute, feel free to fork the repository and submit a pull request. For any issues or suggestions, please open an issue on GitHub.

## License
This project is licensed under the MIT License.