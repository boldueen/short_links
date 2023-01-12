from fastapi import APIRouter

from .v1 import api_v1

root_router = APIRouter()

root_router.include_router(api_v1.api_v1_router, prefix='/api')

