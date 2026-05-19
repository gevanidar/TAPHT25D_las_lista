from behave import when, then

from behave.api.pending_step import StepNotImplementedError

@given(u'att jag är på hemsidan')
def step_impl(context):
    pass

@when(u'jag trycker på knappen {button}')
def step_impl(context, button):
    locator = context.page.get_by_test_id(button)
    if not locator.is_disabled():
        locator.click()

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
        locator = context.page.get_by_test_id(book)
        if locator:
            c += 1
    assert c == count

@then(u'bör jag se en div med {div_class}')
def step_impl(context, div_class):
    locator = context.page.locator('main')
    assert locator is not None
    locator.get_by_text(div_class)
    assert locator is not None
    
@then('bör jag se en label {label}')
def step_impl(context, label):
    locator = context.page.get_by_label(label)
    assert locator is not None


@then('bör jag se en text {text}')
def step_impl(context, text):
    locator = context.page.get_by_text(text)
    assert locator is not None


# Lista
# <div class="catalog">
# <p>
# Sidan för dig som gillar att läsa. Välj dina favoriter. </p>
# <div class="book">
# <div data-testid="star-Ormar på ett plan: En Python-berättelse" class="star" role="button">
# ❤️</div>
# "Ormar på ett plan: En Python-berättelse", Guido van Rossum</div>
# <div class="book">
# <div data-testid="star-The Pragmatic Procrastinator" class="star" role="button">
# ❤️</div>
# "The Pragmatic Procrastinator", Dave Thomasson</div>
# <div class="book">
# <div data-testid="star-Python för folk som hatar ormar" class="star" role="button">
# ❤️</div>
# "Python för folk som hatar ormar", Monty Pythonsson</div>
# <div class="book">
# <div data-testid="star-Why Your Tests Are Lying to You" class="star" role="button">
# ❤️</div>
# "Why Your Tests Are Lying to You", Kent Backdoor</div>
# <div class="book">
# <div data-testid="star-Playwright: Click It Till You Make It" class="star" role="button">
# ❤️</div>
# "Playwright: Click It Till You Make It", Microslop Browserdóttir</div>
# <div class="book">
# <div data-testid="star-Git Blame and Other Ways to Lose Friends" class="star" role="button">
# ❤️</div>
# "Git Blame and Other Ways to Lose Friends", Linus Torvalds</div>
# <div class="book">
# <div data-testid="star-Learn Python in 21 Years" class="star" role="button">
# ❤️</div>
# "Learn Python in 21 Years", Sams Teachyourself</div>
# <div class="book">
# <div data-testid="star-Agile Is a Feeling" class="star" role="button">
# ❤️</div>
# "Agile Is a Feeling", Jeff Sutherland</div>
# <div class="book">
# <div data-testid="star-Playwright: Waiting for Selectors" class="star" role="button">
# ❤️</div>
# "Playwright: Waiting for Selectors", Samuel Barclay Beckett</div>
# <div class="book">
# <div data-testid="star-Stack Overflow: A Love Story" class="star" role="button">
# ❤️</div>
# "Stack Overflow: A Love Story", Copy Pasta</div>
# <div class="book">
# <div data-testid="star-My First Regex (And Last)" class="star" role="button">
# ❤️</div>
# "My First Regex (And Last)", Larry Wallström</div>
# <div class="book">
# <div data-testid="star-The Developer Who Knew Nothing" class="star" role="button">
# ❤️</div>
# "The Developer Who Knew Nothing", George R.R. Martin</div>
# <div class="book">
# <div data-testid="star-The Bugs are Coming" class="star" role="button">
# ❤️</div>
# "The Bugs are Coming", George R.R. Martin</div>
# </div>
 
