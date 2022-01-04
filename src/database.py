from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    second_name = db.Column(db.String)
    third_name = db.Column(db.String)
    phone = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(80))
    password = db.Column(db.String(80))
    city = db.Column(db.String(80))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __repr__(self) -> str:
        return str(self.serialize())

    def serialize(self):
        return {
            "first_name": self.first_name,
            "second_name": self.second_name,
            "third_name": self.third_name,
            "phone": self.phone,
            "email": self.email,
            "password": self.password,
            "city": self.city,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(80))
    model = db.Column(db.String(80))
    year = db.Column(db.Integer)
    number = db.Column(db.Integer)
    series = db.Column(db.String(80))
    region = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __repr__(self):
        return str(self.serialize())

    def serialize(self):
        return {
            "brand": self.brand,
            "model": self.model,
            "year": self.year,
            "number": self.number,
            "series": self.series,
            "region": self.region,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


class CarDisk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(80))
    radius = db.Column(db.String(80))
    lifetime = db.Column(db.String(80))
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'))

    def __repr__(self):
        return str(self.serialize())

    def serialize(self):
        return {
            "brand": self.brand,
            "radius": self.radius,
            "lifetime": self.lifetime,
            "car_id": self.car_id
        }


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    second_name = db.Column(db.String(80))
    third_name = db.Column(db.String(80))
    rate = db.Column(db.Float, default = 0.0)

    def __repr__(self) -> str:
        return str(self.serialize())

    def serialize(self):
        return {
            "first_name": self.first_name,
            "second_name": self.second_name,
            "third_name": self.third_name,
            "rate": self.rate
        }