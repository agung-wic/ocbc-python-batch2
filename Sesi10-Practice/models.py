from datetime import datetime
from config import db, ma
from marshmallow import fields

class Avotype(db.model):
    __tablename__ = 'avotype'
    type_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(32))
    avocado = db.relationship(
        'Avocado',
        backref = 'avotype',
        cascade = 'all, delete, delete-orphan',
        
    )