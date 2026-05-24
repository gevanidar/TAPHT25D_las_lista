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

    def toggle_mark_favorite(self, test_id):
        row = self.get_by_test_id(test_id)
        row.click()

    def get_by_test_id(self, test_id):
        return self.page.get_by_test_id(test_id)

    def get_by_label(self, label):
        return self.page.get_by_label(label)

    def get_by_text(self, text):
        return self.page.get_by_text(text)

    def is_favorite_marked(self, test_id):
        row = self.get_by_test_id(test_id)
        clazz = row.get_attribute("class")
        return clazz == 'star selected'

    def contains_favorite(self, test_id):
        row = self.get_by_test_id(test_id)
        return row is not None

