from datetime import datetime

class BorrowTransaction:
    def __init__(self, member_id: str, isbn: str):
        self.member_id = member_id
        self.isbn = isbn
        self.borrowed_at = datetime.now()