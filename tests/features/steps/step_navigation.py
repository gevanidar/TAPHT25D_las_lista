from behave import when, then

from behave.api.pending_step import StepNotImplementedError

@given(u'att jag är på hemsidan')
def step_impl(context):
    pass

@when(u'jag trycker på knappen {button}')
def step_impl(context, button):
    locator = context.page.get_by_test_id(button)
    if not locator.is_disabled():
        locator.click()

@then('bör jag se en lista med {count:d} böcker')
def step_impl(context, count):
    books = context.page.get_by_role('div', name='book').all()
    print(f"{books=}")
    assert len(books) == count


@then(u'bör jag se en div med {div_class}')
def step_impl(context, div_class):
    locator = context.page.get_by_role('div', name=div_class)
    print(f"{locator=}")
    assert locator.to_be_visible()
    
@then('bör jag se label {label}')
def step_impl(context, label):
    raise StepNotImplementedError(u'Then bör jag se en text {label}')

@then('bör jag se text {text}')
def step_impl(context, text):
    raise StepNotImplementedError("bör jag se text {text}")
