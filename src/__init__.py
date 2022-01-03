from flask import Flask, jsonify
import os
from src.auth import auth
from src.car import car
from src.database import db
from flask_jwt_extended import JWTManager
from flasgger import Swagger, swag_from
from src.config.swagger import swagger_config, template

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config = True)

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DB_URI"),
            JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY'),
            SWAGGER={
                'title': "Tire Fitting API",
                'uiversion': 3
            }
        )
    else :
        app.config.from_mapping(test_config)


    db.app = app
    db.init_app(app)

    JWTManager(app)

    app.register_blueprint(auth)
    app.register_blueprint(car)

    Swagger(app, config=swagger_config, template=template)

    return app