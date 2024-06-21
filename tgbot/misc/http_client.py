import asyncio

from aiohttp import ClientSession
from icecream import ic


class HTTPClient:
    def __init__(self, base_url: str, external_api_url: str):
        self.base_url = base_url
        self.external_api_url = external_api_url
        self._session = None

    async def _get_session(self):
        if self._session is None:
            self._session = ClientSession()
        return self._session

    async def close(self):
        if self._session is not None:
            await self._session.close()


class CMCHTTPClient(HTTPClient):
    async def get_user(self, chat_id):
        session = await self._get_session()
        try:
            async with asyncio.timeout(10):  # Set a timeout for the request
                async with session.get(self.base_url + f"/user/{chat_id}") as resp:
                    if resp.status == 200:
                        return await resp.json()
                    return None
        except asyncio.TimeoutError:
            print("Request timed out")
            return None

    # @alru_cache
    async def add_user(self, chat_id, full_name, username, language):
        data = {
            "chat_id": chat_id,
            "full_name": full_name,
            "username": username,
            "language": language,
        }
        session = await self._get_session()
        try:
            async with asyncio.timeout(10):  # Set a timeout for the request
                async with session.post(self.base_url + "/user/", json=data) as resp:
                    return await resp.json()
        except asyncio.TimeoutError:
            print("Request timed out")
            return None
