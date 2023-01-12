from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.core.db import get_session

from fastapi import HTTPException, status

from app.models import Link
from app.schemas.link import CreateShortLink

from app.core.config import FORBIDDEN_SYMBOLS

from app.services.link.shortener import get_short_link


forbidden_symbols = list(FORBIDDEN_SYMBOLS)

def create_link(create_link:CreateShortLink):
    session = get_session()
    
    short_link = ''
    if create_link.short_link is None or create_link.short_link == "string":
        rows: int = session.query(Link).count()
        short_link=get_short_link(int(rows))
    else:
        if set(forbidden_symbols) & set(create_link.short_link):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'symbols like {FORBIDDEN_SYMBOLS} are not allowed')
        short_link = create_link.short_link

    new_short_link = Link(long_link=create_link.long_link, short_link=short_link)
    session.add(new_short_link)
    try:    
        session.commit()
    except IntegrityError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='link with this short_link already exists')

    return {
        "long_link":create_link.long_link,
        "short_link":short_link
    }



def get_link_by_short_link(short_link:str) -> str:
    session = get_session()
    link = session.query(Link).filter(Link.short_link==short_link).first()
    if link is None:
        return '/api/v1/error'
    link.redirect_users +=1
    session.commit()
    return link.long_link

