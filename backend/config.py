import os
from dotenv import load_dotenv

load_dotenv()

USEDB = os.getenv('USERDB')
PASSWORD = os.getenv('PASSWORD')
DATABASE = os.getenv('DATABASE')

SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret')
ALGORITHM = os.getenv('ALGORITHM', 'HS256')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', 30))
