import sqlite3

def create_tables():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    # Authors Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)

    # Magazines Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL
    )
    """)

    # Articles Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        author_id INTEGER NOT NULL,
        magazine_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        FOREIGN KEY(author_id) REFERENCES authors(id),
        FOREIGN KEY(magazine_id) REFERENCES magazines(id)
    )
    """)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_tables()
