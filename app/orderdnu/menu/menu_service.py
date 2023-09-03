from app.clients.grab.grab_client import GrabClient
from app.orderdnu.menu.menu_model import MenuResponse


class MenuService:
    def __init__(self, grab_client: GrabClient):
        self.grab_client = grab_client

    async def get_menus_grab(self, merchant_id: str) -> MenuResponse:
        grab_menu_response = await self.grab_client.get_menus(merchant_id)
        return MenuResponse(**dict(grab_menu_response))
