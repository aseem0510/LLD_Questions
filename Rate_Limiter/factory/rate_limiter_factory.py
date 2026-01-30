from enums import RateLimitAlgorithm
from limiters.token_bucket_limiter import TokenBucketRateLimiter

class RateLimiterFactory:
    @staticmethod
    def get_limiter(algorithm, store, config):
        if algorithm == RateLimitAlgorithm.TOKEN_BUCKET:
            return TokenBucketRateLimiter(store, config)
        raise ValueError("Unsupported rate limiting algorithm")