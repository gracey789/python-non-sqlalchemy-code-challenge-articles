class Article:
    all = []

    def _init_(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string and between 5-50 characters")
        self._title = title

        self._author = author
        self._magazine = magazine
        self._author.articles().append(self)
        self._magazine.articles().append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise ValueError("Author must be of type Author")
        self._author = author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be of type Magazine")
        self._magazine = magazine


class Author:
    def _init_(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    def _init_(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = name
        
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = category
        
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author = article.author
            if author not in author_counts:
                author_counts[author] = 0
            author_counts[author] += 1

        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        return contributing_authors if contributing_authors else None



author1 = Author("John Lee")


magazine1 = Magazine("Tech Monthly", "Technology")
magazine2 = Magazine("M News", "News")


article1 = Article(author1, magazine2, "Plus News")
print (article1.magazine.name)
print (article1.author.name)
Magazine_by_1 = author1.magazines()
magazine_names = [magazine.name for magazine in Magazine_by_1]

print(magazine_names)


# This verifies the relationship
print(f"Author1: {author1.name}, Articles: {[article.title for article in author1.articles()]}")
print(f"Magazine2: {magazine2.name}, Articles: {[article.title for article in magazine2.articles()]}")
