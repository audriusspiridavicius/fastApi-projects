from fastapi import FastAPI, Query, Body
from pydantic import BaseModel
from fastApi_user_guide.models.user import User
from typing import Annotated
from fastApi_user_guide.models.product import Product
from fastApi_user_guide.main import app


# app = FastAPI()

# Base.metadata.create_all(bind=engine)



@app.get("/")
def index():
    return {"page": "index"}

@app.get("/index/{parameter}")
def index2(parameter:int):
    return {"index2":{"param":parameter}}


@app.get("/index3")
def index3(parameter:int | None = 0):
    return {"index2":{"param":parameter}}


@app.post("/users")
def get_users(user:Annotated[User,Body()] = ...):
    return user


@app.post("/users/query_list")
def get_users(user:Annotated[User,Body()] = ..., q:Annotated[list[str] | None,Query(min_length=5)] = None):
    return {"user":user, "query":q}


class Result(BaseModel):
    user:User
    products:list[Product]
@app.post("/products")
def products(
    user:Annotated[User | None,Body(examples=[{
        "username": "johnwick",
        "first_name": "john",
        "last_name": "wick",
        "email": "Johnwick@gmail.com"
        }])] = None, 
    product:Annotated[list[Product] | None, Body(examples=[{
        "name": "computer",
        "price": 123.45,
        "price2": 1.99,
        "brand": "opel",
        "description": "very bad car"
        }])] = None)-> Result :
    return {"products":product, "user":user}





if __name__ == "__main__":
    pass