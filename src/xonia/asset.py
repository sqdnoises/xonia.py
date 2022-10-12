__all__ = [
    "Asset"
]

class Asset(object):
    """
    Represents an asset
    """
    def __init__(
        self,
        url: str | None = None,
        filename: str | None = None,
        filetype: str | None = None
    ) -> None:
        self.filename = filename
        self.filetype = filetype
        self.url = url
    
    def __str__(self):
        return self.url