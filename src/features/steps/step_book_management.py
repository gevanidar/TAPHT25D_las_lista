from behave import when, then


@when("jag fyller i titlen ")
def step_impl(context):
    context.reading_list_page.add_title("")
    context.title = ""


@when("jag fyller i författaren ")
def step_impl(context):
    context.add_input_author("")
    context.author = ""


@when("jag fyller i titlen {title}")
def step_impl(context, title):
    context.reading_list_page.add_title(title)
    context.title = title


@when("jag fyller i författaren {author}")
def step_impl(context, author):
    context.add_input_author(author)
    context.author = author


@then("bör jag inte kunna trycka på knappen {test_id}")
def step_impl(context, test_id):
    # TODO: Extract this to ReadingListPage
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

    assert button.is_disabled(), f"Can submit even when {error_message}"


@then("bör listan innehålla boken {title} och {author}")
def step_impl(context, title, author):
    book_name = f'"{title}", {author}'
    assert context.reading_list_page.contains_row_with_test_id(book_name)


@then("bör listans sista bok vara {title2} och {author2}")
def step_impl(context, title2, author2):
    # TODO: Extract this to ReadingListPage
    rows = context.reading_list_page.get_catalog_rows()
    count = rows.count()
    last_row = rows.nth(count-1)
    last_row_inner = last_row.locator('div')

    row_data_test_id = last_row_inner.get_attribute('data-testid')
    row_book_name = last_row.inner_text()

    expected_data_test_id = f'star-{title2}'
    assert expected_data_test_id == row_data_test_id, f"{expected_data_test_id} is not last in the list, {row_data_test_id} is."

    expected_book_name = f'❤️"{title2}", {author2}'
    assert expected_book_name == row_book_name, f"{expected_book_name} is not last in the list, {row_book_name} is."
