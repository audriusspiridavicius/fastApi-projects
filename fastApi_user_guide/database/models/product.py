from sqlalchemy import Column, Integer, String
from fastApi_user_guide.database.db import Base


# Base.metadata


class Product(Base):
    
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)
    price2 = Column(Integer)
    quantity = Column(Integer)
    brand = Column(String)
    