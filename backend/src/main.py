from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import sqlite3
from sqlite3 import Connection, connect
from contextlib import contextmanager
from typing import Generator

# FastAPI app instance
app = FastAPI()


# SQLite connection pool
@contextmanager
def get_db() -> Generator[sqlite3.Connection, None, None]:
    conn = sqlite3.connect(r"..\DB\recipe_database.db")
    try:
        yield conn
    finally:
        conn.close()


# Pydantic models for request and response bodies
class Recipe(BaseModel):
    name: str
    owner_id: int
    recipe_content: str
    recipe_category: str


class Review(BaseModel):
    recipe_id: int
    content: str
    rating: int
    user: str


class User(BaseModel):
    name: str
    surname: str
    password: str


# Endpoint to create a new recipe
@app.post("/recipes/")
def create_recipe(recipe: Recipe):
    with get_db() as db:
        cursor = db.cursor()
        query = """
        INSERT INTO recipes (name, owner_id, first_review_id, second_review_id, third_review_id, recipe_content, recipe_category)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, (
            recipe.name, recipe.owner_id, None, None, None,
            recipe.recipe_content, recipe.recipe_category))
        db.commit()
    return {"message": "Recipe created successfully"}


# Endpoint to get all recipes
@app.get("/recipes/")
def get_all_recipes():
    with get_db() as db:
        cursor = db.cursor()
        query = "SELECT * FROM recipes"
        cursor.execute(query)
        recipes = cursor.fetchall()
    return recipes


# Endpoint to create a new review for a recipe
@app.post("/reviews/")
def create_review(review: Review):
    with get_db() as db:
        cursor = db.cursor()
        query = """
        INSERT INTO reviews (recipe_id, content, rating, user)
        VALUES (?, ?, ?, ?)
        """
        cursor.execute(query, (review.recipe_id, review.content, review.rating, review.user))
        db.commit()
    return {"message": "Review created successfully"}


# Endpoint to get all reviews for a recipe
@app.get("/reviews/{recipe_id}")
def get_reviews_for_recipe(recipe_id: int):
    with get_db() as db:
        cursor = db.cursor()
        query = "SELECT * FROM reviews WHERE recipe_id = ?"
        cursor.execute(query, (recipe_id,))
        reviews = cursor.fetchall()
    return reviews


# Endpoint to create a new user
@app.post("/users/")
def create_user(user: User):
    import pdb;pdb.set_trace()
    with get_db() as db:
        cursor = db.cursor()
        query = """
        INSERT INTO users (name, surname, password, reviews_num)
        VALUES (?, ?, ?, ?)
        """
        cursor.execute(query, (user.name, user.surname, user.password, 0))
        db.commit()
    return {"message": "User created successfully"}
