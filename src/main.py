"""Main program."""

import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("https://tap-ht25-testverktyg.github.io/exam/")

    expect(page).to_have_title(re.compile("Läslistan"))


if __name__ == "__main__":
    print("This is the main function")
