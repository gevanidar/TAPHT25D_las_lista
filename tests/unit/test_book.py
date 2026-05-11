"""Tests for the BookStore."""

import pytest

from reading_list.book import Book

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
    """Test generated id is ok."""

    assert book.book_id == "kung_kobra-min_lilla_bok_om_python"
