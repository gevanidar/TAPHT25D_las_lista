from behave import when, then

from behave.api.pending_step import StepNotImplementedError


def get_rows(context):
    page = context.reading_list_page.page
    return page.locator("div.catalog .book")


@when("jag fyller i titlen ")
def step_impl(context):
    data_test_id = "add-input-title"
    context.reading_list_page.fill_field_with_test_id(data_test_id, "")
    context.title = ""


@when("jag fyller i författaren ")
def step_impl(context):
    data_test_id = "add-input-author"
    context.reading_list_page.fill_field_with_test_id(data_test_id, "")
    context.author = ""


@when("jag fyller i titlen {title}")
def step_impl(context, title):
    data_test_id = "add-input-title"
    context.reading_list_page.fill_field_with_test_id(data_test_id, title)
    context.title = title


@when("jag fyller i författaren {author}")
def step_impl(context, author):
    data_test_id = "add-input-author"
    context.reading_list_page.fill_field_with_test_id(data_test_id, author)
    context.author = author


@then("bör jag inte kunna trycka på knappen {test_id}")
def step_impl(context, test_id):
    button = context.reading_list_page.get_by_test_id(test_id)

    title = context.title
    author = context.author

    error_message = ""
    if not title or len(title) == 0:
        error_message = "title is empty"
    if not author or len(author) == 0:
        if len(error_message) == 0:
            error_message += " and "
        error_message += "author is empty"
    error_message += "."

    print(f"{button=}\n{button.is_disabled()=}\n{error_message=}\n{title=}\n{author=}")

    assert button.is_disabled(), f"Can submit even when {error_message}"


@then("bör listan innehålla boken {title} och {author}")
def step_impl(context, title, author):
    book_name = f'"{title}", {author}'
    assert context.reading_list_page.contains_row_with_test_id(book_name)


@then("bör listans sista bok vara {title2} och {author2}")
def step_impl(context, title2, author2):
    rows = get_rows(context)
    last_row = rows.last

    row_data_test_id = row.get_attribute('data-test-id')

    expected_book_name = f'"{title2}", {author2}'
    assert expected_book_name == row_data_test_id, f"{expected_book_name} is not last in the list, {row_data_test_id} is."
