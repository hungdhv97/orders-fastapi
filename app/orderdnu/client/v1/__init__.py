from fastapi import APIRouter

from app.orderdnu.client.v1.grab_router import router as grab_router

router = APIRouter(prefix="/api/v1/client", tags=["Clients (Grab, ...)"])

router.include_router(grab_router)
