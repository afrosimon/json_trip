from app import db


class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(500), nullable=False)
    country_name = db.Column(db.String(500), nullable=False)
    latitude = db.Column(db.Numeric(precision=6))
    longitude = db.Column(db.Numeric(precision=6))
    arrival_date = db.Column(db.Date(), nullable=False)
    departure_date = db.Column(db.Date(), nullable=False)
