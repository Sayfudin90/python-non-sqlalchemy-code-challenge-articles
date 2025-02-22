# many_to_many.py
class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        self._title = title
        self._author = author
        self._magazine = magazine
        Article.all.append(self)
        magazine.article.append(self)
        author._articles.append(self)
        
    @property
    def title(self):
        return self._title
        
    @title.setter
    def title(self, value):
        pass
        
    @property
    def author(self):
        return self._author
        
    @author.setter
    def author(self, value):
        self._author = value
        
    @property
    def magazine(self):
        return self._magazine
        
    @magazine.setter
    def magazine(self, value):
        self._magazine = value

class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        pass

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))

class Magazine:
    _all = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self.article = []
        Magazine._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return self.article

    def contributors(self):
        return list(set(article.author for article in self.article))

    def article_titles(self):
        if not self.article:
            return None
        return [article.title for article in self.article]

    def contributing_authors(self):
        author_count = {}
        for article in self.article:
            author_count[article.author] = author_count.get(article.author, 0) + 1
        
        prolific = [author for author, count in author_count.items() if count > 2]
        return prolific if prolific else None

    @classmethod
    def top_publisher(cls):
        if not cls._all or not any(m.article for m in cls._all):
            return None
        return max(cls._all, key=lambda m: len(m.article))