from src.constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, handle_error, handle_response
from flask import jsonify

def token_data(refresh, access):
    return jsonify(
        handle_response(
            {
                "refresh": refresh,
                "access": access
            }
        )
    ), HTTP_201_CREATED


def info_user(user):
    return jsonify(
        handle_response(
            {
                "first_name": user.first_name,
                "second_name": user.second_name,
                "third_name": user.third_name,
                "phone": user.phone,
                "email": user.email,
                "city": user.city,
                "created_at": user.created_at,
                "updated_at": user.updated_at
            }
        )
    ), HTTP_200_OK