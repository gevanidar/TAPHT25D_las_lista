from behave import when, then

from behave.api.pending_step import StepNotImplementedError

def get_rows(context):
    page = context.reading_list_page.page
    return page.locator('div.catalog .book')

def get_favorite_rows(context):
    page = context.reading_list_page.page
    return page.locator('div.favorites .book')

def get_row(context, n):
    rows = get_rows(context)

    if len(rows) < n:
        raise StepNotImplementedError("No way to reach row `n`")
    row = rows.nth(n)
    return row

@when(u'jag fyller i titeln ')
def step_impl(context):
    data_test_id = 'add-input-title'
    context.reading_list_page.fill_field_with_test_id(data_test_id, "")
    context.title = ""

@when(u'jag fyller i författaren ')
def step_impl(context):
    data_test_id = 'add-input-author'
    context.reading_list_page.fill_field_with_test_id(data_test_id, "")
    context.author = ""

@when(u'jag fyller i titeln {titel}')
def step_impl(context, titel):
    data_test_id = 'add-input-title'
    context.reading_list_page.fill_field_with_test_id(data_test_id, titel)
    context.title = titel

@when(u'jag fyller i författaren {author}')
def step_impl(context, author):
    data_test_id = 'add-input-author'
    context.reading_list_page.fill_field_with_test_id(data_test_id, author)
    context.author = author

@then(u'bör jag inte kunna trycka på knappen {test_id}')
def step_impl(context, test_id):
    button = context.reading_list_page.get_by_test_id(test_id)

    title = context.title
    author = context.author

    error_message = ""
    if not title or len(title) == 0:
        error_message = "title is empty"
    if not author or len(author) == 0:
        if len(error_message) == 0:
            error_message += " and "
        error_message += "author is empty"
    error_message += "."

    print(f"{button=}\n{button.is_disabled()=}\n{error_message=}\n{title=}\n{author=}")

    assert button.is_disabled(), f"Can submit even when {error_message}"

@then(u'bör listan innehålla boken {titel} och {author}')
def step_impl(context, titel, author):
    rows = get_rows(context)
    
    contains = False;
    for n in range(rows.count()):
        row = rows.nth(n)
        row_titel = get_title(row)
        if titel != row_titel:
            continue
        row_author = get_author(row)
        if author == row_author:
            contains = True
            break

    book_name = f'"{titel}", {author}'
    assert contains, f'{book_name} is not in the list'


@then(u'bör listans sista bok vara {titel2} och {author2}')
def step_impl(context, titel2, author2):
    rows = get_rows(context)
    last_row = rows[-1]
    contains = True
    row_titel = get_title(row)
    if titel != row_titel:
        contains = False
    row_author = get_author(row)
    if author != row_author:
        contains = False

    book_name = f'"{titel}", {author}'
    assert contains, f'{book_name} is not in the list'


@then(u'ska jag se en bok med {titel} i favoritlistan')
def step_impl(context, titel):

    context.reading_list_page.get_by_test_id('book-list')
    data_test_id = 'fav' + titel
    rows = get_favorite_rows(context)
    contains = False;
    for n in range(rows.count()):
        row = rows.nth(n)
        row_titel = row.get_by_test_id(data_test_id)
        print(f'{titel=}')
        if titel == row_titel:
            contains = True
            break

    book_name = f'{titel}'
    assert contains, f'{book_name} is not in the favorite list'

		

