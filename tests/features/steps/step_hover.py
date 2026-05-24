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
    row = context.reading_list_page.page.locator('div.catalog .book')
    first = row.first 
    color = first.evaluate("el => window.getComputedStyle(el).backgroundColor")
    context.color = color

@then(u'ska en raden visuellt förtydligas')
def step_impl(context):
    color = context.color

    assert color != "rgba(0, 0, 0, 0)", "Incorrect selection of element which has hover effect."
    assert color != "rgba(229, 190, 149)", "Incorrect hover color for first row"
    
    assert True == False
   # --cat1: rgb(222, 219, 207);
   # --cat2: rgb(201, 198, 187); 
   # --cat3: rgb(244, 207, 168);
   # --cat4: rgb(229, 190, 149);
