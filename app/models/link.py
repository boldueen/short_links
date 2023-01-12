from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy import Sequence

from . import Base

class Link(Base):
    __tablename__ = "link"
    link_id = Column(Integer, Sequence("seq_link"), primary_key=True, nullable=False)
    long_link = Column(String, nullable=False)
    short_link = Column(String, index=True, unique=True)
    redirect_users = Column(Integer, default=0)

