from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import POSTGRES_URL

engine = create_engine(POSTGRES_URL, echo=False)
Session = sessionmaker(bind=engine)


def get_session():
    return Session()

