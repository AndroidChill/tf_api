from flask import Blueprint, jsonify, request
from src.constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT, handle_response
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity
from src.database import User, db, CarDisk
from src.constants.success_messages import created_tire, token_data, info_user, updated_tire
from src.constants.error_messages import unauthorization_error, user_phone_already_exist, input_incorrect_phone
from flasgger import Swagger, swag_from

tire = Blueprint("tire", __name__, url_prefix="/api/v1/tire")

@tire.post("/create")
@jwt_required()
@swag_from('/src/docs/car/tire_create.yaml')
def tire_create():

    brand = request.json['brand']
    radius = request.json['radius']
    lifetime = request.json["lifetime"]
    car_id = request.json["car_id"]

    carDiskOld = CarDisk.query.filter_by(car_id=car_id).first()

    if carDiskOld is not None:
        carDiskOld.brand = brand
        carDiskOld.radius = radius
        carDiskOld.lifetime = lifetime

        db.session.commit()

        return updated_tire(carDiskOld)
    else :
        carDisk = CarDisk(
            brand=brand,
            radius=radius,
            lifetime=lifetime,
            car_id=car_id
        )

        db.session.add(carDisk)
        db.session.commit()

    return created_tire(carDisk)
