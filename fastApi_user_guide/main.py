from fastapi import FastAPI
from .database.db import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

