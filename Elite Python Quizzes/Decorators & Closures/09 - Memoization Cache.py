"""
Drill 09: Memoization Cache Decorator
Module: 04-decorators-and-closures
"""
from functools import wraps


def memoize(func: callable) -> callable:
    """
    Decorator caching results for positional arguments in wrapper.cache.
    """
    # TODO: Implement memoization decorator
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]

        cache[args] = func(*args)
        return cache[args]
    wrapper.cache = cache
    return wrapper
