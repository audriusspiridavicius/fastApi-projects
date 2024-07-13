from sqlalchemy.orm import Session
from .models.user import User
from .utils import fill_db_with_users
def get_user(user_id:int, db:Session):

    existing_user = db.query(User).filter_by(id=user_id).first()
    
    if existing_user:
        return existing_user
    else:
        return None

    
def get_users(db:Session):
    fill_db_with_users(db)
    return db.query(User).all()