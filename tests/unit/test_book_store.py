"""Tests for the BookStore."""

from unittest.mock import MagicMock
import pytest

from reading_list.book import Book
from reading_list.book_store import BookStore


# Arrange
@pytest.fixture(name="author")
def setup_author():
    """Author fixture."""
    return "Kung Kobra"


@pytest.fixture(name="title")
def setup_title():
    """Title fixture."""
    return "Min lilla bok om python"


@pytest.fixture(name="book")
def setup_book(author, title):
    """Book fixture."""
    return Book(author, title)


@pytest.fixture(name="favorite_books")
def setup_favorite_books():
    """FavoriteBooks mock fixture."""
    favorite_books = MagicMock()

    favorite_books.book_ids = []

    def mock_add(book: Book):
        book_id = book.book_id
        if book_id not in favorite_books.book_ids:
            favorite_books.book_ids.append(book_id)

    favorite_books.add.side_effect = mock_add

    def mock_remove(book: Book):
        book_id = book.book_id
        if book_id in favorite_books.book_ids:
            favorite_books.book_ids.remove(book_id)

    favorite_books.remove.side_effect = mock_remove

    return favorite_books


@pytest.fixture(name="book_store")
def setup_book_store(favorite_books):
    """BookStore fixture."""
    return BookStore(favorite_books)


@pytest.mark.unit
def test_add_book_to_book_store(book_store, book):
    """Test the function add_book to BookStore.
    The book should be added to the empty bookstore.
    Increasing the number of books in the bookstore from 0 to 1.
    The book stored in the bookstore should be the same book that was added."""
    # Act
    book_store.add_book(book.author, book.title)

    books = book_store.get_books()
    count = len(books)

    # Assert
    # Verify book store now has 1 book.
    assert count == 1

    book_in_store = books[0]
    # Verify that the book stored in the BookStore is the same one that was stored.
    assert book_in_store is not None
    assert book_in_store.author == book.author
    assert book_in_store.title == book.title
    assert book_in_store.book_id == book.book_id


@pytest.mark.unit
def test_toggle_book_favorite_to_favorite(book_store, book):
    """Test the toggle_favorite method.
    After toggle the book should be marked as a favorite book."""
    # Act
    book_store.add_book(book.author, book.title)

    book_store.toggle_favorite(book.book_id)

    # Assert
    # Verify that the book is now favorite
    assert book.book_id in book_store.favorite_books.book_ids


@pytest.mark.unit
def test_toggle_book_favorite_twice_book_no_longer_a_favorite(book_store, book):
    """Test the toggle_favorite method.
    After toggling a favorite book it should no longer be a favorite."""
    # Act
    book_store.add_book(book.author, book.title)

    book_store.toggle_favorite(book.book_id)
    book_store.toggle_favorite(book.book_id)

    # Assert
    # Verify that the book is no longe favorite
    assert book.book_id not in book_store.favorite_books.book_ids
