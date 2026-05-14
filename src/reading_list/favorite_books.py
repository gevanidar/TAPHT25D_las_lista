"""A representation of my favorite books."""

from .book import Book

class FavoriteBooks:
    """A list of my favorite books."""

    def __init__(self):
        """Todo."""
        self.book_ids = []

    def add(self, book: Book):
        """Add a book_id to to the favorite books list."""
        book_id = book.book_id
        if book_id not in self.book_ids:
            self.book_ids.append(book_id)

    def remove(self, book):
        """Remove a book_id present in the favorite books list."""
        book_id = book.book_id
        if book_id in self.book_ids:
            self.book_ids.remove(book_id)
