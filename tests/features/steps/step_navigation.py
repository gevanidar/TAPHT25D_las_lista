from behave import when, then

from behave.api.pending_step import StepNotImplementedError

@given(u'att jag är på hemsidan')
def step_impl(context):
    pass

@when(u'jag trycker på knappen {button}')
def step_impl(context, button):
    locator = context.reading_list_page.click_button_with_test_id(button)

@then('bör jag se en lista med {count:d} böcker')
def step_impl(context, count):
    books = context.reading_list_page.get_initial_books()
    c = 0
    for book in books:
        locator = context.reading_list_page.get_by_test_id(book)
        if locator:
            c += 1
    assert c == count

@then(u'bör jag se en div med {div_class}')
def step_impl(context, div_class):
    locator = context.reading_list_page.page.locator('main')
    assert locator is not None
    locator.get_by_text(div_class)
    assert locator is not None
    
@then('bör jag se en label {label}')
def step_impl(context, label):
    locator = context.reading_list_page.get_by_label(label)
    assert locator is not None


@then('bör jag se en text {text}')
def step_impl(context, text):
    locator = context.reading_list_page.get_by_text(text)
    assert locator is not None
