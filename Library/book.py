class Book:
    def __init__(self, isbn: str, title: str, author: str, year: int):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.available = True