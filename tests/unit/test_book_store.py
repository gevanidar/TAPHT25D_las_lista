"""Tests for the BookStore."""

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

def test_add_book_to_book_store(book):
    """Test the function add_book to BookStore.
    The book should be added to the empty bookstore.
    Increasing the number of books in the bookstore from 0 to 1.
    The book stored in the bookstore should be the same book that was added."""
    # Act
    book_store = BookStore()
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
