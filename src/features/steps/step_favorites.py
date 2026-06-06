from behave import when, then

from playwright.api import expect


def get_first_book(context):
    # TODO: Extract this to the ReadingListPage
    initial_state = context.initial_state
    books = initial_state.get_books()
    if books and len(books) > 0:
        return books[0]
    return None


@given("att jag står på sidan {page}")
def step_impl(context, page):
    # TODO: Extract this to the ReadingListPage
    locator = context.reading_list_page.page.locator("main")
    assert locator is not None
    expect(locator).to_be_visible()
    locator.get_by_text(page)
    assert locator is not None
    expect(locator).to_be_visible()


# TODO: This is actually not the row, this is the heart of the first row.
@when("jag markerar en rad")
def step_impl(context):
    # TODO: Extract this to the ReadingListPage
    book = get_first_book(context)
    locator = context.reading_list_page.get_by_test_id(book)
    locator.hover()


@when("jag klickar på hjärtat")
def step_impl(context):
    book = get_first_book(context)
    locator = context.reading_list_page.toggle_mark_favorite(book)


@then("ska boken favoritmarkeras")
def step_impl(context):
    book = get_first_book(context)
    is_favorite = context.reading_list_page.is_favorite_marked(book)
    assert is_favorite


@then("ska boken avfavoritmarkeras")
def step_impl(context):
    book = get_first_book(context)
    is_favorite = context.reading_list_page.is_favorite_marked(book)
    assert not is_favorite


@then("ska jag se boken i listan")
def step_impl(context):
    book = get_first_book(context)
    # TODO: Fix this quick hack
    fav_book = "fav" + book[4:]
    context.reading_list_page.contains_row_with_test_id(fav_book)


@then("ska jag inte se boken i listan")
def step_impl(context):
    book = get_first_book(context)
    # TODO: Fix this quick hack
    fav_book = "fav" + book[4:]
    assert context.reading_list_page.contains_row_with_test_id(fav_book)


@then("ska jag se en bok med {title} i favoritlistan")
def step_impl(context, title):
    # TODO: Extract this to the ReadingListPage
    assert context.reading_list_page.contains_row_with_test_id(title)
