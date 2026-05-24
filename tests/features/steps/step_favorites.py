from behave import when, then

from behave.api.pending_step import StepNotImplementedError

def get_first_book(context):
    initial_state = context.initial_state
    books = initial_state.get_books()
    #print(f"{context=}\n{initial_state=}\n{books=}")
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
    book = get_first_book(context)
    locator = context.reading_list_page.toggle_mark_favorite(book)

@then(u'ska boken favoritmarkeras')
def step_impl(context):
    book = get_first_book(context)
    is_favorite = context.reading_list_page.is_favorite_marked(book)
    assert is_favorite

@then(u'ska boken avfavoritmarkeras')
def step_impl(context):
    book = get_first_book(context)
    is_favorite = context.reading_list_page.is_favorite_marked(book)
    assert not is_favorite

@then(u'ska jag se boken i listan')
def step_impl(context):
    book = get_first_book(context)
    # TODO: Fix this quick hack
    fav_book = 'fav' + book[4:]
    context.reading_list_page.contains_favorite(fav_book)

@then(u'ska jag inte se boken i listan')
def step_impl(context):
    book = get_first_book(context)
    # TODO: Fix this quick hack
    fav_book = 'fav' + book[4:]
    assert context.reading_list_page.contains_favorite(fav_book)

@then(u'ska en raden visuellt förtydligas')
def step_impl(context):
		raise StepNotImplementedError(u'Then ska en raden visuellt förtydligas')
