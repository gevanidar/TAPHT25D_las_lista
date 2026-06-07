"""Representation of a book."""


class Book:
    """Book has an author, title and a book id."""

    def __init__(self, author, title):
        """Create a representation of a book from an author and title."""
        self.author = author
        self.title = title
        self.book_id = self.__generate_book_id()

    def __generate_book_id(self):
        """Generate a simple id for the book."""
        return (
            self.author.replace(" ", "_").lower()
            + "-"
            + self.title.replace(" ", "_").lower()
        )

    def get_author(self):
        """Return the author of the book."""
        return self.author

    def get_title(self):
        """Return the title of the book."""
        return self.title
