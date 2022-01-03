from flask import Blueprint, jsonify, request
from src.constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT, handle_response
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity
from src.database import User, db
from src.constants.success_messages import token_data, info_user
from src.constants.error_messages import unauthorization_error, user_phone_already_exist, input_incorrect_phone
from flasgger import Swagger, swag_from

auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


@auth.post("/verification_status")
@swag_from('/src/docs/auth/verification_status.yaml')
def verification_status():
    phone = request.json['phone']

    status = "login"

    if User.query.filter_by(phone=phone).first() is None:
        status = "registration"
        
    return jsonify(
            handle_response(
                {
                    "status": status
                }
            )
        ), HTTP_200_OK


@auth.post("/register")
@swag_from('/src/docs/auth/register.yaml')
def register():
    phone = request.json['phone']
    password = request.json['password']

    if len(password) != 4:
        return input_incorrect_phone()

    if User.query.filter_by(phone=phone).first() is not None:
        return user_phone_already_exist()

    pwd_hash = generate_password_hash(password)

    user = User(phone = phone, password = pwd_hash)
    db.session.add(user)
    db.session.commit()

    refresh = create_refresh_token(identity=user.id)
    access = create_access_token(identity=user.id)

    return token_data(refresh=refresh, access=access)


@auth.post("/login")
@swag_from('/src/docs/auth/login.yaml')
def login():
    phone = request.json['phone']
    password = request.json['password']

    user = User.query.filter_by(phone=phone).first()

    if user:
        is_pass_correct = check_password_hash(user.password, password)

        if is_pass_correct:
            refresh = create_refresh_token(identity=user.id)
            access = create_access_token(identity=user.id)

            return token_data(refresh, access)

    return unauthorization_error()


@auth.get("/me")
@swag_from('/src/docs/user/info_user.yaml')
@jwt_required()
def me():
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()
    return info_user(user)


@auth.get("/token/refresh")
def refresh_users_token():
    identity = get_jwt_identity()
    access = create_access_token(identity=identity)

    return jsonify({
        "access": access
    }), HTTP_200_OK
