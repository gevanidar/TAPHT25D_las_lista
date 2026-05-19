from behave import when, then
from reading_list import HomePage

from behave.api.pending_step import StepNotImplementedError

@given(u'att jag är på hemsidan')
def step_impl(context):
    home_page = HomePage(context.page)

@when(u'jag trycker på knappen <knapp>')
def step_impl(context):
    raise StepNotImplementedError(u'When jag trycker på knappen <knapp>')

@then('bör jag se en lista med {count:d} böcker')
def step_impl(context, count):
    raise StepNotImplementedError("bör jag se en lista med {count:d} böcker")

@then(u'bör jag se en div med <div-class>')
def step_impl(context, div_class):
    raise StepNotImplementedError(u'Then bör jag se en div med <div-class>')
    
@then('bör jag se label {label}')
def step_impl(context, label):
    raise StepNotImplementedError(u'Then bör jag se en text {label}')

@then('bör jag se text {text}')
def step_impl(context, text):
    raise StepNotImplementedError("bör jag se text {text}")
