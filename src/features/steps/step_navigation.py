"""Test navigation on the home page."""
from behave import when, then

@given("att jag är på hemsidan")
def step_impl(context):
    """Step for going to the home page."""
    context.reading_list_page.navigate()


@when("jag trycker på knappen {button}")
def step_impl(context, button):
    """Step for clicking on a button."""
    locator = context.reading_list_page.click_button_with_test_id(button)


@then("bör jag se en lista med {count:d} böcker")
def step_impl(context, count):
    """Validate the number of books in the catalog."""
    rows = context.reading_list_page.get_catalog_rows()

    assert count == rows.count()


@then("bör jag se en div med {div_class}")
def step_impl(context, div_class):
    """Validate that the div i has a specific class."""
    locator = context.reading_list_page.page.locator("main")
    assert locator is not None
    locator.get_by_text(div_class)
    assert locator is not None


@then("bör jag se en label {label}")
def step_impl(context, label):
    """Step for checking that the label exists."""
    locator = context.reading_list_page.get_by_label(label)
    assert locator is not None


@then("bör jag se en text {text}")
def step_impl(context, text):
    """Step for checking that a text exists."""
    locator = context.reading_list_page.get_by_text(text)
    assert locator is not None
