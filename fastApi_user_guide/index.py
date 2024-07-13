from fastapi import Body, Depends, Path
from fastapi.security import OAuth2PasswordBearer
from fastApi_user_guide.models.user import User, UserProducts
from typing import Annotated, List
from fastApi_user_guide.models.product import Product, Product2, UpdateProduct, DeleteProduct
from .main import app
from .database.db import get_database
import fastApi_user_guide.database as database
from .database.models.product import Product as DProduct
from .database.models.user import User as DUser
from sqlalchemy.orm import Session
from .functions import login_user, verify_token, generate_token
from passlib.context import CryptContext
from .models.token import Token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
password_context = CryptContext(schemes=["bcrypt"])

db = Depends(get_database)


logged_user = Annotated[User, Depends(login_user)]
 

@app.get("/users", response_model=List[UserProducts])
def get_users(user:Annotated[User, Depends(login_user)], db:Session = db ):

        users = database.get_users(db)
        users=[UserProducts.model_validate(user) for user in users]
    
        return users


@app.put("/users")
def get_users(user:Annotated[User,Body()] = ..., db:Session = db):
    
    existing_user = db.query(DUser).filter_by(email=user.email).first()
    if existing_user:
        existing_user.name = user.name
        db.commit()
        db.refresh(existing_user)
        return user
    return {"message":"such user was not found","user":user}


@app.post("/users")
def get_users(user:Annotated[User,Body()] = ...):
    return user

@app.get("/users/{user_id}", response_model=UserProducts)
def get_user(user_id:Annotated[int, Path(title="user id")], db:Session = db, ):
   
    user = database.get_user(user_id,db)
    return user


@app.get("/")
@app.get("/products", response_model=list[Product])
def products(token:Annotated[OAuth2PasswordBearer, Depends(oauth2_scheme)],db:Session = db):
    
    user = verify_token(token)
    products = db.query(DProduct).all()

    return list(products)


#add multiple products at once
@app.post("/products", response_model=list[Product2])
def add_products(products:Annotated[list[Product] | None, Body(
    examples=[{
        "name": "computer",
        "price": 123.45,
        "price2": 1.99,
        "brand": "opel",
        "description": "very bad car"
        }]
    )] = None, db:Session = db):
    
    prods = []
    for product in products:
        db_prod = DProduct(**product.model_dump())
        prods.append(db_prod)

    db.add_all(prods)
    db.commit()
    
    return prods


#add single product
@app.post("/product", response_model=Product2)
def add_product(product:Annotated[Product, Body()] = ..., db:Session = db):
    product.model_validate
    new_product = DProduct(**product.model_dump())
    
    db.add(new_product)
    db.commit()
    
    return new_product


# update product
@app.put("/product")
def update_product(product:UpdateProduct = ..., db:Session = db):
    existing_product =  db.query(DProduct).filter_by(id=product.id).first()
    
    if existing_product:
        props = product.model_dump()
        for key, value in props.items():
            if hasattr(existing_product, key) and value:
                setattr(existing_product,key,value)

        db.commit()
        db.refresh(existing_product)
        return existing_product
    else:
        return {"message": "product not found"}


@app.delete("/product")    
def delete_product(product:DeleteProduct = ..., db:Session = db):
    
    existing_product = db.query(DProduct).filter_by(id=product.id).first()
    
    if existing_product:
        db.delete(existing_product)
        db.commit()
        return {"message": "product deleted successfully"}
    else:
        return {"message": "product not found"}




@app.post("/login", response_model=Token)
def login(user:Annotated[User,Depends(login_user)]) -> Token:
    
    token = generate_token(user.model_dump(),1)
    
    return token