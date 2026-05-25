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
def step_impl(context, page):
    raise StepNotImplementedError(u'jag fyller i titeln <titel>')


@given(u'jag fyller i författaren <författare>')
def step_impl(context, page):
    raise StepNotImplementedError(u'jag fyller i författaren <författare>')


@given(u'bör listan innehålla boken <titel> och <författare>')
def step_impl(context, page):
    raise StepNotImplementedError(u'bör listan innehålla boken <titel> och <författare>')


@given(u'bör listan innehålla boken <titel2> och <författare2> sist')
def step_impl(context, page):
    raise StepNotImplementedError(u'bör listan innehålla boken <titel2> och <författare2> sist')


@given(u'ska jag se en bok med <titel> och <författare> i listan')
def step_impl(context, page):
    raise StepNotImplementedError(u'ska jag se en bok med <titel> och <författare> i listan')

