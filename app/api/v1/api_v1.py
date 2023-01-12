from fastapi import APIRouter
from .endpoints import link, error

api_v1_router = APIRouter(prefix='/v1')

api_v1_router.include_router(link.link_router)
api_v1_router.include_router(error.error_router, prefix='/error')
