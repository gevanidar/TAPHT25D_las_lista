from behave import when, then

from behave.api.pending_step import StepNotImplementedError


# TODO: Change the strange feature text, since do we really want to test if the text is correct or the count? 
@then("ska jag se statistik texten för antal böcker Listan har {count} böcker.")
def step_impl(context, count):
  books, _ = context.reading_list_page.get_statistics()

  assert books == count, f"The number of books should be {count}, but they were {books}."

# TODO: Change the strange feature text, since do we really want to test if the text is correct or the count? 
@then("ska jag se statistik texten för antal favoritmarkerade böcker Våra användare har hjärtmarkerat {count} böcker.")
def step_impl(context, count):
  _, favorites = context.reading_list_page.get_statistics()

  assert favorites == count, f"The number of favorites should be {count}, but they were {favorites}."

