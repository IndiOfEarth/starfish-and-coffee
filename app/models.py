# Holds all database models
from app import db

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), unique=True, nullable=False)
    img_url = db.Column(db.String(500), unique=True, nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Integer, nullable=False)
    has_toilet = db.Column(db.Integer, nullable=False)
    has_wifi = db.Column(db.Integer, nullable=False)
    can_take_calls = db.Column(db.Integer, nullable=False)
    seats = db.Column(db.Integer, nullable=False)
    coffee_price = db.Column(db.String(50), nullable=False)

    # __repr__ returns the string representation of an object
    # Allows each cafe to be identified by its name when printed
    def __repr__(self):
        return f'<Cafe {self.name}>'
