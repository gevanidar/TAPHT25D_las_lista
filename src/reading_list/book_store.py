"""Representation of a book store that can contain books."""

from .book import Book
from .favorite_books import FavoriteBooks

class BookStore:
    """A book store contains a list over available books."""

    def __init__(self, favorite_books: FavoriteBooks):
        """Initiate an empty bookstore."""
        self.books = []
        print(f"Creating {favorite_books=} as {type(favorite_books)} and {len(favorite_books.books_id)}")
        self.favorite_books = favorite_books

    # addBook, naming convention is snake case for python
    def add_book(self, author, title):
        """Add a book based on the author and title."""
        book = Book(author, title)
        self.books.append(book)

    def get_books(self):
        """Get a list over the books currently in the book store."""
        return self.books

    def _get_favorite_books(self):
        """Get a list over the the favorite books object."""
        return self.favorite_books

    # toggleFavorite, naming convention is snake case for python
    def toggle_favorite(self, book_id):
        """Add a book based on the author and title."""

        print(f"toggle {self.favorite_books=} as {type(self.favorite_books)} and {len(self.favorite_books.books_id)}")
        if book_id not in self.favorite_books.book_ids:
            self.favorite_books.add(book_id)
        else:
            self.favorite_books.remove(book_id)
        print(f"toggled {self.favorite_books=} as {type(self.favorite_books)} and {len(self.favorite_books.books_id)}")

