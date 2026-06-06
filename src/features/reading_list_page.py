class ReadingListPage:
    def __init__(self, page):
        self.page = page
        self.page.set_default_timeout(1000)
        self.base_url = "https://tap-ht25-testverktyg.github.io/exam/"

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

    def fill_field_with_test_id(self, test_id, text):
        if not text or len(text) == 0:
            return
        locator = self.get_by_test_id(test_id)
        locator.fill(text)

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
        return clazz == "star selected"

    def contains_row_with_test_id(self, test_id):
        row = self.get_by_test_id(test_id)
        return row is not None

    # Catalog Page route
    def get_catalog_rows(self):
        return self.page.locator("div.catalog .book")

    def add_input_title(self, title):
        data_test_id = 'add-input-title'
        self.fill_field_with_test_id(data_test_id, title)

    def add_input_author(self, author):
        data_test_id = 'add-input-author'
        self.fill_field_with_test_id(data_test_id, author)
    
    # Statistics Page route
    def get_statistics_book_count_text(self):
        return self.get_by_test_id('book-count')

    def get_statistics_favorites_text(self):
        return self.get_by_test_id('stars-count')

    def get_statistics(self):
        book_count_locator = self.get_statistics_book_count_text()
        favorite_count_locator = self.get_statistics_favorites_text()

        book_count_text = book_count_locator.inner_text();
        favorite_count_text = favorite_count_locator.inner_text();

        book_count = int(book_count_text.replace('Listan har ', '').replace(' böcker.', ''))
        favorite_count = int(favorite_count_text.replace('Våra användare har hjärtmarkerat ', '').replace(' böcker.', ''))

        print(f"{book_count_text=}\n{favorite_count_text=}\n{book_count=}\n{favorite_count=}\n")

        return book_count, favorite_count

