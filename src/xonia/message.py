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