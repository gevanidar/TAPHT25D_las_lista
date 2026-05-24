class ReadingListPage:
    def __init__(self, page):
        self.page = page
        self.page.set_default_timeout(1000)
        self.base_url = "https://tap-ht25-testverktyg.github.io/exam/"
        self.navigate()

        self.search_input = page.locator("#search-input")
        self.search_button = page.locator("#search-button")
        self.results = page.locator(".search-results .song-item")
        self.favorite_buttons = page.locator(".song-item .favorite-btn")

    def navigate(self):
        self.page.goto(self.base_url)

    def click_button_with_test_id(self, test_id):
        locator = self.get_by_test_id(test_id)
        if not locator.is_disabled():
            locator.click()

    def mark_as_favorite(self, result_index):
        raise NotImplementedError

    def get_by_test_id(self, test_id):
        return self.page.get_by_test_id(test_id)

    def get_by_label(self, label):
        return self.page.get_by_label(label)

    def get_by_text(self, text):
        return self.page.get_by_text(text)

    def is_favorite_marked(self, test_id):
        locator = self.get_by_test_id(test_id)
        print(f"{locator=}")
        star_selected = locator.get_by_text('star-selected')
        print(f"{star_selected=}")
        print(f"{vars(star_selected)=}")
        print(f"{dir(star_selected)=}")
        return star_selected is not None

    def get_initial_books(self):
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
        return [book_0, book_1, book_2, book_3, book_4, book_5, book_6, book_7, book_8, book_9, book_10, book_11, book_12]
