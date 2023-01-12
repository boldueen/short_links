from pydantic import BaseModel
from typing import Optional


class CreateShortLink(BaseModel):
    long_link: str
    short_link: Optional[str]