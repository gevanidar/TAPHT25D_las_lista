from behave import when, then

from behave.api.pending_step import StepNotImplementedError

def get_first_book(context):
    books = context.initial_state.get_books()
    if books and len(books) > 0:
        return books[0]
    return None

@given(u'att jag står på sidan {page}')
def step_impl(context, page):
    locator = context.reading_list_page.page.locator('main')
    assert locator is not None
    locator.get_by_text(page)
    assert locator is not None

@when(u'jag markerar en rad')
def step_impl(context):
    book = get_first_book(context)
    locator = context.reading_list_page.get_by_test_id(book)
    locator.hover()

@when('jag klickar på hjärtat')
def step_impl(context):
    book = get_first_book(contest)
    locator = context.reading_list_page.get_by_test_id(book)
    locator.click()

@then(u'ska boken favoritmarkeras')
def step_impl(context):
    book = get_first_book(contest)
    locator = context.reading_list_page.is_favorite_marked(book)
