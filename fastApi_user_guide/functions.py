from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from .database.models.user import User as DUser
from .database.db import get_database
from .models.user import User
from sqlalchemy.orm import Session
import datetime
import jwt
from datetime import timedelta, timezone
from .models.token import Token

ACCESS_TOKEN_EXPIRE_MINUTES = 30
ALGORITHM = "HS256"
SECRET_KEY = "525d8be904ade7e7ab48245f1da0702dafea5ab960ba7312ba52dd031c199d92"


security = HTTPBasic()

def login_user(credentials:Annotated[HTTPBasicCredentials, Depends(security)], db:Session = Depends(get_database)):
    

    logged_user = db.query(DUser).filter_by(email=credentials.username, password=credentials.password).first()
    if logged_user:
        return User.model_validate(logged_user)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

def generate_token(data, expires:timedelta = ACCESS_TOKEN_EXPIRE_MINUTES) -> Token:
    
    expire = datetime.datetime.now(timezone.utc) + timedelta(minutes=expires)
    refresh_expire = datetime.datetime.now(timezone.utc) + timedelta(minutes=expires + 10)
    
    token_data = {"data":data, "exp":expire}
    refresh_token_data = {"data":data,"refresh_token":True, "exp":refresh_expire}
    
    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    refresh = jwt.encode(refresh_token_data, SECRET_KEY, algorithm=ALGORITHM)
    
    return Token(access_token=token, refresh_token=refresh)

