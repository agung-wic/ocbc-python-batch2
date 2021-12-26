import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Masrhmallow

basedir = os.path.abspath(os.path.dirname(__file__))

connexApp = connexion.App(__name__, specification_dir=basedir)

app = connexApp.app

app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'avocado.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


ma = Marshmallow(app)