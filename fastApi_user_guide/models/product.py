from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Annotated, Optional
from fastApi_user_guide.database.db import SessionLocal


db = SessionLocal()

class Product(BaseModel):
    
    model_config = ConfigDict(from_attributes=True)
    
    name:str
    price:float = Field(default=0)
    price2:Annotated[float | None,Field(gt=0)] = 1
    quantity:int | None = 0 
    brand:Annotated[str | None, Field()] = "undefined"
    description:str = Field(default="undefined")
    size: Optional[float] = None
    user:'User'
    
    # @field_validator('name')
    # def validate_unique(cls, value):
    #     exists = db.query(DbProduct).filter_by(name=value).first()
    #     if exists:
    #         raise ValueError('name already exists')
    #     return value
    

class UpdateProduct(Product):
    id:int



class DeleteProduct(BaseModel):
    id:int
    
       
class Product2(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    name:str
    price:float = Field(default=0)
    price2:Annotated[float | None,Field(gt=0)] = 1
    quantity:int | None = 0 
    brand:Annotated[str | None, Field()] = "undefined"
    
from .user import User
# Product.model_rebuild()
