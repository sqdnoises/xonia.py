__all__ = [
    "CredentialsError",
    "UnknownEvent",
]


class XoniaException(Exception):
    """Base exception class for all exceptions."""
    pass


class CredentialsError(XoniaException):
    """An exception that is raised when no credentials are given"""

    def __init__(self, message: str | None = None) -> None:
        if message is None:
            message = "No credentials were provided when assigning the class"

        super().__init__(message)


class NotConnectedError(XoniaException):
    """An exception that is raise"""


class UnknownEvent(XoniaException):
    """An exception that is raised when the decorator is used in an unknown event"""

    def __init__(self, func_name: str, message: str | None = None) -> None:
        if message is None:
            message = f"Unknown event `{func_name}`"

        super().__init__(message)
