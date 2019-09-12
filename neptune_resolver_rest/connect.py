import json

import aiohttp

from .resolver import Resolver


class Connection:

    def __init__(self,
                 loop,
                 base_url,
                 username=None,
                 password=None):
        self.loop = loop
        self.base_url = base_url
        self.username = username
        self.password = password
        self._session = aiohttp.ClientSession()
        self.Resolver = Resolver(self)


    async def init_connection(self) -> None:
        pass
