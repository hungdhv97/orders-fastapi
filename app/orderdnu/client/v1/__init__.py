from fastapi import APIRouter

from app.orderdnu.client.v1.client_router import router as client_router

router = APIRouter(prefix="/api/v1/client", tags=["Clients (Grab, ...)"])

router.include_router(client_router)
