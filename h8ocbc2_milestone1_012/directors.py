"""
This is the directors module and supports all the REST actions for the
directors data
"""

from flask import make_response, abort
from config import db
from models import Director, DirectorSchema, Movie


def read_all(limit=None):
    '''
    This function responds to a request for /api/directors with the complete list of directors

    :return: json string of list of directors
    '''

    # Create the list of directors from our data
    if limit is None:
        directors = Director.query.order_by(Director.id).all()
    else:    
        directors = Director.query.order_by(Director.id).limit(limit).all()

    # Serialize the data for the response
    director_schema = DirectorSchema(many=True)
    data = director_schema.dump(directors)
    return data


def read_one(director_id):
    '''
    This function respond to a request for /api/directors/{id}
    with one matching director from directors

    :param id:  Id of director to find
    :return:    director matching id
    '''
    # Build the initial query
    director = (
        Director.query.filter(Director.id == director_id)
        .outerjoin(Movie)
        .one_or_none()
    )

    # director id was found in our data
    if director is not None:
        # Serialize the data dor the response
        director_schema = DirectorSchema()
        data = director_schema.dump(director)
        return data

    # director id was not found in our data
    else:
        abort(404, f"Director not found for Id: {director_id}")


def create(director):
    """
    This function creates a new director in the directors structure
    based on the passed in director data

    :param director:    director to create in directors structure

    :return:            201 on success, 406 on director exists
    """
    name = director.get("name")
    gender = director.get("gender")
    uid = director.get("uid")
    department = director.get("department")

    # validator
    if not(name and (gender or gender > 2 or gender < 0) and uid and department):
        return "", 400

    existing_director = (
        Director.query
        .filter(Director.uid == uid)
        .one_or_none()
    )

    if existing_director is None:
        schema = DirectorSchema()
        new_director = schema.load(director, session=db.session)

        db.session.add(new_director)
        db.session.commit()

        data = schema.dump(new_director)

        return data, 201

    else:
        abort(409, f"Director with {uid} already exist")


def update(director_id, director):
    """
    This function updates an exixting director in the directors structure

    :param id:          Id of the director to update in the directors structure
    :param director:    director to update

    :return:             updated director structure
    """

    update_director = Director.query.filter(
        Director.id == director_id
    ).one_or_none()

    if update_director is not None:
        schema = DirectorSchema()
        update = schema.load(director, session=db.session)

        update.id = update_director.id

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update)

        return data, 200
    else:
        abort(404, f"Director not found for Id: {director_id}")


def delete(director_id):
    """
    This function deletes a director from the directors structure

    :param id:      Id of the director to delete

    :return:        200 on successfull delete, 404 if id not found
    """

    director = Director.query.filter(Director.id == director_id).one_or_none()

    if director is not None:
        db.session.delete(director)
        db.session.commit()
        return make_response(f"Director {director_id} deleted", 200)

    else:
        abort(404, f"Director not found for Id: {director_id}")


def director_most_movies(limit=None, director_sort="asc"):
    '''
    This function responds to a request for /api/directors/mostmovies with the complete list of directors with most movies

    :params limit:  integer to limit top
    :params director_sort:  string enum to sort ascending or descending

    :return: json string of list of director with most movies
    '''

    # Create the list of directors from our data
    directors = Director.query.order_by(Director.id).limit(100).all()

    # Serialize the data for the response
    movie_sort = True
    if director_sort == "asc": 
        movie_sort = False
    else:
        movie_sort = True
    director_schema = DirectorSchema(many=True)
    datas = director_schema.dump(directors)
    for data in datas:
        data["total_movies"] = len(data["movies"])
        del data["movies"]
    new_data = sorted(datas, key=lambda x: x["total_movies"], reverse=movie_sort)
    if limit is None:
        return new_data
    else:
        return new_data[:limit]


def search(director_name, limit=None):
    '''
    This function respond to a request for /api/directors/{director_name}
    with one matching director from directors

    :param director_name:  Name of director to find
    :return:    director matching id
    '''
    # Build the initial query
    if limit is None:
        director = Director.query.order_by(Director.id).filter(Director.name.ilike('%'+director_name+'%')).all()
    else:    
        director = Director.query.order_by(Director.id).filter(Director.name.ilike('%'+director_name+'%')).limit(limit).all()

    if director == []:
        abort(404, f"Director not found for Id: {director_name}")

    else:
        directors_schema = DirectorSchema(many=True)
        data = directors_schema.dump(director)
        return data    
