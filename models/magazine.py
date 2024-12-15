class Magazine:
    def __init__(self, id, name, category):
       
        if not isinstance(id, int):
            raise ValueError("ID must be of type int.")

        
        if not isinstance(name, str):
            raise ValueError("Name must be of type str.")
        if not (2 <= len(name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters.")

        
        if not isinstance(category, str):
            raise ValueError("Category must be of type str.")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters.")

        self._id = id
        self._name = name
        self._category = category

        
        self.add_to_database()

    def __repr__(self):
        return f'<Magazine {self._name}>'

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be of type str.")
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be of type str.")
        if len(value) == 0:
            raise ValueError("Category must be longer than 0 characters.")
        self._category = value

    def add_to_database(self):
       
        print(f"Magazine '{self._name}' in category '{self._category}' has been added to the database.")

    def articles(self):
       
        return [
            article for article in Article._all_articles if article.magazine.id == self._id
        ]

    def contributors(self):
      
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
       
        articles = self.articles()
        return [article.title for article in articles] if articles else None

    def contributing_authors(self):
        
        authors = self.contributors()
        if not authors:
            return None

        author_article_count = {
            author: len([article for article in self.articles() if article.author == author])
            for author in authors
        }

        return [
            author for author, count in author_article_count.items() if count > 2
        ] or None


class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Article:
    _all_articles = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article._all_articles.append(self)


author1 = Author(1, "John Doe")
author2 = Author(2, "Jane Smith")
magazine1 = Magazine(1, "Tech Weekly", "Technology")
magazine2 = Magazine(2, "Health Digest", "Health")


article1 = Article(author1, magazine1, "The Rise of AI")
article2 = Article(author1, magazine1, "Quantum Computing")
article3 = Article(author1, magazine1, "AI in Healthcare")
article4 = Article(author2, magazine1, "Future of Medicine")
article5 = Article(author2, magazine2, "Healthy Living Tips")

print(magazine1.articles())
print(magazine1.contributors())
print(magazine1.article_titles())
print(magazine1.contributing_authors())