1️⃣ Requirements
✅ Functional Requirements

1- Limit API requests per client (user / API key / IP).
2- Support different rate-limiting algorithms:
    - Token Bucket (primary)
    - Fixed Window / Sliding Window (future-ready)
3- Configurable limits:
    - Requests per second/minute/hour
4- Thread-safe handling of concurrent requests.
5- Allow/Reject requests in O(1) time.
6- Pluggable storage:
    - In-memory (LLD focus)
    - Redis (future extension)

🚫 Non-Functional Requirements

- Low latency (decision in < 1ms).
- Scalable (can move to distributed store).
- High availability (no single point of failure).
- Extensible (new algorithms without changing existing code).
- Maintainable & testable (SOLID compliant).
- Thread-safe.

2️⃣ Classes, Interfaces & UML Diagram
🧩 Core Components


| Interface        | Responsibility                            |
| ---------------- | ----------------------------------------- |
| `RateLimiter`    | Contract for all rate-limiting algorithms |
| `RateLimitStore` | Abstract storage (in-memory / Redis)      |

| Enum                 | Purpose             |
| -------------------- | ------------------- |
| `RateLimitAlgorithm` | Algorithm selection |
| `TimeUnit`           | SECOND, MINUTE      |

| Class                    | Responsibility                     |
| ------------------------ | ---------------------------------- |
| `TokenBucketRateLimiter` | Token bucket logic                 |
| `TokenBucket`            | Holds tokens & refill logic        |
| `InMemoryStore`          | Stores buckets per client          |
| `RateLimiterFactory`     | Creates limiter based on algorithm |
| `RateLimitConfig`        | Configuration holder               |


(Textual UML – interviewer friendly)
+------------------+
|  RateLimiter     |<<interface>>
+------------------+
| allow(clientId)  |
+------------------+
        ^
        |
+---------------------------+
| TokenBucketRateLimiter   |
+---------------------------+
| store: RateLimitStore    |
| config: RateLimitConfig  |
+---------------------------+
| allow(clientId)          |
+---------------------------+

+----------------------+
| TokenBucket          |
+----------------------+
| capacity             |
| tokens               |
| refillRate           |
| lastRefillTimestamp  |
+----------------------+
| tryConsume()         |
| refill()             |
+----------------------+

+----------------------+
| RateLimitStore       |<<interface>>
+----------------------+
| getBucket(clientId)  |
| saveBucket(...)      |
+----------------------+

+----------------------+
| InMemoryStore        |
+----------------------+
| buckets: Map         |
+----------------------+

+----------------------+
| RateLimiterFactory   |
+----------------------+
| getLimiter(...)      |
+----------------------+

3️⃣ SOLID Principles Used

✅ S — Single Responsibility
    - TokenBucket → Only token logic
    - InMemoryStore → Only storage
    - RateLimiterFactory → Only creation logic

✅ O — Open/Closed
    - New algorithm (Sliding Window) → add new class
    - No modification in existing code

✅ L — Liskov Substitution
    - Any RateLimiter implementation can replace another

✅ I — Interface Segregation
    - RateLimiter and RateLimitStore are small & focused

✅ D — Dependency Inversion
    - TokenBucketRateLimiter depends on RateLimitStore interface, not concrete class

4️⃣ Design Patterns Used
| Pattern                            | Where                                 | Why                      |
| ---------------------------------- | ------------------------------------- | ------------------------ |
| **Strategy**                       | Different RateLimiter implementations | Switch algorithms easily |
| **Factory**                        | `RateLimiterFactory`                  | Centralized creation     |
| **Singleton** (optional)           | Store                                 | Shared state             |
| **Template Method** (conceptually) | RateLimiter interface                 | Common contract          |
