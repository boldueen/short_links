import dotenv 
import os

dotenv.dotenv_path = ("../.env")
dotenv.load_dotenv(dotenv.find_dotenv())

APP_PORT=os.environ.get("APP_PORT")
POSTGRES_URL=os.environ.get("POSTGRES_URL")
POSTGRES_URL_MIGRATIONS=os.environ.get("POSTGRES_URL_MIGRATIONS")

ALLOWED_SYMBOLS_IN_LINK='ABCDEFGHKLMNOPQRSTUVWXYZ'
FORBIDDEN_SYMBOLS='/.,:;"\'@#$%&*()_-+=!'
