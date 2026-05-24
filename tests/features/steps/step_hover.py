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
    #book = get_first_book(context)
    #locator = context.reading_list_page.get_by_test_id(book)

    page = context.reading_list_page.page
    row = page.locator('div.catalog .book')
    first = row.nth(0)
    first_original_color = first.evaluate("el => window.getComputedStyle(el).backgroundColor")
    context.first_original_color = first_original_color
    first.hover()
    page.wait_for_timeout(500)
    first_color = first.evaluate("el => window.getComputedStyle(el).backgroundColor")
    context.first_color = first_color

@then(u'ska en raden visuellt förtydligas')
def step_impl(context):
    color = context.first_color
    print(f"{color=}")
    original_color = context.first_original_color
    print(f"{original_color=}")

    assert color != "rgb(0, 0, 0, 0)", "Incorrect selection of element which has hover effect."
    assert color != original_color, "The hover had no effect on color"
    assert color == "rgb(229, 190, 149)", "Incorrect hover color for first row"
    
