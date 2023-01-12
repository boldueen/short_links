from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData

metadata = MetaData()

Base = declarative_base(metadata=metadata)

from .link import Link

__all__ = ["metadata", "Link", "User"]