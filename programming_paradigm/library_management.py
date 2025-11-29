#!/usr.bin/env python3

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def check_in(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out: {title}")
                    return True
                else:
                    print(f"Error: '{title}' is already checked out.")
                    return False
        print(f"Error: Book with title '{title}' not found.")
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_in():
                    print(f"Returned: {title}")
                    return True
                else:
                    print(f"Error: '{title}' was not checked out.")
                    return False
        print(f"Error: Book with title '{title}' not found.")
        return False

    def list_available_books(self):
        available_count = 0
        for book in self._books:
            if book.is_available():
                print(book)
                available_count += 1
        
        if available_count == 0:
            print("No books are currently available.")