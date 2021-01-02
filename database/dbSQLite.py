from database.book import Book
from database import booksSDK

book = Book('first book', 72)
print(booksSDK.get_books())
