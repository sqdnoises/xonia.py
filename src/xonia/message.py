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

from .asset import Asset
from .user import User

__all__ = [
    "Message"
]

class Message(object):
    """
    Class that represents a message
    """
    def __init__(
        self,
        id: int,
        content: str | None = None,
        attachment: Asset | None = None,
        created_at: str | None = None,
        updated_at: str | None = None,
        author: User | None = None
    ) -> None:
        self.content = content
        self.attachment = attachment
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.author = author
    
    def __str__(self) -> str:
        return self.content