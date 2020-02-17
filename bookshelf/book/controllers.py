from flask import Blueprint
from bookshelf.models.book import Book

book = Blueprint("book", __name__)


@book.route("/")
def get_books():
    # books = [book for book in Book.query.all()]
    return 'Books Main'


@book.route("/create", methods=["GET", "POST"])
def create_book():
    return 'Book Created'
