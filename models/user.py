from sqlalchemy import Column, Integer, String, TIMESTAMP
from database import Base
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    password = Column(String)
    role = Column(String(20), default="user")
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())