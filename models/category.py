from sqlalchemy import Column, Integer, String, TIMESTAMP
from database import Base
from sqlalchemy.sql import func

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    nama_kategori = Column(String(100))
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())