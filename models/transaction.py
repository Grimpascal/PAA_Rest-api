from sqlalchemy import Column, Integer, DECIMAL, ForeignKey, String
from sqlalchemy.orm import relationship
from database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    total_price = Column(DECIMAL)
    status = Column(String(20))

    user = relationship("User")