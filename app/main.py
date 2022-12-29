from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Schema


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


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


@app.get("/")
def root():
    return {"message": "Hello Guys"}


@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    return {"status": "success"}

    # Get all posts


@app.get("/posts")
def get_posts():
    cursor.execute(""" SELECT * FROM posts """)
    posts = cursor.fetchall()
    print(posts)
    return {"data": posts}

# Post a post


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
                   (post.title, post.content, post.published))
    new_post = cursor.fetchone()

    # Commit the change

    conn.commit()

    return {"data": new_post}


# GET a post
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    cursor.execute("""SELECT * FROM posts WHERE id = (%s)""", (str(id),))
    post = cursor.fetchone()

    conn.commit()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return {"post_detail": post}


# DELETE a post
@ app.delete("/posts/{id}")
def delete_post(id: int):
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * """,
                   (str(id),))
    deleted_post = cursor.fetchone()

    conn.commit()

    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    return Response(status_code=status.HTTP_204_NO_CONTENT)


# Update a post
@ app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """,
                   (post.title, post.content, post.published, (str(id),)))

    updated_post = cursor.fetchone()
    conn.commit()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    return {"data": updated_post}
