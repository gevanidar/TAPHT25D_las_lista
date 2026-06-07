"""Step module for testing the hover effect on rows in the catalog."""
from behave import when, then


def evaluate_color(locator):
    """Return the color of the locator."""
    if not locator:
        return None
    return locator.evaluate("el => window.getComputedStyle(el).backgroundColor")


def get_first_book(context):
    """Return the first book in the catalog list."""
    initial_state = context.initial_state
    books = initial_state.get_books()
    if books and len(books) > 0:
        return books[0]
    return None


@when("jag hovrar över en rad")
def step_impl(context):
    """Step for when a user hovers over a boo row in the catalog."""

    rows = context.reading_list_page.get_catalog_rows()

    count = rows.count()
    colors = []
    original_colors = []
    for n in range(count):
        row = rows.nth(n)

        original_color = evaluate_color(row)
        original_colors.append(original_color)

        row.hover()
        context.reading_list_page.page.wait_for_timeout(500)

        color = evaluate_color(row)

        colors.append(color)

    context.original_colors = original_colors
    context.colors = colors
    context.count = count


def validate_color_on_row_hover(context, n, expected):
    """Helper function for validating the color on a row."""
    color = context.colors[n]
    original_color = context.original_colors[n]

    assert (
        color != "rgb(0, 0, 0, 0)"
    ), "Incorrect selection of element which has hover effect."
    assert color != original_color, "The hover had no effect on color"
    assert color == expected , "Incorrect hover color for first row"


@then("ska en raden visuellt förtydligas")
def step_impl(context):
    """Step for checking that the hover has actually taken effect."""
    expected_alternating = ["rgb(229, 190, 149)", "rgb(201, 198, 187)"]
    count = context.count
    for n in range(count):
        expected = expected_alternating[n%2]
        validate_color_on_row_hover(context, n, expected)
