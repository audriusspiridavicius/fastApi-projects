

from sqlalchemy.orm import Mapped, relationship, mapped_column
from ..db import Base


class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email:Mapped[str] = mapped_column(nullable=False)
    password:Mapped[str] = mapped_column(nullable=False)
    
    products:Mapped[list["Product"]] = relationship("Product",back_populates="user")




