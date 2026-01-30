from library_manager import LibraryManager
from book import Book
from member import Member

lm = LibraryManager()

lm.add_book(Book("ISBN1", "Clean Code", "Robert Martin", 2008))
lm.add_book(Book("ISBN2", "Design Patterns", "GoF", 1994))

lm.register_member(Member("M1", "Aseem", "aseem@email.com"))

lm.borrow_book("M1", "ISBN1")
print([b.title for b in lm.search_books("clean")])
lm.return_book("ISBN1")