from interfaces.store import RateLimitStore

class InMemoryStore(RateLimitStore):
    def __init__(self):
        self.buckets = {}

    def get_bucket(self, client_id: str):
        return self.buckets.get(client_id)

    def save_bucket(self, client_id: str, bucket):
        self.buckets[client_id] = bucket