"""
Drill 03: Announce Execution Order
Module: 04-decorators-and-closures
"""


def announce(log_list: list[str]) -> callable:
    """
    Decorator logging DECORATION, BEFORE, and AFTER milestones.
    """
    # TODO: Implement parametric decorator appending to log_list at correct lifecycle phases
    log_list.append("DECORATION")
    def wrapper(func):
        def decorated(*args):
            log_list.append("BEFORE")
            res = func(*args)
            log_list.append("AFTER")
            return res
        return decorated
    return wrapper