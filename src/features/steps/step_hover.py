from behave import when, then

from behave.api.pending_step import StepNotImplementedError


def get_first_book(context):
    initial_state = context.initial_state
    books = initial_state.get_books()
    # print(f"{context=}\n{initial_state=}\n{books=}")
    if books and len(books) > 0:
        return books[0]
    return None


@when("jag hovrar över en rad")
def step_impl(context):
    # book = get_first_book(context)
    # locator = context.reading_list_page.get_by_test_id(book)

    page = context.reading_list_page.page
    rows = page.locator("div.catalog .book")

    n = 0
    colors = []
    original_colors = []
    for n in range(2):
        row = rows.nth(n)
        original_color = row.evaluate(
            "el => window.getComputedStyle(el).backgroundColor"
        )
        if not original_colors:
            original_colors = []
        original_colors.append(original_color)
        row.hover()
        page.wait_for_timeout(500)
        color = row.evaluate("el => window.getComputedStyle(el).backgroundColor")
        if not colors:
            colors = []
        colors.append(color)
    context.original_colors = original_colors
    context.colors = colors


@then("ska en raden visuellt förtydligas")
def step_impl(context):
    n = 0
    color = context.colors[n]
    original_color = context.original_colors[n]

    assert (
        color != "rgb(0, 0, 0, 0)"
    ), "Incorrect selection of element which has hover effect."
    assert color != original_color, "The hover had no effect on color"
    assert color == "rgb(229, 190, 149)", "Incorrect hover color for first row"

    n = 1
    color = context.colors[n]
    original_color = context.original_colors[n]

    assert (
        color != "rgb(0, 0, 0, 0)"
    ), "Incorrect selection of element which has hover effect."
    assert color != original_color, "The hover had no effect on color"
    assert color == "rgb(201, 198, 187)", "Incorrect hover color for first row"
