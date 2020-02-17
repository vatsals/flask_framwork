from flask import Flask, current_app
from bookshelf.utils import get_instance_folder_path
from bookshelf.book.controllers import book
from bookshelf.author.controllers import author
from bookshelf.config import configure_app
from bookshelf.models import db


app = Flask(
    __name__,
    instance_path=get_instance_folder_path(),
    instance_relative_config=True
)

configure_app(app)
db.init_app(app)


@app.route("/")
def home():
    return 'Welcome to the application'


app.register_blueprint(book, url_prefix="/book")
app.register_blueprint(author, url_prefix="/author")
