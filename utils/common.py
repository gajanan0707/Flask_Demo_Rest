import os
import jwt
from datetime import datetime, timedelta, timezone
from utils.http_code import HTTP_200_OK, HTTP_201_CREATED


def generate_response(data=None, message=None, status=400):
    """
    It takes in a data, message, and status, and returns a dictionary with the data, message, and status

    :param data: The data that you want to send back to the client
    :param message: This is the message that you want to display to the user
    :param status: The HTTP status code, defaults to 400 (optional)
    :return: A dictionary with the keys: data, message, status.
    """
    if status == HTTP_200_OK or status == HTTP_201_CREATED:
        status_bool = True
    else:
        status_bool = False

    return {
        "data": data,
        "message": modify_slz_error(message, status_bool),
        "status": status_bool,
    }, status


def modify_slz_error(message, status):
    """
    It takes a message and a status, and returns a list of errors

    :param message: The error message that you want to display
    :param status: The HTTP status code you want to return
    :return: A list of dictionaries.
    """
    final_error = list()
    if message:
        if type(message) == str:
            if not status:
                final_error.append({"error": message})
            else:
                final_error = message
        elif type(message) == list:
            final_error = message
        else:
            for key, value in message.items():
                final_error.append({"error": str(key) + ": " + str(value[0])})
    else:
        final_error = None
    return final_error


class TokenGenerator:
    @staticmethod
    def encode_token(user):
        """
        The encode_token function takes in a user object and returns a token

        :param user: The user object that we want to encode
        :return: A token
        """

        payload = {
            "exp": datetime.now(timezone.utc) + timedelta(days=1),
            "id": str(user.id),
        }
        token = jwt.encode(payload, os.environ.get("SECRET_KEY"), algorithm="HS256")
        return token

    @staticmethod
    def decode_token(token):
        """
        It takes a token, decodes it, and returns the decoded token

        :param token: The token to decode
        :return: A dictionary with the user's id and username.
        """
        return jwt.decode(
            token,
            os.environ.get("SECRET_KEY"),
            algorithms="HS256",
            options={"require_exp": True},
        )

    @staticmethod
    def check_token(token):
        """
        It takes a token, and returns True if the token is valid, and False if it's not

        :param token: The token to be decoded
        :return: A boolean value.
        """
        try:
            jwt.decode(
                token,
                os.environ.get("SECRET_KEY"),
                algorithms="HS256",
                options={"require_exp": True},
            )
            return True
        except:
            return False

    @staticmethod
    def get_user_id(token):
        """
        It decodes the token, and returns the user's id

        :param token: The token that was sent to the server
        :return: The user id is being returned.
        """
        data = jwt.decode(
            token,
            os.environ.get("SECRET_KEY"),
            algorithms="HS256",
            options={"require_exp": True},
        )
        return data["id"]


token_generator = TokenGenerator()
