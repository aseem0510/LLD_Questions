from enum import Enum

class RateLimitAlgorithm(Enum):
    TOKEN_BUCKET = "TOKEN_BUCKET"

class TimeUnit(Enum):
    SECOND = 1
    MINUTE = 60