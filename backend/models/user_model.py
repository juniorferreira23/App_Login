from config import DB_USER, DB_PASSWORD, DATABASE, DB_HOST
from sqlalchemy import Column, Integer, String, Boolean
from core.database import Database

db = Database(DB_USER, DB_PASSWORD, DATABASE, DB_HOST)
db.connect()
db.base()

class Users(db.Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    disable = Column(Boolean, nullable=False, default=False)
    
db.Base.metadata.create_all(db.engine)