import json
import aiohttp
from datetime import datetime
from .config import API_URL, USER_DATE_FORMAT, COOKIE_EXPIRE_FORMAT
from .errors import CredentialsError, CredentialsHTTPError
from .token import Token
from .user import User
from .asset import Asset

__all__ = [
    "Credentials"
]

class Credentials(object):
    """
    Class that contains credentials
    """
    def __init__(
        self,
        email: str,
        password: str
    ) -> None:
        self.email = email
        self.password = password
        self.token = None
        self.user = None
    
    def __str__(self) -> str:
        return self.email if self.user == None else str(self.user)

    async def get_token(self) -> str:
        """
        Get token with set credentials

        Returns:
            str: token string
        """
        async with aiohttp.ClientSession() as session:
            async with session.post(
                API_URL/"account"/"login",
                json = {
                    "email": self.email,
                    "password": self.password,
                }
            ) as response:
                if response.status == 200:
                    token_cookie = str(response.cookies.get("xonia-auth"))
                    user = json.loads(await response.text())
                    self.user = User(
                        id = int(user["id"]),
                        created_at = datetime.strptime(user["createdAt"], USER_DATE_FORMAT),
                        updated_at = datetime.strptime(user["updatedAt"], USER_DATE_FORMAT),
                        name = user["username"],
                        email = user["email"],
                        avatar = Asset(url = user["image"]),
                        is_online = user["isOnline"]
                    )
                elif response.status == 401:
                    raise CredentialsError
                else:
                    raise CredentialsHTTPError(response=response)
        cookie = {}
        for x in token_cookie.replace("Set-Cookie: ", "").split("; "):
            x = x.split("=") if "=" in x else [x, True]
            cookie.update({x[0]: x[1]})
        token = {}
        for x in cookie:
            token.update({x.replace("-", "_"): cookie[x]})
        token.update({
            "expires": datetime.strptime(token["expires"], COOKIE_EXPIRE_FORMAT)
        })
        self.token = Token(token)
        return self.token