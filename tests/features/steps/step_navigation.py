from behave import when, then

@when('jag trycker på knappen "{button}"')
def step_impl(context, button):
    raise NotImplementedError("Jag trycker på knappen är inte implementerad än")

# TODO: Should there be a data-test-id sent in?
@then('bör jag se en lista med {count:d} böcker')
def step_impl(context, count):
    raise NotImplementedError("bör jag se en lista med {count:d} böcker")

@then('Then bör jag se en div med {div_class}')
def step_impl(context, div_class):
    raise NotImplementedError("Then bör jag se en div med {div_class}")
    
@then('Then bör jag se label {label}')
def step_impl(context, label):
    raise NotImplementedError("Then bör jag se en div med {class}")

@then('Then bör jag se text {text}')
def step_impl(context, text):
    raise NotImplementedError("Then bör jag se en div med {class}")
