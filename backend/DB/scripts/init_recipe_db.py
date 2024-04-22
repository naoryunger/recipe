import sqlite3


def create_recipe_db(db_path):
    # Connect to SQLite database (create it if it doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create table for recipes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recipes (
            recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
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
            review_id INTEGER PRIMARY KEY AUTOINCREMENT,
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
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            surname TEXT,
            password TEXT,
            reviews_num INTEGER
        )
    ''')

    # Commit changes and close connection
    conn.commit()
    conn.close()


def main():
    create_recipe_db(r"..\recipe_database.db")


if __name__ == '__main__':
    main()
