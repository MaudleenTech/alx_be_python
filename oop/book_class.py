# Book class demonstrating core Python magic methods.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        # Informal string representation
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # Official string representation for recreation
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        # Destructor: prints message upon deletion
        print(f"Deleting {self.title}")