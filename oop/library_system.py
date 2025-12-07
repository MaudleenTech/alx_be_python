# Library System demonstrating Inheritance and Composition

class Book:
    # Base class for all book types.
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        # Basic string representation.
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    # Derived class for electronic books.
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size # Unique attribute

    def __str__(self):
        # EBook-specific string representation.
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    # Derived class for physical print books.
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count # Unique attribute

    def __str__(self):
        # PrintBook-specific string representation.
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    # Manages a collection of Book objects (Composition).
    def __init__(self):
        self.books = []

    def add_book(self, book):
        # Adds any book type to the collection.
        self.books.append(book)

    def list_books(self):
        # Prints details of all books using polymorphism via __str__.
        for book in self.books:
            print(book)