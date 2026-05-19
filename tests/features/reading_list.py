import re
from playwright.sync_api import Page, expect

from unittest.mock import MagicMock
import pytest

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.button_catalog = page.get_by_test_id('catalog')
        self.button_favorites = page.get_by_test_id('favorites')
        self.button_add_book = page.get_by_test_id('add-book')
        self.button_statistics = page.get_by_test_id('statistics')

    def navigate_home(self):
        self.page.goto("https://tap-ht25-testverktyg.github.io/exam/")

    def click_catalog(self):
        self.button_catalog.click()

    def click_add_button(self):
        self.button_add_button.click()

    def click_favorites(self):
        self.button_favorites.click()

    def click_statistcs(self):
        self.button_statistcs.click()


