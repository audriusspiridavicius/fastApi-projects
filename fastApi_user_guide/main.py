from fastapi import FastAPI
from fastApi_user_guide.database.db import Base, engine
from fastApi_user_guide.database.models.product import Product
app = FastAPI()

Base.metadata.create_all(bind=engine)

