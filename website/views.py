from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from datetime import datetime
from .models import Movie, Song
from . import db
import random

views = Blueprint('views', __name__)

@views.route('/super/secret/epic/plan', methods=['POST', 'GET'])
@login_required
def superSecretEpicPlan():
    return render_template('epic.html', user=current_user)

@views.route('/', methods=['POST','GET'])
@login_required
def home():
    return render_template('home.html', user=current_user)


@views.route('/movies', methods=['POST', 'GET'])
@login_required
def movies():
    if request.method == 'POST':
        movie_name = request.form.get('movieNameInput')
        newMovie = Movie(name=movie_name, whoAdded=current_user.username, haveWatched=False)
        db.session.add(newMovie)
        db.session.commit()
        return redirect(url_for('views.movies'))
    allMovies = Movie.query.all()
    notWatched = []

    for movie in allMovies:
        if not movie.haveWatched:
            notWatched.append(movie)

    if len(notWatched) > 0:
        randMovie = random.choice(notWatched)
        return render_template("movies.html", user=current_user, movies=allMovies, randomMovie=randMovie.name)
    else:
        return render_template("movies.html", user=current_user, movies=allMovies, randomMovie="All Movies Watched")


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
    return redirect(url_for('views.movies'))


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
    return redirect(url_for('views.movies'))


@views.route('/songs', methods=['POST', 'GET'])
@login_required
def songs():
    if request.method == 'POST':
        song_name = request.form.get('songNameInput')
        song_artist = request.form.get('songArtistInput')
        newSong = Song(name=song_name, artist=song_artist, whoAdded=current_user.username, haveListened=False)
        db.session.add(newSong)
        db.session.commit()
        return redirect(url_for('views.songs'))

    allSongs = Song.query.all()
    notListened = []

    for song in allSongs:
        if not song.haveListened:
            notListened.append(song)

    if len(notListened) > 0:
        randSong = random.choice(notListened)
        return render_template('songs.html', user=current_user, songs=allSongs, randomSong=randSong.name)
    else:
        return render_template('songs.html', user=current_user, songs=allSongs, randomSong="All Songs Listened To")



@views.route('/listenSong/<song_id>')
@login_required
def listenSong(song_id):
    song = Song.query.filter_by(id=song_id).first()
    if song:
        tempBool = song.haveListened
        song.haveListened = not tempBool
        db.session.commit()
        if (song.haveListened):
            flash('Song Listened To', category='success')
        else:
            flash('Song Unlistened To', category='error')
    else:
        flash("Error Occurred", category='error')
    return redirect(url_for('views.songs'))


@views.route('/songDelete/<song_id>')
@login_required
def songDelete(song_id):
    song = Song.query.filter_by(id=song_id).first()
    if song:
        msg_text = f"Successfully Deleted {song.name}"
        db.session.delete(song)
        db.session.commit()
        flash(msg_text, category='success')
    else:
        flash("Error occurred", category='error')
    return redirect(url_for('views.songs'))


@views.route('/settings')
@login_required
def settings():
    return render_template('settings.html', user=current_user)


@views.context_processor
@login_required
def datetime_context_processor():
    def daysSince(currDate):
        daysSinceVar = (datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) - currDate.replace(tzinfo=None, hour=0, minute=0, second=0, microsecond=0)).days
        if daysSinceVar == 1:
            return 'Yesterday'
        elif daysSinceVar == 0:
            return 'Today'
        else:
            return f'{daysSinceVar} days ago'

    return dict(daysSince=daysSince)
