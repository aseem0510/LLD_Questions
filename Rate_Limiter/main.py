from factory.rate_limiter_factory import RateLimiterFactory
from store.in_memory_store import InMemoryStore
from config.rate_limit_config import RateLimitConfig
from enums import RateLimitAlgorithm
store = InMemoryStore()
config = RateLimitConfig(capacity=1, refill_rate=1)  # 5 req burst, 1/sec

limiter = RateLimiterFactory.get_limiter(
    RateLimitAlgorithm.TOKEN_BUCKET,
    store,
    config
)

client1 = "user_123"

for i in range(10):
    print(limiter.allow(client1))