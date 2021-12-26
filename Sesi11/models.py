from datetime import datetime
from config import db, ma

# Define the Person class as discussed in the data modeling section above, but now you know where the db.Model that the class inherits from originates. This gives the Person class SQLAlchemy features, like a connection to the database and access to its tables.
class Person(db.Model):
    __tablename__ = 'person'
    person_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), index=True)
    fname = db.Column(db.String(32))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


# Define the PersonSchema class as was discussed in the data serialzation section above. This class inherits from ma.ModelSchema and gives the PersonSchema class Marshmallow features, like introspecting the Person class to help serialize/deserialize instances of that class.
class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        sqla_session = db.session 
        load_instance = True