class Article:
    def __init__(self, author, magazine, title):
       
        if not isinstance(title, str):
            raise ValueError("Title must be of type str.")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters.")

        self._title = title

       
        if not hasattr(author, 'id') or not isinstance(author.id, int):
            raise ValueError("Author must have a valid integer ID.")

        
        if not hasattr(magazine, 'id') or not isinstance(magazine.id, int):
            raise ValueError("Magazine must have a valid integer ID.")

        self._author = author
        self._magazine = magazine

        self.add_to_database()

    def __repr__(self):
        return f"<Article {self._title}>"

    @property
    def title(self):
        
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Title cannot be changed after the article is instantiated.")

    @property
    def author(self):
        
        return self._fetch_author()

    @property
    def magazine(self):
       
        return self._fetch_magazine()

    def add_to_database(self):
        
        print(f"Article '{self._title}' by Author ID {self._author.id} for Magazine ID {self._magazine.id} has been added to the database.")

    def _fetch_author(self):
       
        return self._author

    def _fetch_magazine(self):
        
        return self._magazine


class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Magazine:
    def __init__(self, id, name):
        self.id = id
        self.name = name


author = Author(1, "John Doe")
magazine = Magazine(1, "Tech Monthly")


article = Article(author, magazine, "The Future of AI")

print(article)
print("Title:", article.title)
print("Author:", article.author.name)
print("Magazine:", article.magazine.name)