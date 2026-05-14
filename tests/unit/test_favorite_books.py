"""Tests for the BookStore."""

import pytest

from reading_list.book import Book
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

@pytest.mark.unit
def test_add_favorite_book(book: Book):
    """Test adding a book to favorite books."""
    favorite_books = FavoriteBooks()

    # Act
    favorite_books.add(book)

    book_ids = favorite_books.book_ids
    count = len(book_ids)

    # Assert
    assert count == 1

    favorite_book_id = book_ids[0]

    assert favorite_book_id == book.book_id

@pytest.mark.unit
def test_add_favorite_book_to_favorite_list_containing_another_book(book):
    """Test adding a book to favorite books list already containing other books."""
    favorite_books = FavoriteBooks()
    # Arrange
    old_book = Book("Story Teller", "An old tale")
    favorite_books.add(old_book)

    # Act
    favorite_books.add(book)

    book_ids = favorite_books.book_ids
    count = len(book_ids)

    # Assert
    assert count == 2

    old_favorite_book_id = book_ids[0]
    assert old_favorite_book_id == old_book.book_id

    favorite_book_id = book_ids[1]
    assert favorite_book_id == book.book_id


@pytest.mark.unit
def test_add_favorite_book_already_in_favorite_books_list(book):
    """Test adding a book that is already a favorite book to favorite books."""
    favorite_books = FavoriteBooks()

    # Arrange
    favorite_books.add(book)

    book_ids = favorite_books.book_ids
    first_count = len(book_ids)

    # Act
    favorite_books.add(book)

    book_ids = favorite_books.book_ids
    second_count = len(book_ids)

    # Assert
    assert second_count == 1
    assert first_count == second_count

    favorite_book_id = book_ids[0]

    assert favorite_book_id == book.book_id

@pytest.mark.unit
def test_remove_favorite_book(book):
    """Test removing a book to favorite books."""
    favorite_books = FavoriteBooks()

    # Arrange
    favorite_books.add(book)

    # Act
    favorite_books.remove(book)

    # Assert
    assert book.book_id not in favorite_books.book_ids

    book_ids = favorite_books.book_ids
    count = len(book_ids)
    assert count == 0

@pytest.mark.unit
def test_remove_favorite_book_from_empty_list(book):
    """Test removing a book to favorite books."""
    favorite_books = FavoriteBooks()

    # Act
    favorite_books.remove(book)

    # Assert
    assert book.book_id not in favorite_books.book_ids

    book_ids = favorite_books.book_ids
    count = len(book_ids)
    assert count == 0

@pytest.mark.unit
def test_remove_present_favorite_after_adding_new_favorite_removes_old_favorite_and_keeps_new(book):
    """Test addind a new book the favorite books when another book is already present in list.
    Then remove the old favorite book."""
    favorite_books = FavoriteBooks()
    # Arrange
    old_book = Book("Story Teller", "An old tale")
    favorite_books.add(old_book)

    # Act
    favorite_books.add(book)
    favorite_books.remove(old_book)

    book_ids = favorite_books.book_ids
    count = len(book_ids)

    # Assert
    assert count == 1

    assert old_book.book_id not in book_ids
    assert book.book_id in book_ids
