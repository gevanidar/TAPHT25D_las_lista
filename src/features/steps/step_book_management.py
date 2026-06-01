from behave import when, then

from behave.api.pending_step import StepNotImplementedError


def get_rows(context):
    page = context.reading_list_page.page
    return page.locator("div.catalog .book")


def get_favorite_rows(context):
    page = context.reading_list_page.page
    return page.locator("div.favorites .book")


def get_row(context, n):
    rows = get_rows(context)

    if rows.count() < n:
        raise StepNotImplementedError("No way to reach row `n`")
    row = rows.nth(n)
    return row

def get_favorite_row(context, n):
    rows = get_favorite_rows(context)

    if rows.count() < n:
        raise StepNotImplementedError("No way to reach row `n`")
    row = rows.nth(n)
    return row



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
    rows = get_rows(context)

    contains = False
    for n in range(rows.count()):
        row = rows.nth(n)
        row_title = get_title(row)
        if title != row_title:
            continue
        row_author = get_author(row)
        if author == row_author:
            contains = True
            break

    book_name = f'"{title}", {author}'
    assert contains, f"{book_name} is not in the list"


@then("bör listans sista bok vara {title2} och {author2}")
def step_impl(context, title2, author2):
    rows = get_rows(context)
    last_row = rows[-1]
    contains = True
    row_title = get_title(row)
    if title != row_title:
        contains = False
    row_author = get_author(row)
    if author != row_author:
        contains = False

    book_name = f'"{title}", {author}'
    assert contains, f"{book_name} is not in the list"


@then("ska jag se en bok med {title} i favoritlistan")
def step_impl(context, title):
    rows = get_favorite_rows(context)

    contains = False
    for n in range(rows.count()):
        row = rows.nth(n)
        print(f'looped {row=}')
    row = get_favorite_row(context, 0)
    print(f'{row=}')
    contains = False
    row_title = get_title(row)
    if title != row_title:
        contains = True

    book_title = f'"{title}"'
    assert contains, f"{book_title} is not in the list"

    fav_title = "fav-" + title
    book = context.reading_list_page.get_by_test_id(fav_title)
    # TODO: Fix errors
    print(f"Should not be found {book=}")
    print(f"{context.title=}")
    assert book is None, f"{title} is not in the favorite list"
