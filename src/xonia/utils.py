from traceback import format_exception

__all__ = [
    "exc"
]

exc = lambda e: "".join(format_exception(e, e, e.__traceback__))