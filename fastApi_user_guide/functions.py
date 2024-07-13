from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from .database.models.user import User as DUser
from .database.db import get_database
from .models.user import User
from sqlalchemy.orm import Session

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
        