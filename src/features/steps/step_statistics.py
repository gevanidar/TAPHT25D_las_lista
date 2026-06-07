"""Tests forn the statistics page."""
from behave import when, then


@then("ska jag se statistik för antal böcker {count}")
def step_impl(context, count):
    """Step for validating the number of books that exist in the catalog in the statisitcs page."""
    books, _ = context.reading_list_page.get_statistics()

    count = int(count)

    assert (
        books == count
    ), f"The number of books should be {count}, but they were {books}."


@then("ska jag se statistik för antal favoritmarkerade böcker {count}")
def step_impl(context, count):
    """Step for validating the number of favorite marked books in the statisitcs page."""
    _, favorites = context.reading_list_page.get_statistics()

    count = int(count)

    assert (
        favorites == count
    ), f"The number of favorites should be {count}, but they were {favorites}."
