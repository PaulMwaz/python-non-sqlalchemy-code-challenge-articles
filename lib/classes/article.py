class Article:
    instances = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author class.")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine class.")
        
        self._author = author
        self._magazine = magazine
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

    def __repr__(self):
        return f"Article(title={self._title}, author={self._author}, magazine={self._magazine})"
