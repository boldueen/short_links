from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from app.schemas.link import CreateShortLink

from app.services.crud.link import get_link_by_short_link, create_link


link_router=APIRouter(prefix="/link")


@link_router.get('/{short_link}', status_code=307)
def get_link(short_link:str):
    link = get_link_by_short_link(short_link=short_link)
    return RedirectResponse(link, status_code=307)


@link_router.post('/')
def create(link:CreateShortLink):
    return create_link(link)

