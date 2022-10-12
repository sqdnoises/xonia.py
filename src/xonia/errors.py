"""
The MIT License (MIT)

Copyright (c) 2022-present SqdNoises

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

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