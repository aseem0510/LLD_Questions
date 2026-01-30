from abc import ABC, abstractmethod

class RateLimitStore(ABC):
    @abstractmethod
    def get_bucket(self, client_id: str):
        pass

    @abstractmethod
    def save_bucket(self, client_id: str, bucket):
        pass