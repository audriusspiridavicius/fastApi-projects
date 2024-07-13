import random
from .db import get_database
from fastapi import Depends
from sqlalchemy.orm import Session
from .models.user import User
from .models.product import Product

def fill_db_with_users(db:Session):
    
    db_has_users = db.query(User).first()
    if not db_has_users:
        users = [ User(name=f"username{index}", email=f"testuseremail{index}@email.com", password=f"pass{index}") for index in range(1,11)]
        db.add_all(users)
        db.commit()
    fill_db_with_products(db)
    
def fill_db_with_products(db:Session):
    
    db_has_products = db.query(Product).first()
    if not db_has_products:
        user_ids = db.query(User.id).all()
        user_ids = [id[0] for id in user_ids]
    
       
        products = [Product(
            name=f"product_test_name_{index}", 
            description=f"product{index} description",
            price=random.randint(1, 1000),
            price2=random.randint(1, 1000),
            quantity=random.randint(1, 100),
            brand="unknown",
            size=random.randint(1,11),
            user_id = random.choice(user_ids)
            ) for index in range(1,11)]
        db.add_all(products)
        db.commit()
