from sqlalchemy import Column, Integer, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from database import Base

class TransactionDetail(Base):
    __tablename__ = "transaction_details"

    id = Column(Integer, primary_key=True)
    transaction_id = Column(Integer, ForeignKey("transactions.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    price = Column(DECIMAL)

    transaction = relationship("Transaction")
    product = relationship("Product")