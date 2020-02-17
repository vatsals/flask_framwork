from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    names = db.Column(db.String(100), unique=True)

    def __init__(self, names):
        self.names = names

    def __repr__(self):
        return "<Author %r>" % (self.names)
