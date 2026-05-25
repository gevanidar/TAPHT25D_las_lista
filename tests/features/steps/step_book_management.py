from behave import when, then

from behave.api.pending_step import StepNotImplementedError

def get_row(context, n):
    page = context.reading_list_page.page
    rows = page.locator('div.catalog .book')

    if len(rows) < n:
        raise StepNotImplementedError("No way to reach row `n`")
    row = rows.nth(n)
    return row

@given(u'jag fyller i titeln <titel>')
def step_impl(context, titel):
    data_test_id = 'add-input-text'
    title_input = context.reading_list_page.get_by_test_id(data_test_id)
    title_input.fill(title)


@given(u'jag fyller i författaren <author>')
def step_impl(context, author):
    data_test_id = 'add-input-author'
    author_input = context.reading_list_page.get_by_test_id(data_test_id)
    author_input.fill(author)

@given(u'bör listan innehålla boken <titel> och <author>')
def step_impl(context, titel, author):
    raise StepNotImplementedError(u'bör listan innehålla boken <titel> och <author>')


@given(u'bör listan innehålla boken <titel2> och <author2> sist')
def step_impl(context, titel2, author2):
    raise StepNotImplementedError(u'bör listan innehålla boken <titel2> och <author2> sist')


@given(u'ska jag se en bok med <titel> och <author> i listan')
def step_impl(context, titel, author):
    raise StepNotImplementedError(u'ska jag se en bok med <titel> och <author> i listan')

