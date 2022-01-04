from flask import Flask, jsonify
import os
from src.auth import auth
from src.car import car
from src.tire import tire
from src.employee import employee
from src.database import db
from datetime import timedelta
from flask_jwt_extended import JWTManager
from flasgger import Swagger, swag_from
from src.config.swagger import swagger_config, template
from flask_migrate import Migrate

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config = True)

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY='SECRET_KEY',
            SQLALCHEMY_DATABASE_URI="sqlite:///tf_db.db",
            JWT_SECRET_KEY='JWT_SECRET_KEY',
            JWT_ACCESS_TOKEN_EXPIRES=36600,
            SQLALCHEMY_TRACK_MODIFICATIONS = False,
            SWAGGER={
                'title': "Tire Fitting API",
                'uiversion': 3
            }
        )
    else :
        app.config.from_mapping(test_config)

    migrate = Migrate()

    db.app = app
    db.init_app(app)

    migrate.init_app(app, db)

    JWTManager(app)

    app.register_blueprint(auth)
    app.register_blueprint(car)
    app.register_blueprint(tire)
    app.register_blueprint(employee)

    Swagger(app, config=swagger_config, template=template)

    return app