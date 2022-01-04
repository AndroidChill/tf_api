from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.constants.error_messages import car_already_exist, incorrect_car_create
from src.constants.http_status_codes import HTTP_200_OK, handle_response
from src.constants.success_messages import created_car, created_employee
from src.database import Car, Employee
from src.database import db
from flasgger import Swagger, swag_from

employee = Blueprint("employee", __name__, url_prefix="/api/v1/employee")

@employee.post("/create")
@swag_from('/src/docs/employee/employee_create.yaml')
def employee_create():
    first_name = request.json['first_name']
    second_name = request.json['second_name']
    third_name = request.json['third_name']

    empl = Employee(
        first_name=first_name,
        second_name=second_name,
        third_name=third_name
    )

    db.session.add(empl)
    db.session.commit()

    return created_employee(empl)


@employee.get("/list")
@swag_from('/src/docs/employee/employee_list.yaml')
def employee_list():
    return jsonify(
        handle_response({
            "employes" : [item.serialize() for item in Employee.query.all()]
        })
    ), HTTP_200_OK
