from behave import when, then

from behave.api.pending_step import StepNotImplementedError

@given(u'att jag står på sidan {page}')
def step_impl(context, page):
    locator = context.reading_list_page.page.locator('main')
    assert locator is not None
    locator.get_by_text(page)
    assert locator is not None

@when(u'jag markerar en rad')
def step_impl(context):
    locator = contest.reading_list_page.get_by_test_id('star-Ormar på ett plan: En Python-berättelse')
    locator.hover()

@then('klickar på hjärtat till höger')
def step_impl(context):
    locator = context.reading_list_page.get_by_test_id('star-Ormar på ett plan: En Python-berättelse')
    locator.click()

@then(u'ska boken favoritmarkeras')
def step_impl(context, div_class):
    locator = context.reading_list_page.is_favorite_marked('star-Ormar på ett plan: En Python-berättelse')


#		<div data-testid="star-Ormar på ett plan: En Python-berättelse" class="star" role="button">❤️</div>
#		<div data-testid="star-Ormar på ett plan: En Python-berättelse" class="star-selected" role="button">❤️</div>

