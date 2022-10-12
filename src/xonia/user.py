from .asset import Asset

__all__ = [
    "User"
]

class User(object):
    """
    Class that represents a user
    """
    def __init__(
        self,
        name: str | None = None,
        id: int | None = None,
        created_at: str | None = None,
        is_online: bool = False,
        is_friend: bool = False,
        avatar: Asset | None = None,
        updated_at: str | None = None,
        email: str | None = None,
        color: int | None = None,
        colour: int | None = None
    ) -> None:
        self.name = name
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_online = is_online
        self.id = id
        self.avatar = avatar
        self.is_friend = is_friend
        self.color = color
        self.colour = colour
    
    def __str__(self) -> str:
        return self.name