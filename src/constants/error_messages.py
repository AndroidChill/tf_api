from src.constants.http_status_codes import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT, handle_error
from flask import jsonify

def input_incorrect_phone():
    return jsonify(
        handle_error(
            HTTP_400_BAD_REQUEST,
            "Введите корректную длину телефона"
        )
)

def user_phone_already_exist():
    return jsonify(
        handle_error(
            HTTP_409_CONFLICT,
            "Пользователь с данным номером телефона уже существует"
        )
)

def unauthorization_error():
    return jsonify(
        handle_error(
            HTTP_401_UNAUTHORIZED,
            "Ошибка авторизации"
        )
)

def incorrect_car_create():
    return jsonify(
        handle_error(
            HTTP_400_BAD_REQUEST,
            "Некорректные данные, проверьте правильность ввода"
        )
    )

def car_already_exist():
    return jsonify(
        handle_error(
            HTTP_409_CONFLICT,
            "Вы уже создавали такую машину"
        )
)