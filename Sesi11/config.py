import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# creates the variable basedir pointing to the directory the program is running in.
basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connex_app.app

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True # This causes SQLAlchemy to echo SQL statements it executes to the console. This is very useful to debug problems when building database programs. Set this to False for production environments.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mqjjtucgdxxaqy:3cd53e7afa104e28b1eeb580738c7ead2f7102d8ea59ac43bb3e120da9b98d6a@ec2-52-86-177-34.compute-1.amazonaws.com:5432/dcl5bg1c6clql0' # This tells SQLAlchemy to use SQLite as the database, and a file named people.db in the current directory as the database file. Different database engines, like MySQL and PostgreSQL, will have different SQLALCHEMY_DATABASE_URI strings to configure them.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # turning off the SQLAlchemy event system, which is on by default. The event system generates events useful in event-driven programs but adds significant overhead. Since you’re not creating an event-driven program, turn this feature off.

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)