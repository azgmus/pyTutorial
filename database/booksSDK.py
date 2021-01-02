import sqlite3
from .book import Book

def cursor():
    return sqlite3.connect('books.db').cursor()


def add_book(book):
    c = cursor()
    with c.connection:
        c.execute('INSERT INTO books VALUES (?, ?)', (book.title, book.pages))

    return c.lastrowid

def get_books():
    c = cursor()

    with c.connection:
        c.execute('SELECT * FROM books')
        return c.fetchall()



c = cursor()
c.execute('CREATE TABLE IF NOT EXISTS books (title TEXT, pages INTEGER)')
c.connection.close()




