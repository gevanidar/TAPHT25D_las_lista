class InitialState:
    def __init__(self):
        book_0 = "star-Ormar på ett plan: En Python-berättelse"
        book_1 = "star-The Pragmatic Procrastinator"
        book_2 = "star-Python för folk som hatar ormar"
        book_3 = "star-Why Your Tests Are Lying to You"
        book_4 = "star-Playwright: Click It Till You Make It"
        book_5 = "star-Git Blame and Other Ways to Lose Friends"
        book_6 = "star-Learn Python in 21 Years"
        book_7 = "star-Agile Is a Feeling"
        book_8 = "star-Playwright: Waiting for Selectors"
        book_9 = "star-Stack Overflow: A Love Story"
        book_10 = "star-My First Regex (And Last)"
        book_11 = "star-The Developer Who Knew Nothing"
        book_12 = "star-The Bugs are Coming"
        self.books = [
            book_0,
            book_1,
            book_2,
            book_3,
            book_4,
            book_5,
            book_6,
            book_7,
            book_8,
            book_9,
            book_10,
            book_11,
            book_12,
        ]

    # TODO: This is the test-id
    def get_books(self):
        return self.books
