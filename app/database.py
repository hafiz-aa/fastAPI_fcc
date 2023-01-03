from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Connect to postgres
# while True:

#     try:
#         conn = psycopg2.connect(host='localhost', database='fastAPI', user='postgres',
#                                 password='130894', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connected")
#         break
#     except Exception as error:
#         print("Datacase connection failded")
#         print("Error: ", error)
#         time.sleep(2)