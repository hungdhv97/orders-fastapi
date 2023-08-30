from typing import Any

from app.clients.grab.grab_client import GrabClient


class MenuService:
    def __init__(self, grab_client: GrabClient):
        self.grab_client = grab_client

    async def get_menus_grab(self, merchant_id: str) -> Any:
        response = await self.grab_client.get_menus(merchant_id)
        return response.json()
