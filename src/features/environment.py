from playwright.sync_api import sync_playwright

from reading_list_page import ReadingListPage
from initial_state import InitialState


# Runs before any scenarios
def before_all(context):
    # Start Playwright and the browser - close it in after_all
    context.playwright = sync_playwright().start()
    context.browser_type = context.playwright.chromium
    context.browser = context.browser_type.launch(headless=True)


# Runs at the start of each scenario
def before_scenario(context, scenario):
    # The scenario fixture is created from a feature file, we don't typically need it for anything.
    # Open a new page, to prevent cookies to leak between tests. Set default timeout to something appropriate. Close the page in after_scenario.
    page = context.browser.new_page()
    reading_list_page = ReadingListPage(page)
    context.reading_list_page = reading_list_page
    context.initial_state = InitialState()


# Runs directly after each scenario - clean up to avoid memory leaks
def after_scenario(context, scenario):
    page = context.reading_list_page.page
    if page:
        page.close()


# Runs after all scenarios have finished - clean up
def after_all(context):
    browser = context.browser
    if browser:
        browser.close()
    pw = context.playwright
    if pw:
        pw.stop()
