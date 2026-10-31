"""
Drill 04: Return Value Forwarder
Module: 04-decorators-and-closures
"""


def forward_result(func: callable) -> callable:
    """
    Decorator that guarantees the wrapped function's return value is preserved.
    """
    # TODO: Implement wrapper capturing and returning result
    def wrapper(*args):
        res = func(*args)
        return res
    return wrapper
