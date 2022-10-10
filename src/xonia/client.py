import aiohttp

from . import config
from .credentials import Credentials
from .models import Message
from .errors import NotConnectedError

__all__ = [
    "Client",
]

class Client:
    """Represents a Xonia client"""

    def __init__(self) -> None:
        self._session = aiohttp.ClientSession()
        self._is_connected = False
    
    async def connect(self, email: str, password: str) -> None:
        self._token = await self.get_token(email, password)
        self._is_connected = True

    async def get_token(self, email: str, password: str) -> str:
        """Get the token using :code:`_creds`."""

        if not self._

        res = await self._session.post(
            config.API_URL / "account" / "login",
            json={
                "email": email,
                "password": password,
            },
        )

        return res.headers["Set-Cookie"].split(";")[0]
