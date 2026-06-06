from behave import when, then

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
    locator.get_by_text(page)
    assert locator is not None


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
    assert context.reading_list_page.contains_favorite_book(book), f'{book} was not found in the list'


@then("ska jag inte se boken i listan")
def step_impl(context):
    book = get_first_book(context)
    assert not context.reading_list_page.contains_favorite_book(book), f'{book} was found in the list'


@then("ska jag se en bok med {title} i favoritlistan")
def step_impl(context, title):
    assert context.reading_list_page.contains_favorite_book(book), f'book with title: "{title}" was not found in the list'
