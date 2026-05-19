
import re
from playwright.sync_api import Page, expect

from unittest.mock import MagicMock
import pytest

# Arrange
@pytest.fixture(name="homepage")
def setup_homepage():
    return "https://tap-ht25-testverktyg.github.io/exam/"

@pytest.fixture(name="catalog")
def setup_catalog():
    return "Katalog"

@pytest.fixture(name="book_snakes_on_a_plane")
def setup_book_snakes_on_a_plane():
    return "star-Ormar på ett plan: En Python-berättelse"

@pytest.mark.e2e
def test_has_title(page: Page, homepage):
    page.goto(homepage)

    expect(page).to_have_title(re.compile("Läslistan"))

@pytest.mark.e2e
def test_catalog_button_visible(page: Page, homepage, catalog):
    page.goto(homepage)

    expect(page.get_by_test_id('catalog')).to_be_visible()

@pytest.mark.e2e
def test_goto_catalog_should_show_catalog(page: Page, homepage, catalog, book_snakes_on_a_plane):
    page.goto(homepage)

    button = page.get_by_test_id('catalog').click()

    expect(page.get_by_test_id(book_snakes_on_a_plane)).to_be_visible()
