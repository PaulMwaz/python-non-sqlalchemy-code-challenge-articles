class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or not category:
            raise ValueError("Category must be a non-empty string.")
        
        self._name = name
        self._category = category

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

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        author_counts = {author: authors.count(author) for author in authors}
        return [author for author, count in author_counts.items() if count > 2]

    def __repr__(self):
        return f"Magazine(name={self._name}, category={self._category})"
