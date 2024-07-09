from pydantic import BaseModel

class User(BaseModel):
    first_name:str | None = ""
    last_name:str | None = ""
    username:str
    email:str
    