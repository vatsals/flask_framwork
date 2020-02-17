from flask import Blueprint
from bookshelf.models.author import Author

author = Blueprint("author", __name__)


@author.route("/")
def get_authors():
    # authors = [author for author in Author.query.all()]
    return 'Authors Main'


@author.route("/create", methods=["GET", "POST"])
def create_author():
    return 'Author Created'
