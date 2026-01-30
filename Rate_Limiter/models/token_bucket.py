import time
import threading

class TokenBucket:
    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate
        self.last_refill_timestamp = time.time()
        self.lock = threading.Lock()

    def try_consume(self) -> bool:
        with self.lock:
            self._refill()
            if self.tokens >= 1:
                self.tokens -= 1
                return True
            return False

    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill_timestamp
        refill_tokens = elapsed * self.refill_rate
        if refill_tokens > 0:
            self.tokens = min(self.capacity, self.tokens + refill_tokens)
            self.last_refill_timestamp = now