"""Tests for the BookStore."""

import pytest

from reading_list.book import Book
from reading_list.book_store import BookStore
from reading_list.favorite_books import FavoriteBooks


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
    return FavoriteBooks()


@pytest.fixture(name="book_store")
def setup_book_store(favorite_books):
    """BookStore fixture."""
    return BookStore(favorite_books)


@pytest.mark.integration
def test_toggle_book_favorite_to_favorite(book_store, book):
    """Test the toggle_favorite method.
    After toggle the book should be marked as a favorite book."""
    # Act
    book_store.add_book(book.author, book.title)

    book_store.toggle_favorite(book.book_id)

    # Assert
    # Verify that the book is now favorite
    assert book.book_id in book_store.favorite_books.book_ids


@pytest.mark.integration
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


@pytest.mark.integration
def test_toggle_favorite_for_book_not_present_in_store(book_store, book):
    """Test the toggle_favorite when book_id is not present in book_store."""
    # Act
    book_store.toggle_favorite(book.book_id)

    # Assert
    # Verify that the book is no longe favorite
    assert book.book_id not in book_store.favorite_books.book_ids
