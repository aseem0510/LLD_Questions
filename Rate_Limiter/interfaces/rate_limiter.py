from abc import ABC, abstractmethod

class RateLimiter(ABC):
    @abstractmethod
    def allow(self, client_id: str) -> bool:
        pass