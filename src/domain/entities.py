from sqlalchemy import Column, Integer, String, Float
from core.database import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)

class Sale(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer)
    quantity = Column(Integer)