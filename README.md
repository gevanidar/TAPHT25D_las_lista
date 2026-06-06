
## How to run

Ensure that you are in the project root directory and have installed `python` and everything in the `requirements.txt`.

From the project root you can now run the tests for BDD and TDD.

### Running TDD

```
pytest
```

### Running BDD

```
behave tests/features/
```

## What has been tested

### Backend
A class for containing the information for what describes a book have been tested and added. The BookStore class has been tested with unit tests and using mocking for allowing tests for the `toggle_favorite` function. The FavoriteBooks have been tested for marking books as favorites, and also for removing them from the favorites list. Combination of adding and removing books from favorites have been tested to make sure that the correct book is removed from the favorite list.

### Frontend

Navigation to all pages have been tested, navigation to the current page has been specifically tested for `catalog`.
Adding books to the book store has been tested, the test includes adding one book and checking that it exists in the list. Tests towards the original bookstore (initial state) has been tested. Tests have been done for validating that the book added is added last into the list.
Marking a book as a favorite has been tested.
Hovering over a book in the catalog has been tested for checking the change of color (hovering effect).
The statistics page have been checked that it does increate the number of books that has been marked as favorites and the total number of books in the bookstore.
