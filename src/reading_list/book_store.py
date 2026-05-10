"""Representation of a book store that can contain books."""

from .book import Book

class BookStore:
    """A book store contains a list over available books."""

    def __init__(self, favorite_books=[]):
        """Initiate an empty bookstore."""
        self.books = []
        self.favorite_books = favorite_books

    # addBook, naming convention is snake case for python
    def add_book(self, author, title):
        """Add a book based on the author and title."""
        # TODO: implement

    def get_books(self):
        """Get a list over the books currently in the book store."""
        return self.books

    # toggleFavorite, naming convention is snake case for python
    def toggle_favorite(self, book_id):
        """Add a book based on the author and title."""
        # TODO: implement
