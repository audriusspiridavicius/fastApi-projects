from sqlalchemy import Column, Integer, String, Float, UniqueConstraint, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from ..db import Base

class Product(Base):
    
    __tablename__ = "products"
    __table_args__ = (UniqueConstraint("name", name="name_unique_1" ),)
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    price = Column(Integer)
    price2 = Column(Integer)
    quantity = Column(Integer)
    brand = Column(String)
    description = Column(String)
    size = Column(Float)
    
    user_id:Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
    user:Mapped["User"] = relationship("User",back_populates="products")
    
    
    

