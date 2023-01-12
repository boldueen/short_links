from fastapi import APIRouter

error_router = APIRouter()

@error_router.get('/')
def error():
    return {
        "message":"error"
    }