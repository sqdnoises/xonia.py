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
import time
import aiohttp
import asyncio
from datetime import datetime
from .config import API_URL, USER_DATE_FORMAT
from .credentials import Credentials
from .user import User
from .asset import Asset
from .errors import CredentialsError, CredentialsHTTPError

__all__ = [
    "Client",
]

class Client:
    """Represents a Xonia client"""

    def __init__(
        self,
        credentials: Credentials
    ) -> None:
        self.credentials = credentials
        self.user = self.credentials.user
        self.latency = 0
        self._events = {}
        self._info = {}
        self.loop = asyncio.new_event_loop()
        self._is_ready = False
    
    def __str__(self) -> str:
        return self.user
    
    async def get_user(self) -> User:
        """
        Get user with set credentials

        Returns:
            User: user
        """
        try:
            await self.credentials.get_token()
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    API_URL/"account",
                    headers = {
                        "Cookie": f"xonia-auth={self.credentials.token.xonia_auth}"
                    }
                ) as response:
                    if response.status == 200:
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
                        return self.user
                    elif response.status == 401:
                        raise CredentialsError
                    else:
                        raise CredentialsHTTPError(response=response)
        except Exception as e:
            self.fire_event("on_error", error=e)

    def event(self, func) -> None:
        """
        Event handler
        """
        name = func.__name__
        if name == "before_ready" or name == "on_ready" or name == "on_disconnect" or name == "on_error":
            self._events.update({
                name: func
            })
        return func

    def fire_event(self, event_name: str, **kwargs) -> None:
        """
        Fire an event
        """
        if event_name in self._events:
            self.loop.create_task(self._events[event_name](**kwargs))
    
    def edit_info(self, v1, v2) -> None:
        """
        Edit info
        """
        if v1 in self._events:
            self._info.update({
                v1: v2
            })
    
    async def check_connectivity(self):
        """
        Check connectivity
        """
        while True:
            try:
                async with aiohttp.ClientSession() as session:
                    t1 = time.monotonic()
                    await session.get(API_URL/"ping")
                    t2 = time.monotonic()
            except Exception as e:
                self.fire_event("on_error", error=e)
                if self._is_ready:
                    self.fire_event("on_disconnect")
                    self._is_ready = False
            else:
                if not self._is_ready:
                    self.fire_event("on_ready")
                    self._is_ready = True
                self.latency = t2 - t1
            await asyncio.sleep(5)

    def start(self) -> None:
        """
        Start the client
        """
        self.loop.run_until_complete(self.get_user())

        self.loop.run_until_complete(self.check_connectivity())