from fastapi import APIRouter
from .auth import router as authRouter

apis = APIRouter()

apis.include_router(authRouter)

__all__ = ['routers']