"""
Drill 05: Arguments Forwarder
Module: 04-decorators-and-closures
"""


def record_call_args(func: callable) -> callable:
    """
    Decorator that tracks last_args and last_kwargs on the returned wrapper.
    """
    # TODO: Implement universal argument capture
    def wrapper(*args, **kwargs):
        wrapper.last_args = args
        wrapper.last_kwargs = kwargs
        return func(*args, **kwargs)
    wrapper.last_args = ()
    wrapper.last_kwargs = {}
    return wrapper