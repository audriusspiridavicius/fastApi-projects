from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
SQLALCHEMY_DATABASE_URI = "sqlite:///./products.db"

engine = create_engine(SQLALCHEMY_DATABASE_URI)


SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()


def get_database():
    db = SessionLocal()

    try:
        yield db
    except Exception as e:
        print(e)
        raise Exception(f"something went wrong with database connnection! Please try again or contact support team.{e}")
    finally:
        db.close()