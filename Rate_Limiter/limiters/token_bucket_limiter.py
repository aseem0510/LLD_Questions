from interfaces.rate_limiter import RateLimiter
from models.token_bucket import TokenBucket

class TokenBucketRateLimiter(RateLimiter):
    def __init__(self, store, config):
        self.store = store
        self.config = config

    def allow(self, client_id: str) -> bool:
        bucket = self.store.get_bucket(client_id)
        print(f"Client ID: {client_id}, Bucket before allowance: {bucket}")

        if not bucket:
            print(f"Creating new bucket for client ID: {client_id}")
            bucket = TokenBucket(
                self.config.capacity,
                self.config.refill_rate
            )
            self.store.save_bucket(client_id, bucket)
        
        print(f"Client ID: {client_id}, Bucket after retrieval/creation: {bucket}")

        return bucket.try_consume()