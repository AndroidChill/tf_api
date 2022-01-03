from flask import Blueprint

car = Blueprint("car", __name__, url_prefix="/api/v1/car")

@car.get("/")
def get_all():
    return {"cars": []}