from datetime import datetime
from book import Book
from member import Member
from borrow_transaction import BorrowTransaction
from default_fine_policy import DefaultFinePolicy
from payment_processor import PaymentProcessor
from upi_payment import UPIPayment

class LibraryManager:
    _instance = None

    MAX_BOOKS = 5
    LOAN_DAYS = 15

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.books = {}
            cls._instance.members = {}
            cls._instance.transactions = {}
            cls._instance.fine_policy = DefaultFinePolicy()
        return cls._instance

    # -------- Book Management --------
    def add_book(self, book: Book):
        self.books[book.isbn] = book
        print(f"Book '{book.title}' added.")

    def remove_book(self, isbn: str):
        if isbn in self.transactions:
            raise Exception("Book is currently borrowed")

        if isbn not in self.books:
            raise Exception("Book not found")

        del self.books[isbn]
        print(f"Book with ISBN '{isbn}' removed.")

    def search_books(self, keyword: str):
        keyword = keyword.lower()
        return [
            book for book in self.books.values()
            if keyword in book.title.lower()
            or keyword in book.author.lower()
            or keyword in book.isbn.lower()
        ]

    # -------- Member Management --------
    def register_member(self, member: Member):
        self.members[member.member_id] = member
        print(f"Member '{member.name}' registered.")

    def unregister_member(self, member_id: str):
        for txn in self.transactions.values():
            if txn.member_id == member_id:
                raise Exception("Member has active borrowed books")

        if member_id not in self.members:
            raise Exception("Member not found")

        del self.members[member_id]
        print(f"Member with ID '{member_id}' unregistered.")

    # -------- Borrow / Return --------
    def borrow_book(self, member_id: str, isbn: str):
        if member_id not in self.members:
            raise Exception("Invalid member")

        book = self.books.get(isbn)
        if not book or not book.available:
            raise Exception("Book not available")

        self.transactions[isbn] = BorrowTransaction(member_id, isbn)
        book.available = False
        print(f"Book '{book.title}' borrowed by member '{self.members[member_id].name}'.")

    def return_book(self, isbn: str):
        txn = self.transactions.pop(isbn, None)
        if not txn:
            raise Exception("Invalid return")

        borrowed_days = (datetime.now() - txn.borrowed_at).days
        fine = self.fine_policy.calculate_fine(borrowed_days, self.LOAN_DAYS)

        if fine > 0:
            if PaymentProcessor(UPIPayment()).process(fine):
                self.books[isbn].available = True
                print(f"Book returned with a fine of ₹{fine}.")
            else:
                raise Exception("Payment failed")
        else:
            self.books[isbn].available = True
            print("Book returned on time. No fine.")