__all__ = [
    "CredentialsError",
    "CredentialsHTTPError",
    "UnknownEvent"
]


class XoniaException(Exception):
    """Base exception class for all exceptions."""
    pass


class CredentialsError(XoniaException):
    """An exception that is raised when no credentials are given"""

    def __init__(self, message: str | None = None, response = None) -> None:
        if message == None:
            message = "Invalid Credentials! Please check if your email or password are correct."
        self.response = response
        super().__init__(message)

class CredentialsHTTPError(XoniaException):
    """An exception that is raised when an error occurs while connecting to the API"""

    def __init__(self, message: str | None = None, response = None) -> None:
        if message == None:
            message = f"Response did not return status code 200 or 401, instead returned code {response.status}."
        self.response = response
        super().__init__(message)

class UnknownEvent(XoniaException):
    """An exception that is raised when the decorator is used in an unknown event"""

    def __init__(self, func_name: str, message: str | None = None) -> None:
        if message == None:
            message = f"Unknown event `{func_name}`"
        super().__init__(message)