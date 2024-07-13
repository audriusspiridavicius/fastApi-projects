from typing import List
from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    
    model_config = ConfigDict(from_attributes=True)
    
    name:str | None = ""
    email:str
    


class UserProducts(User):
    products:List["Product"]
    
from .product import Product
User.model_rebuild()