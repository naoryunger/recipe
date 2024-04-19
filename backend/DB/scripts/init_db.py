import sqlite3

# Connect to SQLite database (create it if it doesn't exist)
conn = sqlite3.connect(r"..\recipe_database.db")
cursor = conn.cursor()

# Create table for recipes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS recipes (
        recipe_id INTEGER PRIMARY KEY,
        name TEXT,
        owner_id INTEGER,
        first_review_id INTEGER,
        second_review_id INTEGER,
        third_review_id INTEGER,
        recipe_content TEXT,
        recipe_category TEXT
    )
''')

# Create table for reviews
cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews (
        review_id INTEGER PRIMARY KEY,
        recipe_id INTEGER,
        content TEXT,
        rating INTEGER,
        user TEXT,
        FOREIGN KEY(recipe_id) REFERENCES recipes(recipe_id)
    )
''')

# Create table for users
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        name TEXT,
        surname TEXT,
        reviews_num INTEGER
    )
''')

# Commit changes and close connection
conn.commit()
conn.close()
