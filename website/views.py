from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from .models import Movie
from . import db
import random

views = Blueprint('views', __name__)


@views.route('/', methods=['POST', 'GET'])
@login_required
def home():
    if request.method == 'POST':
        movie_name = request.form.get('movieNameInput')
        newMovie = Movie(name=movie_name, whoAdded=current_user.username, haveWatched=False)
        db.session.add(newMovie)
        db.session.commit()

    allMovies = Movie.query.all()

    randMovie = random.choice(allMovies)

    while randMovie.haveWatched:
        randMovie = random.choice(allMovies)

    return render_template("home.html", user=current_user, movies=allMovies, randomMovie=randMovie.name)


@views.route('/movieDelete/<movie_id>')
@login_required
def movieDelete(movie_id):
    movie = Movie.query.filter_by(id=movie_id).first()
    if movie:
        msg_text = 'Successfully Deleted %s' % str(movie.name)
        db.session.delete(movie)
        db.session.commit()
        flash(msg_text, category='success')
    else:
        flash("Error occurred", category='error')
    return redirect(url_for('views.home'))


@views.route('/movieWatched/<movie_id>')
@login_required
def watchMovie(movie_id):
    movie = Movie.query.filter_by(id=movie_id).first()
    if movie:
        tempBool = movie.haveWatched
        movie.haveWatched = not tempBool
        db.session.commit()
        if (movie.haveWatched):
            flash('Movie Watched', category='success')
        else:
            flash('Movie Unwatched', category='error')
    else:
        flash("Error occurred", category='error')
    return redirect(url_for('views.home'))


@views.route('/settings')
@login_required
def settings():
    return render_template('settings.html', user=current_user)
