from abc import ABC, abstractmethod

class FinePolicy(ABC):
    @abstractmethod
    def calculate_fine(self, borrowed_days: int, allowed_days: int) -> int:
        pass