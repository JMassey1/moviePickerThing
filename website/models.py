from . import db
from flask_login import UserMixin
from sqlalchemy import func


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    whoAdded = db.Column(db.String(150), db.ForeignKey('user.id'))
    dateAdded = db.Column(db.DateTime(timezone=True), default=func.now())
    haveWatched = db.Column(db.Boolean, default=False)


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    artist = db.Column(db.String(150))
    whoAdded = db.Column(db.String(150), db.ForeignKey('user.id'))
    dateAdded = db.Column(db.DateTime(timezone=True), default=func.now())
    haveListened = db.Column(db.Boolean, default=False)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    movieSuggestions = db.relationship('Movie')
