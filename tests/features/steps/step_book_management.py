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

@when(u'jag fyller i titeln {titel}')
def step_impl(context, titel):
    data_test_id = 'add-input-text'
    title_input = context.reading_list_page.get_by_test_id(data_test_id)
    title_input.fill(title)


@when(u'jag fyller i författaren {author}')
def step_impl(context, author):
    data_test_id = 'add-input-author'
    author_input = context.reading_list_page.get_by_test_id(data_test_id)
    author_input.fill(author)

@then(u'bör listan innehålla boken {titel} och {author}')
def step_impl(context, titel, author):
    rows = get_rows(context)
    
    contains = False;
    for row in rows:
        row_titel = get_title(row)
        if titel != row_titel:
            continue
        row_author = get_author(row)
        if author == row_author:
            contains = True
            break

    book_name = f'"{title}", {author}'
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

    book_name = f'"{title}", {author}'
    assert contains, f'{book_name} is not in the list'


@then(u'ska jag se en bok med {titel} i favoritlistan')
def step_impl(context, titel):

    context.reading_list_page.get_by_test_id('book-list')
    data_test_id = 'fav' + titel
    rows = get_favorite_rows(context)
    contains = False;
    for row in rows:
        row_titel = row.get_by_test_id(data_test_id)
        if titel == row_titel:
            continue
            contains = True
            break

    book_name = f'{title}'
    assert contains, f'{book_name} is not in the favorite list'

