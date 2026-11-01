"""
Drill 10: Input Type Enforcer
Module: 04-decorators-and-closures
"""
from functools import wraps


def enforce_types(*expected_types) -> callable:
    """
    Parametric decorator enforcing types of positional arguments.
    """
    # TODO: Implement type enforcement decorator
    def holder(func):
        @wraps(func)
        def wrapper(*args):
            for i in range(len(args)):
                if type(args[i]) != expected_types[i]:
                    raise TypeError
            res = func(*args)
            return res
        return wrapper
    return holder
