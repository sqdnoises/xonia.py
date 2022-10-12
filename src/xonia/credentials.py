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