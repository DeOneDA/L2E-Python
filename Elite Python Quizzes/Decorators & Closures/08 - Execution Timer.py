"""
Drill 08: Execution Timer Decorator
Module: 04-decorators-and-closures
"""
import time
from functools import wraps


def time_execution(func: callable) -> callable:
    """
    Decorator timing function execution and storing in wrapper.last_duration.
    """
    # TODO: Implement execution timer wrapper
    @wraps(func)
    def wrapper(*args):
        start = time.perf_counter()
        res = func(*args)
        wrapper.last_duration = time.perf_counter() - start
        return res
    wrapper.last_duration = 0
    return wrapper
