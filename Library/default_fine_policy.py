from fine_policy import FinePolicy

class DefaultFinePolicy(FinePolicy):
    def calculate_fine(self, borrowed_days: int, allowed_days: int) -> int:
        overdue = max(0, borrowed_days - allowed_days)
        return overdue * 10  # ₹10/day