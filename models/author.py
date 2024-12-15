class Author:
    def __init__(self, id, name):
       
        if not isinstance(id, int):
            raise ValueError("ID must be of type int.")
        self._id = id

        if not isinstance(name, str):
            raise ValueError("Name must be of type str.")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters.")
        
        self._name = name

        
        self.add_to_database()

    def __repr__(self):
        return f"<Author {self._name}>"

    @property
    def id(self):
        
        return self._id

    @id.setter
    def id(self, value):
        raise AttributeError("ID cannot be changed once set.")

    @property
    def name(self):
       
        return self._name

    @name.setter
    def name(self, value):
        
        raise AttributeError("Name cannot be changed after the author is instantiated.")

    def add_to_database(self):
        
        print(f"Author {self._name} with ID {self._id} has been added to the database.")

    def articles(self, db_connection):
        
        query = """
        SELECT articles.*
        FROM articles
        INNER JOIN authors ON authors.id = articles.author_id
        WHERE authors.id = ?;
        """
        cursor = db_connection.cursor()
        cursor.execute(query, (self._id,))
        return cursor.fetchall()

    def magazines(self, db_connection):
       
        query = """
        SELECT magazines.*
        FROM magazines
        INNER JOIN articles ON articles.magazine_id = magazines.id
        INNER JOIN authors ON authors.id = articles.author_id
        WHERE authors.id = ?;
        """
        cursor = db_connection.cursor()
        cursor.execute(query, (self._id,))
        return cursor.fetchall()


import sqlite3


db = sqlite3.connect(':memory:')
try:
    
    db.execute("CREATE TABLE authors (id INTEGER PRIMARY KEY, name TEXT);")
    db.execute("CREATE TABLE articles (id INTEGER PRIMARY KEY, title TEXT, author_id INTEGER, magazine_id INTEGER);")
    db.execute("CREATE TABLE magazines (id INTEGER PRIMARY KEY, name TEXT);")
    
  
    db.execute("INSERT INTO authors (id, name) VALUES (1, 'John Doe');")
    db.execute("INSERT INTO magazines (id, name) VALUES (1, 'Tech Monthly');")
    db.execute("INSERT INTO articles (id, title, author_id, magazine_id) VALUES (1, 'AI Revolution', 1, 1);")
    db.execute("INSERT INTO articles (id, title, author_id, magazine_id) VALUES (2, 'Quantum Computing', 1, 1);")

    
    author = Author(1, "John Doe")
    
   
    articles = author.articles(db)
    magazines = author.magazines(db)
    
    print("Articles:", articles)
    print("Magazines:", magazines)

finally:
    db.close()