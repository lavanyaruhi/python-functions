from functools import lru_cache

@lru_cache(maxsize=3)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(9))  # Output: 5
print(fibonacci(10))  # Output: 55
print(fibonacci.cache_info())  # Output: CacheInfo(hits=2, misses=9, maxsize=3, currsize=3)
