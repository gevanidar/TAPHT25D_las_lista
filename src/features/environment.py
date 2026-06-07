"""Environment setup for behave."""
from playwright.sync_api import sync_playwright

from reading_list_page import ReadingListPage
from initial_state import InitialState


def before_all(context):
    """Set the context for all scenarios."""
    context.playwright = sync_playwright().start()
    context.browser_type = context.playwright.chromium
    context.browser = context.browser_type.launch(headless=True)


def before_scenario(context, scenario):
    """Set scenario specific context."""
    page = context.browser.new_page()
    reading_list_page = ReadingListPage(page)
    context.reading_list_page = reading_list_page
    context.initial_state = InitialState()


def after_scenario(context, scenario):
    """Reset between scenarios."""
    page = context.reading_list_page.page
    if page:
        page.close()


def after_all(context):
    """Reset the browser after finishing up the scenarios."""
    browser = context.browser
    if browser:
        browser.close()
    pw = context.playwright
    if pw:
        pw.stop()
