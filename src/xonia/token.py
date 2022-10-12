__all__ = [
    "Token"
]

class Token(object):
    """
    Represents a xonia-auth cookie token
    """
    def __init__(self, cookie_dict: dict):
        for value in cookie_dict:
            setattr(self, value, cookie_dict[value])
    
    def __str__(self) -> str:
        return self.xonia_auth