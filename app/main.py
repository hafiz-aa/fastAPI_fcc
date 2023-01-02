from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user, auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Connect to postgres
while True:

    try:
        conn = psycopg2.connect(host='localhost', database='fastAPI', user='postgres',
                                password='130894', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connected")
        break
    except Exception as error:
        print("Datacase connection failded")
        print("Error: ", error)
        time.sleep(2)

# Data

my_posts = [
    {"title": "ini title", "content": "ini content", "id": 1},
    {"title": "itu title", "content": "itu content", "id": 2}
]

# Find a post


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

# Find index post


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

# Home


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "Hello Guys"}
