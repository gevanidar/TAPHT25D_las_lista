from behave import when, then

from behave.api.pending_step import StepNotImplementedError

@given(u'att jag är på hemsidan')
def step_impl(context):
    pass

@when(u'jag trycker på knappen {button}')
async def step_impl(context, button):
    await context.page.get_by_test_id(button).click()

@then('bör jag se en lista med {count:d} böcker')
def step_impl(context, count):
    raise StepNotImplementedError("bör jag se en lista med {count:d} böcker")

@then(u'bör jag se en div med {div-class}')
def step_impl(context, div_class):
    raise StepNotImplementedError(u'Then bör jag se en div med <div-class>')
    
@then('bör jag se label {label}')
def step_impl(context, label):
    raise StepNotImplementedError(u'Then bör jag se en text {label}')

@then('bör jag se text {text}')
def step_impl(context, text):
    raise StepNotImplementedError("bör jag se text {text}")
