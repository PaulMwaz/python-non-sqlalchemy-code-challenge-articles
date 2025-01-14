class Author:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.instances if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = [article.magazine.category for article in self.articles()]
        return list(set(categories)) if categories else None


class Article:
    instances = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.instances.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value


class Magazine:
    instances = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        Magazine.instances.append(self)

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def articles(self):
        return [article for article in Article.instances if article.magazine == self]

    def contributors(self):
        authors = [article.author for article in self.articles()]
        return list(set(authors)) if authors else None

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    @classmethod
    def top_publisher(cls):
        if not cls.instances:
            return None
        return max(cls.instances, key=lambda magazine: len(magazine.articles()), default=None)
