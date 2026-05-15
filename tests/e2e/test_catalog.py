
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

def test_has_title(page: Page, homepage):
    page.goto(homepage)

    expect(page).to_have_title(re.compile("Läslistan"))

def test_goto_catalog_should_show_catalog(page: Page, homepage, catalog):
    page.goto(homepage)

    page.get_by_role("link", name="Katalog").click()

    expect(page.get_by_role("div", name="catalog")).to_be_visible()
