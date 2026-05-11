"""Representation of the list of my favorite books."""

class FavoriteBooks:
    """A list of my favorite books."""

    def __init__(self):
        """Todo."""
        self.book_ids = []

    def add(self, book_id):
        """Add a book_id to to the favorite books list."""
        if book_id not in self.book_ids:
            self.book_ids.append(book_id)

    def remove(self, book_id):
        """Todo."""
        print("running un implemented method *(remove)")
        # TODO: Implement
        pass
