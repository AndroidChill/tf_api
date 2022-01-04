from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.constants.error_messages import car_already_exist, incorrect_car_create
from src.constants.success_messages import created_car
from src.database import Car
from src.database import db
from flasgger import Swagger, swag_from

car = Blueprint("car", __name__, url_prefix="/api/v1/car")

@car.post("/create")
@jwt_required()
@swag_from('/src/docs/car/car_create.yaml')
def create():

    car = None

    full_info = request.json['full_info']
    series = request.json['series']
    number = request.json['number']
    region = request.json['region']
    user_id = get_jwt_identity()

    if full_info:
        brand = request.json['brand']
        model = request.json['model']
        year = request.json['year']

        car = Car(
        brand=brand, 
        model=model, 
        year=year, 
        series=series,
        number=number,
        region=region, 
        user_id=user_id
    )
    else:
        car = Car(
            brand="", 
            model="", 
            year=-1, 
            series=series,
            number=number,
            region=region, 
            user_id=user_id
        )

    if car:

        if Car.query.filter_by(series=series, number=number, region=region).first() is not None:
            return car_already_exist()
        else:
            db.session.add(car)
            db.session.commit()

            return created_car(car)

    return incorrect_car_create()


@car.get("/")
def get_all():
    return {"cars": []}