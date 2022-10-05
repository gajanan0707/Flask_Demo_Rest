from marshmallow import Schema, fields, validate


# "This class defines the input schema for the CreateSignup mutation. It requires a username, email,
# and password. The username must be at least 4 characters long, and the password must be at least 6
# characters long."
#
# The input schema is used to validate the input data before it is passed to the mutation
class CreateSignupInputSchema(Schema):
    # the 'required' argument ensures the field exists
    username = fields.Str(required=True, validate=validate.Length(min=4))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))


# "CreateLoginInputSchema is a schema that validates a dictionary with keys 'email' and 'password'
# where 'email' is a valid email address and 'password' is a string with a minimum length of 6
# characters."
#
# The above class is a subclass of the Schema class from the marshmallow library. The Schema class is
# a class that validates dictionaries. The Schema class has a class attribute called fields which is a
# dictionary. The keys of the fields dictionary are the keys of the dictionary that the Schema class
# validates. The values of the fields dictionary are instances of the Field class from the marshmallow
# library. The Field class is a class that validates values
class CreateLoginInputSchema(Schema):
    # the 'required' argument ensures the field exists
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))


# "The CreateResetPasswordEmailSendInputSchema class is a schema that validates the input for the
# create_reset_password_email_send function."
#
# The CreateResetPasswordEmailSendInputSchema class is a schema that validates the input for the
# create_reset_password_email_send function
class CreateResetPasswordEmailSendInputSchema(Schema):
    # the 'required' argument ensures the field exists
    email = fields.Email(required=True)

class ResetPasswordInputSchema(Schema):
    # the 'required' argument ensures the field exists
    password = fields.Str(required=True, validate=validate.Length(min=6))
