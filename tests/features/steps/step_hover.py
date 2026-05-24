from behave import when, then

from behave.api.pending_step import StepNotImplementedError

def get_first_book(context):
    initial_state = context.initial_state
    books = initial_state.get_books()
    #print(f"{context=}\n{initial_state=}\n{books=}")
    if books and len(books) > 0:
        return books[0]
    return None

@when(u'jag hovrar över en rad')
def step_impl(context):
    book = get_first_book(context)
    locator = context.reading_list_page.get_by_test_id(book)
    locator.hover()

@then(u'ska en raden visuellt förtydligas')
def step_impl(context):
    row = context.reading_list_page.page.locator('div.catalog .book')
    first = row.first 

    color = first.evaluate("el => window.getComputedStyle(el).backgroundColor")
    print("{row=}\n{first=}\n{color=}")

    assert color != "rgba(0, 0, 0, 0)", "Incorrect selection of element which has hover effect."
    
