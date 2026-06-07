from behave import when, then


def get_first_book(context):
    initial_state = context.initial_state
    books = initial_state.get_books()
    if books and len(books) > 0:
        return books[0]
    return None


@given("att jag står på sidan {page}")
def step_impl(context, page):
    locator = context.reading_list_page.page.locator("main")
    assert locator is not None
    locator.get_by_text(page)
    assert locator is not None


@when("jag markerar en rad")
def step_impl(context):
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
    test_id = context.reading_list_page.convert_to_fav_test_id(book)
    assert context.reading_list_page.contains_favorite_book_with_test_id(
        test_id
    ), f"{test_id} was not found in the list"


@then("ska jag inte se boken i listan")
def step_impl(context):
    book = get_first_book(context)
    test_id = context.reading_list_page.convert_to_fav_test_id(book)
    contains = context.reading_list_page.contains_favorite_book_with_test_id(test_id)
    assert not contains, f"{test_id} was found in the list"


@then("ska jag se en bok med {title} i favoritlistan")
def step_impl(context, title):
    assert context.reading_list_page.contains_favorite_book_title(
        title
    ), f'book with title: "{title}" was not found in the list'
