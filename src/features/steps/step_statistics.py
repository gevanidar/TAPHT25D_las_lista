from behave import when, then


@then("ska jag se statistik för antal böcker {count}")
def step_impl(context, count):
    books, _ = context.reading_list_page.get_statistics()

    count = int(count)

    assert (
        books == count
    ), f"The number of books should be {count}, but they were {books}."


@then("ska jag se statistik för antal favoritmarkerade böcker {count}")
def step_impl(context, count):
    _, favorites = context.reading_list_page.get_statistics()

    count = int(count)

    assert (
        favorites == count
    ), f"The number of favorites should be {count}, but they were {favorites}."
