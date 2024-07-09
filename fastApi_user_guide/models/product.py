from pydantic import BaseModel, Field
from typing import Annotated, Optional
from fastapi import Body

class Product(BaseModel):
    name:str
    price:float = Field(default=0)
    price2:Annotated[float | None,Field(gt=0)] = 1
    quantity:Annotated[int | None,Body()] = 0 
    brand:Annotated[str | None, Field(min_length=5, validate_default=True)] = "undefined"
    description:str = Field(default="undefined")
    size: Optional[float] = None