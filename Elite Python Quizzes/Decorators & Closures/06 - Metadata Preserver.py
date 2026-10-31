"""
Drill 06: Metadata Preserver
Module: 04-decorators-and-closures
"""
from functools import wraps


def logged(func: callable) -> callable:
    """
    Decorator preserving original function metadata.
    """
    # TODO: Implement wrapper using @wraps(func)
    @wraps(func)
    def wrapper(*args):
        return func(*args)
    return wrapper

