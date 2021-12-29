"""
This is the movies module and supports all the REST actions for the
movies data
"""

from flask import make_response, abort
from config import db
from models import Director, Movie, MovieSchema


def read_all(sorted_by='id', limit=None, movie_sort='asc'):
    """
    This function responds to a request for api/director/movies with the complete list of movies

    :params sorted_by:  string enum to display data in order by variable
    :params limit:  integer to limit length of movie list
    :params director_sort:  string enum to sort ascending or descending

    :return:    json list of all movies for all directors 
    """
    sort_by = ''
    if sorted_by == 'budget':
        sort_by = Movie.budget
    elif sorted_by == 'revenue':
        sort_by = Movie.revenue
    elif sorted_by == 'popularity':
        sort_by = Movie.popularity
    elif sorted_by == 'vote average':
        sort_by = Movie.vote_average
    elif sorted_by == 'vote count':
        sort_by = Movie.vote_count
    elif sorted_by == 'id':
        sort_by = Movie.id
    else:
        return f"Cannot find parameters{sorted_by}", 404

    sort_method = ''
    if movie_sort == 'asc':
        sort_method = db.asc(sort_by)
    else:
        sort_method = db.desc(sort_by)

    if limit == None:
        movies = Movie.query.order_by(sort_method).all()
    else:
        movies = Movie.query.order_by(sort_method).limit(limit).all()       

    movie_schema = MovieSchema(many=True)
    data = movie_schema.dump(movies)
    return data


def read_one(director_id, movie_id):
    """
    This function responds to a request for
    /api/director/{director_id}/movies/{movie_id}
    with one matching movie for the associated director

    :param director_id:       Id of director the movie is related to
    :param note_id:         Id of the movie
    :return:                json string of movie contents
    """

    movie = (
        Movie.query.join(Director, Director.id == Movie.director_id)
        .filter(Director.id == director_id)
        .filter(Movie.id == movie_id)
        .one_or_none()
    )

    if movie is not None:
        movie_schema = MovieSchema()
        data = movie_schema.dump(movie)
        return data, 200

    else:
        abort(404, f"Movie not found for id: {movie_id}")


def create(director_id, movie):
    """
    This function creates a new movie related to the passed in director id.

    :param person_id:       Id of the director the movie is related to
    :param movie:            The JSON containing the movie data
    :return:                201 on success
    """

    director = Director.query.filter(Director.id == director_id).one_or_none()

    if director is None:
        abort(404, f"Director not found for Id: {director_id}")

    schema = MovieSchema()
    new_movie = schema.load(movie, session=db.session)

    director.movies.append(new_movie)
    db.session.commit()

    data = schema.dump(new_movie)

    return data, 201


def update(director_id, movie_id, movie):
    """
    This function updates an existing movie related to the passed in director id.

    :param director_id:     Id of the director the movie is related to
    :param movie_id:        Id of the note to update

    :return:                200 success
    """

    update_movie = (
        Movie.query.join(Director, Director.id == Movie.director_id).filter(Director.id == director_id)
        .filter(Movie.id == movie_id)
        .one_or_none()
    )

    if update_movie is not None:
        schema = MovieSchema()
        update = schema.load(movie, session=db.session)

        update.director_id = update_movie.director_id
        update.id = update_movie.id

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_movie)

        return data, 200

    else:
        abort(404, f"Movie not found for Id: {movie_id}")


def delete(director_id, movie_id):
    """
    This function deletes a movie from the movies structure

    :param director_id:   Id of the director the movie is related to
    :param movie_id:     Id of the movie to delete
    :return:            200 on successful delete, 404 if not found
    """

    movie = (
        Movie.query.join(Director, Director.id == Movie.director_id).filter(Director.id == director_id)
        .filter(Movie.id == movie_id)
        .one_or_none()
    )

    if movie is not None:
        db.session.delete(movie)
        db.session.commit()
        return make_response(f"Movie {movie_id} deleted", 200)

    else:
        abort(404, f"Movie not found for Id: {movie_id}")

def search(movies_name, limit=None):
    '''
    This function respond to a request for /api/movies/{director_name}
    with one matching director from directors

    :param director_name:  Name of director to find
    :return:    director matching id
    '''
    # Build the initial query
    if limit == None:
        movie = Movie.query.order_by(Movie.id).filter(Movie.title.ilike('%'+movies_name+'%')).all()
    else:
        movie = Movie.query.order_by(Movie.id).filter(Movie.title.ilike('%'+movies_name+'%')).limit(limit).all()

    if movie == []:
        abort(404, f"movie not found for Id: {movies_name}")

    else:
        movies_schema = MovieSchema(many=True)
        data = movies_schema.dump(movie)
        return data