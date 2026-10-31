"""
Drill 07: Function Call Counter
Module: 04-decorators-and-closures
"""
from functools import wraps


def count_calls(func: callable) -> callable:
    """
    Decorator tracking invocation frequency on wrapper.calls.
    """
    # TODO: Implement count_calls decorator
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper
