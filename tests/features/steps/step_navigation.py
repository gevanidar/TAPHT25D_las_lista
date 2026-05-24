from behave import when, then

from behave.api.pending_step import StepNotImplementedError

@given(u'att jag är på hemsidan')
def step_impl(context):
    pass

@when(u'jag trycker på knappen {button}')
def step_impl(context, button):
    locator = context.reading_list_page.click_button_by_test_id(button)

@then('bör jag se en lista med {count:d} böcker')
def step_impl(context, count):
    book_0 ="star-Ormar på ett plan: En Python-berättelse"
    book_1 ="star-The Pragmatic Procrastinator"
    book_2 ="star-Python för folk som hatar ormar"
    book_3 ="star-Why Your Tests Are Lying to You"
    book_4 ="star-Playwright: Click It Till You Make It"
    book_5 ="star-Git Blame and Other Ways to Lose Friends"
    book_6 ="star-Learn Python in 21 Years"
    book_7 ="star-Agile Is a Feeling"
    book_8 ="star-Playwright: Waiting for Selectors"
    book_9 ="star-Stack Overflow: A Love Story"
    book_10 ="star-My First Regex (And Last)"
    book_11 ="star-The Developer Who Knew Nothing"
    book_12 ="star-The Bugs are Coming"
    books = [book_0,book_1 ,book_2 ,book_3 ,book_4 ,book_5 ,book_6 ,book_7 ,book_8 ,book_9 ,book_10,book_11,book_12]
    c = 0
    for book in books:
        locator = context.reading_list_page.get_by_test_id(book)
        if locator:
            c += 1
    assert c == count

@then(u'bör jag se en div med {div_class}')
def step_impl(context, div_class):
    locator = context.reading_list_page.page.locator('main')
    assert locator is not None
    locator.get_by_text(div_class)
    assert locator is not None
    
@then('bör jag se en label {label}')
def step_impl(context, label):
    locator = context.reading_list_page.get_by_label(label)
    assert locator is not None


@then('bör jag se en text {text}')
def step_impl(context, text):
    locator = context.reading_list_page.get_by_text(text)
    assert locator is not None
