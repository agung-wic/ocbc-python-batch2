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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'final_project.db')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://qadhatmqcywlzr:170574220a1e54fcef2e007bcfe74834d4567162b191f18c08590928c56b5f52@ec2-3-217-216-13.compute-1.amazonaws.com:5432/d5fqcu93j5ppto' # This tells SQLAlchemy to use SQLite as the database, and a file named people.db in the current directory as the database file. Different database engines, like MySQL and PostgreSQL, will have different SQLALCHEMY_DATABASE_URI strings to configure them.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # turning off the SQLAlchemy event system, which is on by default. The event system generates events useful in event-driven programs but adds significant overhead. Since you’re not creating an event-driven program, turn this feature off.

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)