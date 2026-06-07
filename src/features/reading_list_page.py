"""Page class for the Reading List page."""


class ReadingListPage:
    """Page class for the Reading List page."""

    def __init__(self, page):
        """Initialize the page, the base url and a timeout."""
        self.page = page
        self.page.set_default_timeout(1000)
        self.base_url = "https://tap-ht25-testverktyg.github.io/exam/"

    def navigate(self):
        """Navigate the the base url."""
        self.page.goto(self.base_url)

    def click_button_with_test_id(self, test_id):
        """Handle button clicking."""
        locator = self.get_by_test_id(test_id)
        if not locator.is_disabled():
            locator.click()

    def fill_field_with_test_id(self, test_id, text):
        """Fill a field with a specific text by test_id."""
        if not text or len(text) == 0:
            return
        locator = self.get_by_test_id(test_id)
        locator.fill(text)

    def get_by_test_id(self, test_id):
        """Return the locator by test id."""
        return self.page.get_by_test_id(test_id)

    def get_by_label(self, label):
        """Return the locator by label."""
        return self.page.get_by_label(label)

    def get_by_text(self, text):
        """Return the locator by text."""
        return self.page.get_by_text(text)

    def contains_test_id(self, test_id):
        """Check if locator exist with test id."""
        row = self.get_by_test_id(test_id)
        return row is not None

    # Catalog Page route
    def get_catalog_rows(self):
        """Get all rows from the catalog list."""
        return self.page.locator("div.catalog .book")

    def get_catalog_row(self, i):
        """Get a row from the catalog."""
        if i < 0:
            return None

        rows = self.get_catalog_rows()
        count = rows.count()
        if i > count:
            return None

        row = rows.nth(i)
        inner_row = row.locator("div")

        return row, inner_row

    def get_catalog_last_row(self):
        """Return the last catalog row."""
        rows = self.get_catalog_rows()
        count = rows.count()

        i = count - 1

        return self.get_catalog_row(i)

    def toggle_mark_favorite(self, test_id):
        """Toggle the favorite mark in the catalog."""
        row = self.get_by_test_id(test_id)
        row.click()

    def is_favorite_marked(self, test_id):
        """Check if the book is marked as favorite by test id."""
        row = self.get_by_test_id(test_id)
        clazz = row.get_attribute("class")
        return clazz == "star selected"

    # Add book Page route
    def add_input_title(self, title):
        """Insert title into the input field."""
        data_test_id = "add-input-title"
        self.fill_field_with_test_id(data_test_id, title)

    def add_input_author(self, author):
        """Insert author into the input field."""
        data_test_id = "add-input-author"
        self.fill_field_with_test_id(data_test_id, author)

    # Favorites Page route
    def convert_to_fav_test_id(self, test_id):
        """Convert the default test id to favorite test id."""
        return "fav" + test_id[4:]

    def contains_favorite_book_title(self, text):
        """Check if the favorite book title is visible."""
        locator = self.get_by_text(text)
        return locator.is_visible()

    def contains_favorite_book_with_test_id(self, test_id):
        """Check if the favorite book is visible."""
        locator = self.get_by_test_id(test_id)
        return locator.is_visible()

    # Statistics Page route
    def get_statistics_book_count_text(self):
        """Return the locator for the book count."""
        return self.get_by_test_id("book-count")

    def get_statistics_favorites_text(self):
        """Return the locator for the favorite count."""
        return self.get_by_test_id("stars-count")

    def get_statistics(self):
        """Return the book and favorite count."""
        book_count_locator = self.get_statistics_book_count_text()
        favorite_count_locator = self.get_statistics_favorites_text()

        book_count_text = book_count_locator.inner_text()
        favorite_count_text = favorite_count_locator.inner_text()

        book_count = int(
            book_count_text.replace("Listan har ", "").replace(" böcker.", "")
        )
        favorite_count = int(
            favorite_count_text.replace(
                "Våra användare har hjärtmarkerat ", ""
            ).replace(" böcker.", "")
        )

        print(
            f"{book_count_text=}\n{favorite_count_text=}\n{book_count=}\n{favorite_count=}\n"
        )

        return book_count, favorite_count
