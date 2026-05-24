class SearchPage:
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

    def mark_as_favorite(self, result_index):
        raise NotImplementedError

    def go_to_via_button(self, button_name):
        raise NotImplementedError
