from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if isinstance(exc, ValidationError):
        if response.data.get("username", None):
            response.data['detail'] = response.data["username"][0]
        elif response.data.get("email", None):
            response.data['detail'] = response.data["email"][0]
        elif response.data.get("password", None):
            response.data['detail'] = response.data["password"][0]
    return response
