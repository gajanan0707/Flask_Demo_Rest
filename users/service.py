from users.models import User
from users.validation import CreateSignupInputSchema
from utils.common import generate_response
from utils.http_code import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from server import db


def create_user(request, input_data):
    create_validation_schema = CreateSignupInputSchema()
    errors = create_validation_schema.validate(input_data)
    if errors:
        return generate_response(message=errors)
    check_username_exist = User.query.filter_by(
        username=input_data.get("username")
    ).first()
    check_email_exist = User.query.filter_by(email=input_data.get("email")).first()
    if check_username_exist:
        return generate_response(
            message="Email already exist", status=HTTP_400_BAD_REQUEST
        )
    elif check_username_exist:
        return generate_response(
            message="Username already taken", status=HTTP_400_BAD_REQUEST
        )

    new_user = User(**input_data)  # Create an instance of the User class
    new_user.hash_password()
    db.session.add(new_user)  # Adds new User record to database
    db.session.commit()  # Comment
    del input_data["password"]
    return generate_response(
        data=input_data, message="User Created", status=HTTP_201_CREATED
    )
